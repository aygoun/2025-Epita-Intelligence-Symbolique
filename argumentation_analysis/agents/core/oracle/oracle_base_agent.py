# argumentation_analysis/agents/core/oracle/oracle_base_agent.py
"""
Fondations pour les agents de type "Oracle".

Ce module fournit deux classes essentielles :
1.  `OracleTools`: Un plugin natif pour Semantic Kernel qui expose des fonctions
    (outils) pour interagir avec le système de permissions et d'accès aux
    données. C'est la "façade" que le LLM de l'agent peut utiliser.
2.  `OracleBaseAgent`: Une classe de base abstraite pour tous les agents qui
    agissent comme des gardiens de données. Elle intègre le `OracleTools` et
    le `DatasetAccessManager` pour fournir une base robuste avec un contrôle
    d'accès et un logging intégrés.
"""

import logging
from typing import Dict, List, Any, Optional, ClassVar
from datetime import datetime

from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
# Note: ChatCompletionAgent might not be available in this version of semantic_kernel
# Using a mock or fallback approach for tests
# CORRECTIF COMPATIBILITÉ: Utilisation du module de compatibilité
try:
    from semantic_kernel.contents import ChatCompletionAgent
except ImportError:
    # Fallback for older versions of semantic_kernel
    ChatCompletionAgent = None

from ..abc.agent_bases import BaseAgent
from .dataset_access_manager import DatasetAccessManager
from .permissions import QueryType, OracleResponse, PermissionManager
from argumentation_analysis.utils.performance_monitoring import monitor_performance


class OracleTools:
    """
    Plugin d'outils natifs pour l'interaction avec le système Oracle.

    Cette classe regroupe des fonctions natives (`@kernel_function`) qui
    servent d'interface entre le monde du LLM (qui manipule des chaînes de
    caractères) et la logique métier de l'Oracle (gérée par le
    `DatasetAccessManager`).
    """

    def __init__(self, dataset_manager: DatasetAccessManager, agent_name: Optional[str] = None):
        """
        Initialise le plugin d'outils.

        Args:
            dataset_manager (DatasetAccessManager): L'instance du gestionnaire
                d'accès aux données qui contient la logique de permission et de requête.
            agent_name (Optional[str]): Le nom de l'agent propriétaire de ces outils.
        """
        self.dataset_manager = dataset_manager
        self.agent_name = agent_name or "OracleTools"
        self._logger = logging.getLogger(self.__class__.__name__)

    @kernel_function(name="validate_query_permission", description="Valide qu'un agent a la permission pour un type de requête.")
    def validate_query_permission(self, agent_name: str, query_type: str) -> str:
        """
        Vérifie si un agent a la permission d'exécuter un type de requête.

        Args:
            agent_name (str): Le nom de l'agent dont la permission est vérifiée.
            query_type (str): Le type de requête (ex: 'card_inquiry').

        Returns:
            str: Un message confirmant ou infirmant l'autorisation.
        """
        try:
            query_type_enum = QueryType(query_type)
            is_authorized = self.dataset_manager.check_permission(agent_name, query_type_enum)
            
            if is_authorized:
                return f"Agent {agent_name} autorisé pour {query_type}"
            else:
                return f"Agent {agent_name} NON autorisé pour {query_type}"
                
        except ValueError:
            return f"Type de requête invalide: {query_type}"
        except Exception as e:
            self._logger.error(f"Erreur validation permission: {e}")
            return f"Erreur lors de la validation: {str(e)}"
    
    @kernel_function(name="execute_authorized_query", description="Exécute une requête autorisée sur le dataset.")
    def execute_authorized_query(self, agent_name: str, query_type: str, query_params: str) -> str:
        """
        Exécute une requête après avoir implicitement validé les permissions.

        Cette fonction délègue l'exécution au `DatasetAccessManager`, qui
        gère à la fois la vérification des permissions et l'exécution de la
        requête.

        Args:
            agent_name (str): Le nom de l'agent qui soumet la requête.
            query_type (str): Le type de requête.
            query_params (str): Les paramètres de la requête, sous forme de chaîne JSON.

        Returns:
            str: Un message décrivant le résultat de l'exécution.
        """
        try:
            import json
            
            # Parsing des paramètres
            try:
                params_dict = json.loads(query_params) if isinstance(query_params, str) else query_params
            except json.JSONDecodeError:
                return f"Erreur: Paramètres JSON invalides: {query_params}"
            
            query_type_enum = QueryType(query_type)
            
            # Exécution via le gestionnaire
            response = self.dataset_manager.execute_oracle_query(agent_name, query_type_enum, params_dict)
            
            if response.authorized:
                result_msg = f"Requête exécutée avec succès: {response.message}"
                if response.revealed_information:
                    result_msg += f" | Informations révélées: {', '.join(response.revealed_information)}"
                return result_msg
            else:
                return f"Requête refusée: {response.message}"
                
        except ValueError:
            return f"Type de requête invalide: {query_type}"
        except Exception as e:
            self._logger.error(f"Erreur exécution requête: {e}", exc_info=True)
            return f"Erreur lors de l'exécution: {str(e)}"
    
    @kernel_function(name="get_available_query_types", description="Récupère les types de requêtes autorisés pour un agent.")
    def get_available_query_types(self, agent_name: str) -> str:
        """
        Récupère la liste des requêtes autorisées et les statistiques pour un agent.

        Args:
            agent_name (str): Le nom de l'agent concerné.

        Returns:
            str: Une chaîne de caractères résumant les permissions, le quota
                 et la politique de révélation de l'agent.
        """
        try:
            permission_rule = self.dataset_manager.get_agent_permissions(agent_name)
            
            if not permission_rule:
                return f"Aucune permission configurée pour {agent_name}"
            
            allowed_types = [qt.value for qt in permission_rule.allowed_query_types]
            stats = self.dataset_manager.permission_manager.get_query_stats(agent_name)
            
            result = f"Types autorisés pour {agent_name}: {', '.join(allowed_types)}"
            result += f" | Quota: {stats.get('daily_queries_used', 0)}/{stats.get('daily_queries_limit', 0)}"
            result += f" | Politique: {stats.get('reveal_policy', 'unknown')}"
            
            return result
            
        except Exception as e:
            self._logger.error(f"Erreur récupération types de requêtes: {e}")
            return f"Erreur: {str(e)}"
    
    @kernel_function(name="reveal_information_controlled", description="Révèle des informations selon la politique de révélation.")
    def reveal_information_controlled(self, target_agent: str, information_type: str, context: str = "") -> str:
        """
        Révèle des informations de manière contrôlée (placeholder).

        Note:
            Cette fonction est un placeholder destiné à être surchargé par des
            agents Oracle spécialisés pour implémenter des logiques de
            révélation complexes.

        Args:
            target_agent (str): L'agent à qui l'information est révélée.
            information_type (str): Le type d'information à révéler.
            context (str): Contexte additionnel pour la décision.

        Returns:
            str: Un message confirmant la demande de révélation.
        """
        try:
            # Cette méthode sera surchargée par les agents spécialisés
            return f"Révélation d'information demandée pour {target_agent} - Type: {information_type}"
            
        except Exception as e:
            self._logger.error(f"Erreur révélation contrôlée: {e}")
            return f"Erreur lors de la révélation: {str(e)}"
    
    @kernel_function(name="query_oracle_dataset", description="Exécute une requête sur le dataset Oracle.")
    async def query_oracle_dataset(self, query_type: str, query_params: str) -> str:
        """
        Exécute une requête sur le dataset pour le compte de l'agent propriétaire.

        Cette fonction est une version asynchrone de `execute_authorized_query`.

        Args:
            query_type (str): Le type de requête à exécuter.
            query_params (str): Les paramètres de la requête en format JSON.

        Returns:
            str: Un message résumant le résultat de la requête.
        """
        try:
            import json
            
            # Parsing des paramètres
            try:
                params_dict = json.loads(query_params) if isinstance(query_params, str) else query_params
            except json.JSONDecodeError:
                return f"Erreur de format JSON: {query_params}"
            
            try:
                query_type_enum = QueryType(query_type)
            except ValueError:
                raise ValueError(f"Type de requête invalide: {query_type}")
            
            # Exécution via le gestionnaire
            response = await self.dataset_manager.execute_oracle_query(
                agent_name=self.agent_name,
                query_type=query_type_enum,
                query_params=params_dict
            )
            
            if response.authorized:
                result_msg = f"Requête Oracle exécutée: {response.message}"
                if response.revealed_information:
                    result_msg += f" | Révélations: {', '.join(response.revealed_information)}"
                return result_msg
            else:
                return f"Requête Oracle refusée: {response.message}"
                
        except ValueError:
            raise ValueError(f"Type de requête invalide: {query_type}")
        except Exception as e:
            self._logger.error(f"Erreur requête Oracle: {e}", exc_info=True)
            return f"Erreur lors de la requête Oracle: {str(e)}"
    
    @kernel_function(name="execute_oracle_query", description="Exécute une requête Oracle avec gestion complète.")
    async def execute_oracle_query(self, query_type: str, query_params: str) -> str:
        """
        Exécute une requête Oracle (version sémantiquement redondante).

        Note:
            Cette fonction semble être fonctionnellement identique à
            `query_oracle_dataset`. À conserver pour la compatibilité
            sémantique si des plans l'utilisent.

        Args:
            query_type (str): Le type de requête.
            query_params (str): Les paramètres de la requête en format JSON.

        Returns:
            str: Un message résumant le résultat de la requête.
        """
        try:
            import json
            
            # Parsing des paramètres
            try:
                params_dict = json.loads(query_params) if isinstance(query_params, str) else query_params
            except json.JSONDecodeError:
                return f"Erreur de format JSON: {query_params}"
            
            try:
                query_type_enum = QueryType(query_type)
            except ValueError:
                raise ValueError(f"Type de requête invalide: {query_type}")
            
            # Exécution via le gestionnaire
            response = await self.dataset_manager.execute_oracle_query(
                agent_name=self.agent_name,
                query_type=query_type_enum,
                query_params=params_dict
            )
            
            if response.authorized:
                return f"Requête Oracle exécutée: {response.message}"
            else:
                return f"Requête Oracle refusée: {response.message}"
                
        except ValueError:
            raise ValueError(f"Type de requête invalide: {query_type}")
        except Exception as e:
            self._logger.error(f"Erreur requête Oracle: {e}", exc_info=True)
            return f"Erreur lors de la requête Oracle: {str(e)}"
    
    @kernel_function(name="check_agent_permission", description="Vérifie les permissions d'un agent.")
    async def check_agent_permission(self, query_type: str, target_agent: str = None) -> str:
        """
        Vérifie les permissions d'un agent pour un type de requête.

        Version asynchrone de `validate_query_permission`.

        Args:
            query_type (str): Le type de requête à vérifier.
            target_agent (str, optional): L'agent à vérifier. Si None, vérifie
                les permissions de l'agent propriétaire de l'outil. Defaults to None.

        Returns:
            str: Un message confirmant ou infirmant l'autorisation.
        """
        try:
            query_type_enum = QueryType(query_type)
            agent_to_check = target_agent or self.agent_name
            is_authorized = await self.dataset_manager.check_permission(agent_to_check, query_type_enum)
            
            if is_authorized:
                return f"{agent_to_check} a les permissions pour {query_type}"
            else:
                return f"{agent_to_check} n'a pas les permissions pour {query_type}"
                
        except ValueError as e:
            self._logger.error(f"Type de requête invalide: {query_type}")
            raise ValueError(f"Type de requête invalide: {query_type}")
        except Exception as e:
            self._logger.error(f"Erreur vérification permission: {e}")
            return f"Erreur lors de la vérification: {str(e)}"
    
    @kernel_function(name="validate_agent_permissions", description="Valide les permissions d'un agent.")
    async def validate_agent_permissions(self, target_agent: str, query_type: str) -> str:
        """
        Valide les permissions d'un agent (alias sémantique).

        Cette fonction est un alias de `check_agent_permission` pour des raisons
        de clarté sémantique dans les plans du LLM.
        """
        return await self.check_agent_permission(query_type, target_agent)


class OracleBaseAgent(BaseAgent):
    """
    Classe de base pour les agents qui agissent comme des gardiens de données.

    Cet agent sert de fondation pour des agents spécialisés (comme un agent
    gérant un deck de cartes, un autre gérant des archives, etc.). Il intègre
    nativement un `DatasetAccessManager` pour le contrôle fin des permissions
    et un `OracleTools` pour exposer ses capacités à un LLM.

    Les responsabilités principales de cette classe de base sont :
    -   Recevoir et traiter des requêtes via `process_oracle_request`.
    -   Déléguer la logique de permission et d'exécution au `DatasetAccessManager`.
    -   Tenir un journal d'audit de toutes les interactions (`access_log`).
    -   Exposer un ensemble standard d'outils et de statistiques.
    """
    
    # Prompt système de base pour tous les agents Oracle
    BASE_ORACLE_SYSTEM_PROMPT: ClassVar[str] = """Vous êtes un Agent Oracle, gardien des données et des informations.

**VOTRE RÔLE :**
Vous détenez l'accès exclusif à un dataset spécifique et vous gérez les révélations d'information selon des règles strictes de permissions et de stratégie.

**PROTOCOLE ORACLE :**
1. **VALIDATION DES PERMISSIONS** : Vérifiez toujours que l'agent demandeur a les autorisations nécessaires
2. **EXÉCUTION CONTRÔLÉE** : Traitez les requêtes selon votre politique de révélation
3. **RÉVÉLATION STRATÉGIQUE** : Dosez l'information révélée selon le contexte et la stratégie
4. **AUDIT COMPLET** : Enregistrez toutes les interactions pour traçabilité

**OUTILS DISPONIBLES :**
- `validate_query_permission(agent_name, query_type)`: Vérifier les autorisations
- `execute_authorized_query(agent_name, query_type, query_params)`: Exécuter une requête
- `get_available_query_types(agent_name)`: Consulter les permissions d'un agent
- `reveal_information_controlled(target_agent, information_type, context)`: Révélation contrôlée

**RÈGLES DE CONDUITE :**
- Ne révélez JAMAIS d'informations sans vérification préalable des permissions
- Respectez votre politique de révélation (progressive/cooperative/competitive/balanced)
- Maintenez la cohérence des informations révélées
- Documentez chaque interaction pour auditabilité

Vous êtes un gardien impartial mais stratégique des données."""
    
    dataset_manager: DatasetAccessManager
    
    def __init__(self,
                 kernel: Kernel,
                 dataset_manager: DatasetAccessManager,
                 agent_name: str = "OracleAgent",
                 custom_instructions: Optional[str] = None,
                 access_level: Optional[str] = None,
                 system_prompt_suffix: Optional[str] = None,
                 allowed_query_types: Optional[List[QueryType]] = None,
                 plugins: Optional[List] = None,
                 **kwargs):
        """
        Initialise une instance de `OracleBaseAgent`.

        Args:
            kernel (Kernel): L'instance du kernel Semantic Kernel.
            dataset_manager (DatasetAccessManager): Le gestionnaire qui contrôle
                l'accès au jeu de données sous-jacent.
            agent_name (str): Le nom de cet agent.
            custom_instructions (Optional[str]): Instructions spécialisées à ajouter
                au prompt système de base.
            access_level (Optional[str]): Niveau d'accès de l'agent (pour tests).
            system_prompt_suffix (Optional[str]): Suffixe à ajouter au prompt système.
            allowed_query_types (Optional[List[QueryType]]): Types de requêtes que
                cet agent peut traiter.
            plugins (Optional[List]): Plugins additionnels à enregistrer dans le kernel.
        """
        # Instructions système (base + personnalisées)
        base_prompt = """Vous êtes un Agent Oracle, gardien des données et des informations.

**VOTRE RÔLE :**
Vous détenez l'accès exclusif à un dataset spécifique et vous gérez les révélations d'information selon des règles strictes de permissions et de stratégie.

**PROTOCOLE ORACLE :**
1. **VALIDATION DES PERMISSIONS** : Vérifiez toujours que l'agent demandeur a les autorisations nécessaires
2. **EXÉCUTION CONTRÔLÉE** : Traitez les requêtes selon votre politique de révélation
3. **RÉVÉLATION STRATÉGIQUE** : Dosez l'information révélée selon le contexte et la stratégie
4. **AUDIT COMPLET** : Enregistrez toutes les interactions pour traçabilité

**OUTILS DISPONIBLES :**
- `validate_query_permission(agent_name, query_type)`: Vérifier les autorisations
- `execute_authorized_query(agent_name, query_type, query_params)`: Exécuter une requête
- `get_available_query_types(agent_name)`: Consulter les permissions d'un agent
- `reveal_information_controlled(target_agent, information_type, context)`: Révélation contrôlée

**RÈGLES DE CONDUITE :**
- Ne révélez JAMAIS d'informations sans vérification préalable des permissions
- Respectez votre politique de révélation (progressive/cooperative/competitive/balanced)
- Maintenez la cohérence des informations révélées
- Documentez chaque interaction pour auditabilité

Vous êtes un gardien impartial mais stratégique des données."""
        instructions = base_prompt
        if custom_instructions:
            instructions += f"\n\n**INSTRUCTIONS SPÉCIALISÉES :**\n{custom_instructions}"
        if system_prompt_suffix:
            instructions += f"\n\n{system_prompt_suffix}"
        
        # Initialiser BaseAgent
        super().__init__(
            kernel=kernel,
            agent_name=agent_name,
            system_prompt=instructions,
            **kwargs
        )
        
        # Stocker les attributs spécifiques à Semantic Kernel
        self.kernel = kernel
        
        # Initialisation des attributs spécifiques à Oracle
        self.dataset_manager = dataset_manager
        self.access_log = []
        self.revealed_information = set()
        self.access_level = access_level or "standard"
        
        # Configurer les types de requêtes autorisées
        if allowed_query_types is None:
            allowed_query_types = [QueryType.CARD_INQUIRY, QueryType.GAME_STATE, QueryType.CLUE_REQUEST]
        self.allowed_query_types = allowed_query_types
        
        # Outils Oracle
        self.oracle_tools = OracleTools(dataset_manager, agent_name)
        
        # Enregistrement des outils Oracle comme plugin dans le kernel (si kernel disponible)
        if kernel:
            kernel.add_plugin(self.oracle_tools, plugin_name=f"oracle_tools_{agent_name}")
            
            # Ajouter les plugins supplémentaires si fournis
            if plugins:
                for i, plugin in enumerate(plugins):
                    plugin_name = f"plugin_{agent_name}_{i}"
                    kernel.add_plugin(plugin, plugin_name=plugin_name)
        
        # Logger spécialisé
        self._logger = logging.getLogger(f"agent.{self.__class__.__name__}.{agent_name}")
        # Protection contre les Mock objects dans les tests
        try:
            dataset_name = type(dataset_manager.dataset).__name__
        except AttributeError:
            dataset_name = "RealDataset_Unknown"  # MOCK ÉLIMINÉ PHASE 3
        self._logger.info(f"OracleBaseAgent '{agent_name}' initialisé avec dataset: {dataset_name}")
    
    @monitor_performance(log_args=True)
    def process_oracle_request(self, requesting_agent: str, query_type: QueryType, query_params: Dict[str, Any]) -> OracleResponse:
        """
        Traite une requête adressée à l'Oracle de manière sécurisée.

        C'est le point d'entrée principal pour les interactions internes (agent-à-agent).
        Il délègue la requête au `DatasetAccessManager` et enregistre l'interaction
        pour l'audit.

        Args:
            requesting_agent (str): Le nom de l'agent qui effectue la requête.
            query_type (QueryType): Le type de requête (enum).
            query_params (Dict[str, Any]): Les paramètres de la requête.

        Returns:
            OracleResponse: Un objet structuré contenant le résultat de l'opération.
        """
        self._logger.info(f"Traitement demande Oracle: {requesting_agent} -> {query_type.value}")
        
        try:
            # Délégation au gestionnaire de dataset
            response = self.dataset_manager.execute_oracle_query(requesting_agent, query_type, query_params)
            
            # Enregistrement dans le log d'accès local
            self._log_oracle_interaction(requesting_agent, query_type, response)
            
            # Mise à jour des informations révélées
            if response.revealed_information:
                self.revealed_information.update(response.revealed_information)
            
            return response
            
        except Exception as e:
            self._logger.error(f"Erreur traitement demande Oracle: {e}", exc_info=True)
            
            error_response = OracleResponse(
                authorized=False,
                message=f"Erreur Oracle: {str(e)}",
                query_type=query_type,
                agent_name=requesting_agent,
                metadata={"error": str(e)}
            )
            
            self._log_oracle_interaction(requesting_agent, query_type, error_response)
            return error_response
    
    def _log_oracle_interaction(self, requesting_agent: str, query_type: QueryType, response: OracleResponse) -> None:
        """Enregistre une interaction Oracle dans le log local."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "requesting_agent": requesting_agent,
            "query_type": query_type.value,
            "authorized": response.authorized,
            "message": response.message,
            "revealed_information": response.revealed_information,
            "metadata": response.metadata
        }
        
        self.access_log.append(log_entry)
        self._logger.debug(f"Interaction Oracle enregistrée: {requesting_agent} -> {query_type.value} -> {response.authorized}")
    
    def get_oracle_statistics(self) -> Dict[str, Any]:
        """Retourne les statistiques de l'agent Oracle."""
        total_interactions = len(self.access_log)
        authorized_interactions = sum(1 for log in self.access_log if log["authorized"])
        
        stats = {
            "agent_name": self.name,
            "dataset_type": type(self.dataset_manager.dataset).__name__,
            "total_interactions": total_interactions,
            "authorized_interactions": authorized_interactions,
            "denied_interactions": total_interactions - authorized_interactions,
            "authorization_rate": authorized_interactions / total_interactions if total_interactions > 0 else 0.0,
            "total_revealed_items": len(self.revealed_information),
            "dataset_manager_stats": self.dataset_manager.get_access_statistics()
        }
        
        return stats
    
    def get_revealed_information_summary(self) -> Dict[str, Any]:
        """Retourne un résumé des informations révélées."""
        return {
            "total_items_revealed": len(self.revealed_information),
            "revealed_items": list(self.revealed_information),
            "revelation_timeline": [
                {
                    "timestamp": log["timestamp"],
                    "to_agent": log["requesting_agent"],
                    "items": log["revealed_information"]
                }
                for log in self.access_log
                if log["revealed_information"]
            ]
        }
    
    def reset_oracle_state(self) -> None:
        """Remet à zéro l'état de l'Oracle (pour tests ou nouveau jeu)."""
        self.access_log.clear()
        self.revealed_information.clear()
        self.dataset_manager.reset_statistics()
        self._logger.info(f"État Oracle {self.name} remis à zéro")
    
    # Implémentation des méthodes abstraites requises par BaseAgent
    
    def get_agent_capabilities(self) -> Dict[str, Any]:
        """Retourne les capacités spécifiques de l'agent Oracle."""
        return {
            "dataset_access": "Accès contrôlé aux datasets via permissions ACL",
            "permission_validation": "Validation des autorisations par agent et type de requête",
            "controlled_revelation": "Révélation d'informations selon stratégie configurée",
            "audit_logging": "Audit complet de toutes les interactions",
            "oracle_tools": self.get_agent_specific_tools(),
            "access_level": self.access_level,
            "allowed_query_types": [qt.value for qt in self.allowed_query_types]
        }
    
    def setup_agent_components(self, llm_service_id: str) -> None:
        """Configure les composants spécifiques de l'agent Oracle."""
        self._llm_service_id = llm_service_id
        # Les outils Oracle sont déjà configurés dans __init__
        self._logger.info(f"Agent Oracle '{self.name}' configuré avec service LLM: {llm_service_id}")
    
    async def get_response(self, message: str, **kwargs) -> str:
        """Obtient une réponse de l'agent Oracle."""
        # Pour l'Oracle, la réponse dépend du type de requête
        # Cette méthode peut être surchargée par les agents spécialisés
        self._logger.info(f"Oracle '{self.name}' reçoit message: {message[:100]}...")
        
        # Réponse basique - peut être améliorée selon les besoins
        return f"Oracle '{self.name}' a reçu votre message. Utilisez les outils Oracle pour des requêtes spécifiques."
    
    async def invoke_single(self, message: str = None, **kwargs) -> str:
        """
        Implémentation de la méthode invoke_single requise par BaseAgent.
        
        Args:
            message: Message à traiter par l'agent Oracle
            **kwargs: Arguments supplémentaires
            
        Returns:
            str: Réponse de l'agent Oracle
        """
        if message is None:
            message = kwargs.get('input', kwargs.get('query', ''))
        
        self._logger.info(f"Oracle '{self.name}' invoke_single appelé avec: {message[:100] if message else 'message vide'}...")
        
        # Pour un agent Oracle, on délègue vers get_response
        try:
            response = await self.get_response(message, **kwargs)
            return response
        except Exception as e:
            self._logger.error(f"Erreur lors de invoke_single: {e}")
            return f"Erreur Oracle: {str(e)}"
    
    # Properties héritées de BaseAgent : name, instructions, etc.
    
    # Méthodes à surcharger par les agents spécialisés
    
    def get_specialized_capabilities(self) -> Dict[str, str]:
        """Retourne les capacités spécialisées de cet agent Oracle."""
        return {
            "dataset_access": "Accès contrôlé aux datasets via permissions ACL",
            "permission_validation": "Validation des autorisations par agent et type de requête",
            "controlled_revelation": "Révélation d'informations selon stratégie configurée",
            "audit_logging": "Audit complet de toutes les interactions"
        }
    
    def get_agent_specific_tools(self) -> List[str]:
        """Retourne la liste des outils spécifiques à ce type d'agent."""
        return [
            "validate_query_permission",
            "execute_authorized_query",
            "get_available_query_types",
            "reveal_information_controlled"
        ]