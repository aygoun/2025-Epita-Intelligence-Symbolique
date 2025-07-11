# Cartographie de la Documentation du Projet
Date de génération: 2025-06-04

## Fichiers et Résumés

---
**Fichier:** `docs/architecture/README.md`
**Résumé:**
Ce document sert d'introduction à la section sur l'architecture du système d'analyse argumentative. Il explique que cette section détaillera la conception globale, les composants majeurs et leurs interactions, en mettant l'accent sur l'architecture hiérarchique à trois niveaux et les systèmes de communication inter-agents.

---
**Fichier:** `docs/architecture/architecture_distribuee.md`
**Résumé:**
Ce document décrit l'architecture distribuée du système d'analyse argumentative, conçue pour la scalabilité et la résilience. Il aborde la communication inter-services via des messages, la découverte de services, la gestion de l'état distribué et les stratégies de déploiement.

---
**Fichier:** `docs/architecture/communication_agents.md`
**Résumé:**
Ce document détaille le système de communication entre les agents du projet d'Intelligence Symbolique, incluant les protocoles (potentiellement FIPA-ACL), les formats de message (JSON-RPC), et l'infrastructure de messagerie (RabbitMQ ou ZeroMQ). Il aborde également la gestion des ontologies partagées et la sémantique des messages pour assurer une interopérabilité efficace.

---
**Fichier:** `docs/architecture/flux_donnees_analyse.md`
**Résumé:**
Ce document décrit le flux de données pour le processus d'analyse argumentative, depuis la réception du texte brut jusqu'à la génération des résultats. Il détaille les étapes de prétraitement, d'extraction d'arguments, d'analyse de la structure, de détection de sophismes, et de validation logique, en précisant les formats de données échangés entre les composants.

---
**Fichier:** `docs/architecture/gestion_erreurs_exceptions.md`
**Résumé:**
Ce document spécifie la stratégie de gestion des erreurs et des exceptions au sein du système d'analyse argumentative. Il couvre la classification des erreurs (entrée invalide, problème de ressource, erreur interne), les mécanismes de logging, les stratégies de reprise sur erreur, et la manière dont les erreurs sont propagées et présentées à l'utilisateur ou aux systèmes clients.

---
**Fichier:** `docs/architecture/securite_acces.md`
**Résumé:**
Ce document aborde les aspects de sécurité et de contrôle d'accès pour le système d'analyse argumentative. Il traite de l'authentification des utilisateurs et des services, de l'autorisation basée sur les rôles pour l'accès aux fonctionnalités et aux données, de la protection des données sensibles (chiffrement, anonymisation) et de la journalisation des audits de sécurité.

---
**Fichier:** `docs/composants/README.md`
**Résumé:**
Ce README introduit la section de la documentation dédiée aux composants du système d'analyse argumentative. Il explique que cette section fournira une description détaillée de chaque module, son rôle, ses responsabilités, ses interfaces et ses dépendances avec les autres composants du système.

---
**Fichier:** `docs/composants/agent_analyse_formelle.md`
**Résumé:**
Ce document décrit l'agent d'analyse formelle, responsable de la validation logique des arguments et de la construction de frameworks d'argumentation (comme ceux de Dung). Il détaille son intégration avec TweetyProject, les types de logiques supportées (propositionnelle, premier ordre) et son API pour interagir avec les autres composants.

---
**Fichier:** `docs/composants/agent_analyse_informelle.md`
**Résumé:**
Ce document spécifie l'agent d'analyse informelle, chargé de la détection de sophismes et de l'évaluation de la qualité rhétorique des arguments. Il décrit les techniques NLP utilisées, la taxonomie des sophismes employée, et son interaction avec les modèles de langage pour l'analyse.

---
**Fichier:** `docs/composants/api_web.md`
**Résumé:**
Ce document détaille l'API Web du système, qui sert de point d'entrée principal pour les interactions externes. Il spécifie les endpoints RESTful, les formats de requête et de réponse (JSON), les mécanismes d'authentification et les codes de statut HTTP utilisés.

---
**Fichier:** `docs/composants/base_connaissances_argumentatives.md`
**Résumé:**
Ce document décrit la base de connaissances argumentatives, qui stocke les arguments, leurs relations, les schémas d'argumentation et les taxonomies de sophismes. Il aborde le modèle de données, les mécanismes d'interrogation et de mise à jour, ainsi que son rôle dans l'amélioration continue du système.

---
**Fichier:** `docs/composants/moteur_analyse_structurelle.md`
**Résumé:**
Ce document présente le moteur d'analyse structurelle, responsable de l'identification des composants d'un argument (prémisses, conclusion) et de la reconstruction des relations entre arguments (support, attaque). Il explique les algorithmes d'extraction et de parsing utilisés, ainsi que la représentation interne des structures argumentatives.

---
**Fichier:** `docs/composants/orchestrateur_analyse.md`
**Résumé:**
Ce document décrit l'orchestrateur d'analyse, le composant central qui coordonne les différents agents et modules pour réaliser une analyse argumentative complète. Il détaille la gestion du flux de travail, la distribution des tâches, l'agrégation des résultats et la communication avec l'API Web.

---
**Fichier:** `docs/guides/README.md`
**Résumé:**
Ce README introduit la section des guides et tutoriels du projet. Il indique que cette partie de la documentation vise à aider les utilisateurs et les développeurs à comprendre et à utiliser efficacement le système d'analyse argumentative, en couvrant des sujets allant de l'installation à l'utilisation avancée des fonctionnalités.

---
**Fichier:** `docs/guides/analyse_avancee_sophismes.md`
**Résumé:**
Ce guide avancé explique comment utiliser les fonctionnalités de détection de sophismes de manière approfondie, incluant la configuration de seuils de confiance, l'utilisation de contextes spécifiques pour améliorer la précision, et l'interprétation des résultats détaillés fournis par l'agent d'analyse informelle. Il aborde également la personnalisation de la taxonomie des sophismes.

---
**Fichier:** `docs/guides/contribuer_documentation.md`
**Résumé:**
Ce document fournit des directives pour contribuer à la documentation du projet. Il explique la structure de la documentation, les conventions de formatage (Markdown), le processus de soumission des modifications (Pull Requests) et les bonnes pratiques pour assurer une documentation claire, concise et à jour.

---
**Fichier:** `docs/guides/creation_frameworks_dung.md`
**Résumé:**
Ce guide explique comment créer et analyser des frameworks d'argumentation de Dung à l'aide du système. Il détaille la spécification des arguments et des relations d'attaque, l'appel à l'agent d'analyse formelle, et l'interprétation des différentes sémantiques (fondée, préférée, stable) pour évaluer l'acceptabilité des arguments.

---
**Fichier:** `docs/guides/deploiement_production.md`
**Résumé:**
Ce guide décrit les étapes et les considérations pour déployer le système d'analyse argumentative en environnement de production. Il aborde la configuration matérielle et logicielle requise, les stratégies de scalabilité, la sécurisation de l'API, le monitoring et la maintenance du système.

---
**Fichier:** `docs/guides/demarrage_rapide_developpeurs.md`
**Résumé:**
Ce guide de démarrage rapide est destiné aux développeurs souhaitant contribuer au projet. Il explique comment cloner le dépôt, configurer l'environnement de développement (Python, Java, JPype), installer les dépendances, et lancer les principaux composants du système en mode développement.

---
**Fichier:** `docs/guides/exemples_logique_propositionnelle.md`
**Résumé:**
Ce document fournit des exemples concrets d'utilisation de l'agent de logique propositionnelle. Il illustre comment définir des propositions, construire des formules complexes, créer des bases de croyances et effectuer des requêtes de validation ou d'inférence, avec des explications sur les résultats obtenus.

---
**Fichier:** `docs/guides/guide_utilisation_api_web.md`
**Résumé:**
Ce guide détaille l'utilisation de l'API Web du système d'analyse argumentative. Il présente les différents endpoints, les formats de requête et de réponse, les paramètres disponibles pour chaque type d'analyse (sophismes, structure, validation logique), et fournit des exemples d'appels avec `curl` ou des bibliothèques clientes.

---
**Fichier:** `docs/guides/interpretation_resultats_analyse.md`
**Résumé:**
Ce guide aide à interpréter les résultats fournis par le système d'analyse argumentative. Il explique la signification des différents scores (confiance, force), la structure des rapports d'analyse, et comment comprendre les visualisations des frameworks d'argumentation ou des détections de sophismes.

---
**Fichier:** `docs/guides/utilisation_agents_logiques.md`
**Résumé:**
Ce guide explique comment interagir avec les différents agents logiques (propositionnel, premier ordre, modal) du système. Il détaille la création de bases de croyances, la soumission de requêtes logiques, et l'interprétation des réponses pour chaque type de logique supporté.

---
**Fichier:** `docs/integration/README.md`
**Résumé:**
Ce README introduit la section sur l'intégration et la validation du système d'analyse argumentative. Il précise que cette partie de la documentation couvrira les processus d'intégration continue, les stratégies de test (unitaires, intégration, fonctionnels) et les rapports de validation.

---
**Fichier:** `docs/integration/guide_integration_continue.md`
**Résumé:**
Ce document décrit le pipeline d'intégration continue (CI) mis en place pour le projet, incluant les outils utilisés (ex: Jenkins, GitHub Actions), les étapes de build, les tests automatisés exécutés à chaque commit, et la génération de rapports de qualité du code. Il explique également comment les développeurs peuvent interagir avec le système de CI.

---
**Fichier:** `docs/integration/rapport_validation_fonctionnelle.md`
**Résumé:**
Ce document présente les résultats de la validation fonctionnelle du système, en détaillant les scénarios de test exécutés, les résultats obtenus par rapport aux spécifications, et les éventuels écarts constatés. Il sert à confirmer que le système répond aux besoins fonctionnels exprimés.

---
**Fichier:** `docs/integration/strategie_tests_performance.md`
**Résumé:**
Ce document expose la stratégie adoptée pour les tests de performance du système d'analyse argumentative. Il définit les indicateurs clés de performance (KPIs) tels que la latence, le débit, et l'utilisation des ressources, ainsi que les scénarios de charge et les outils utilisés pour ces tests.

---
**Fichier:** `docs/outils/README.md`
**Résumé:**
Ce README introduit la section de la documentation relative aux outils d'analyse rhétorique et de manipulation de données du projet. Il indique que les documents suivants décriront les fonctionnalités spécifiques de ces outils, leur API et des exemples d'utilisation.

---
**Fichier:** `docs/outils/outil_extraction_entites_argumentatives.md`
**Résumé:**
Ce document décrit l'outil d'extraction d'entités argumentatives, qui identifie les composants clés d'un argument tels que les prémisses, la conclusion, et les indicateurs d'argumentation. Il explique les techniques NLP utilisées (NER, parsing de dépendances) et comment l'outil s'intègre dans le pipeline d'analyse.

---
**Fichier:** `docs/outils/outil_visualisation_graphes_argumentation.md`
**Résumé:**
Ce document présente l'outil de visualisation des graphes d'argumentation, qui permet de représenter graphiquement les frameworks de Dung et les relations entre arguments. Il détaille les formats d'entrée supportés, les options de personnalisation de l'affichage et comment interpréter les visualisations générées.

---
**Fichier:** `docs/projets/README.md`
**Résumé:**
Ce README sert de page d'accueil pour la section des projets étudiants liés à l'Intelligence Symbolique. Il liste les différents sujets de projets proposés, chacun avec un lien vers sa description détaillée, et fournit des informations générales sur les attentes et les ressources disponibles pour les étudiants.

---
**Fichier:** `docs/projets/sujets/1.1.1_Analyse_Structurelle_Arguments_Complexes.md`
**Résumé:**
Ce document décrit un projet étudiant axé sur l'analyse structurelle d'arguments complexes. L'objectif est de développer des méthodes pour identifier les composants (prémisses, conclusions, sous-arguments) et les relations (support, attaque) dans des textes argumentatifs longs et imbriqués, potentiellement en utilisant des techniques de parsing avancé et de machine learning.

---
**Fichier:** `docs/projets/sujets/1.1.2_Classification_Automatique_Types_Arguments.md`
**Résumé:**
Ce sujet de projet concerne la classification automatique des types d'arguments (par exemple, déductif, inductif, abductif, par analogie). Les étudiants devront explorer des approches basées sur le NLP et le machine learning pour entraîner un modèle capable d'identifier la nature du raisonnement employé dans un argument donné.

---
**Fichier:** `docs/projets/sujets/1.1.3_Detection_Relations_Inter_Argumentatives.md`
**Résumé:**
Ce projet vise à développer un système capable de détecter automatiquement les relations entre arguments dans un texte ou un corpus (support, attaque, reformulation). Il implique l'utilisation de techniques de NLP pour analyser les paires d'arguments et classifier leur relation, potentiellement en s'appuyant sur des marqueurs discursifs et la similarité sémantique.

---
**Fichier:** `docs/projets/sujets/1.2.1_Agent_Logique_Propositionnelle_Avance.md`
**Résumé:**
Ce projet étudiant se concentre sur l'extension de l'agent de logique propositionnelle existant. Les objectifs incluent l'implémentation de solveurs SAT plus performants, la gestion de bases de croyances plus larges, et potentiellement l'ajout de fonctionnalités comme l'explication des inférences ou la révision de croyances.

---
**Fichier:** `docs/projets/sujets/1.2.2_Agent_Logique_Premier_Ordre.md`
**Résumé:**
Ce document décrit un projet visant à développer un agent basé sur la logique du premier ordre (FOL). Les tâches comprennent l'intégration d'un raisonneur FOL (ex: Prover9, Vampire), la gestion de la syntaxe FOL, et la capacité à effectuer des inférences et des validations sur des énoncés du premier ordre.

---
**Fichier:** `docs/projets/sujets/1.2.3_Agent_Logique_Modale.md`
**Résumé:**
Ce projet porte sur la création d'un agent capable de raisonner en logique modale (par exemple, K, T, S4, S5). Il implique la sélection et l'intégration d'un solveur de logique modale, la définition d'une syntaxe pour les opérateurs modaux (nécessité, possibilité) et la gestion des modèles de Kripke.

---
**Fichier:** `docs/projets/sujets/1.2.4_Framework_Argumentation_Abstraite_Dung.md`
**Résumé:**
Ce sujet de projet se concentre sur l'implémentation et l'extension des frameworks d'argumentation abstraite de Dung. Les étudiants devront développer des outils pour construire ces frameworks, calculer différentes sémantiques (fondée, préférée, stable, complète) et visualiser les graphes d'argumentation.

---
**Fichier:** `docs/projets/sujets/1.2.5_Extension_Frameworks_Argumentation_Valeurs_Preferences.md`
**Résumé:**
Ce projet vise à étendre les frameworks d'argumentation abstraite pour y intégrer des valeurs et des préférences (par exemple, VAF de Bench-Capon). L'objectif est de permettre une évaluation des arguments qui tienne compte non seulement des relations d'attaque, mais aussi de l'importance relative des valeurs qu'ils promeuvent.

---
**Fichier:** `docs/projets/sujets/1.2.6_Argumentation_Incertaine_Probabiliste.md`
**Résumé:**
Ce projet explore l'argumentation en présence d'incertitude, en utilisant des approches probabilistes. Il s'agit de développer des modèles où les arguments ou les relations d'attaque sont associés à des probabilités, et d'étudier comment calculer l'acceptabilité des arguments dans ce cadre.

---
**Fichier:** `docs/projets/sujets/1.3.1_Analyse_Rhétorique_Discours_Politiques.md`
**Résumé:**
Ce projet se concentre sur l'analyse rhétorique de discours politiques. L'objectif est de développer des outils pour identifier les figures de style, les appels émotionnels (pathos), les arguments d'autorité (ethos) et les stratégies de persuasion utilisées par les orateurs.

---
**Fichier:** `docs/projets/sujets/1.3.2_Detection_Biais_Cognitifs_Textes.md`
**Résumé:**
Ce sujet de projet vise à créer un système capable de détecter les biais cognitifs (biais de confirmation, d'ancrage, etc.) dans des textes argumentatifs. Cela implique de définir une taxonomie de biais, d'identifier des marqueurs linguistiques et d'utiliser potentiellement des techniques de machine learning.

---
**Fichier:** `docs/projets/sujets/1.3.3_Evaluation_Qualite_Argumentation_Persuasive.md`
**Résumé:**
Ce projet porte sur l'évaluation automatique de la qualité de l'argumentation persuasive. Il s'agit de définir des critères de qualité (clarté, pertinence, force des prémisses, absence de sophismes) et de développer un modèle capable d'attribuer un score de qualité à un argument ou à un texte argumentatif.

---
**Fichier:** `docs/projets/sujets/1.4.2_Revision_Croyances_AGM.md`
**Résumé:**
Ce projet se concentre sur l'implémentation des postulats AGM pour la révision de croyances. Les étudiants devront développer un système capable d'effectuer des opérations de contraction, d'expansion et de révision sur une base de croyances propositionnelles, en respectant les principes de rationalité définis par Alchourrón, Gärdenfors et Makinson.

---
**Fichier:** `docs/projets/sujets/1.4.3_Fusion_Bases_Connaissances_Heterogenes.md`
**Résumé:**
Ce projet aborde le problème de la fusion de bases de connaissances hétérogènes, potentiellement conflictuelles. L'objectif est de développer des opérateurs de fusion qui permettent de combiner des informations provenant de sources multiples tout en gérant les incohérences et en préservant autant d'informations pertinentes que possible.

---
**Fichier:** `docs/projets/sujets/2.1.1_Interface_Web_Analyse_Argumentative.md`
**Résumé:**
Ce projet concerne le développement d'une interface web pour le système d'analyse argumentative. L'interface devra permettre aux utilisateurs de soumettre du texte, de visualiser les résultats de l'analyse (structure, sophismes, validation logique) de manière interactive et conviviale, et potentiellement de configurer les paramètres d'analyse.

---
**Fichier:** `docs/projets/sujets/2.1.2_Plugin_Navigateur_Analyse_Temps_Reel.md`
**Résumé:**
Ce projet vise à créer un plugin de navigateur (extension) capable d'analyser le contenu textuel des pages web en temps réel. Le plugin devrait pouvoir identifier les arguments, détecter les sophismes et afficher des annotations directement sur la page consultée par l'utilisateur.

---
**Fichier:** `docs/projets/sujets/2.1.3_Visualisation_Interactive_Frameworks_Argumentation.md`
**Résumé:**
Ce projet se concentre sur la création d'outils de visualisation interactive pour les frameworks d'argumentation. L'objectif est de permettre aux utilisateurs d'explorer dynamiquement les graphes d'argumentation, de manipuler les relations d'attaque, et de voir l'impact des changements sur les extensions et l'acceptabilité des arguments.

---
**Fichier:** `docs/projets/sujets/2.1.4_Integration_Systeme_Annotation_Collaborative.md`
**Résumé:**
Ce projet porte sur l'intégration d'un système d'annotation collaborative pour les arguments et les sophismes. Il s'agit de permettre à plusieurs utilisateurs d'annoter des textes, de valider les annotations des autres, et de contribuer à la création d'un corpus d'entraînement pour les modèles d'IA.

---
**Fichier:** `docs/projets/sujets/2.1.5_Developpement_API_Web_Avancee.md`
**Résumé:**
Ce projet vise à étendre l'API Web existante du système d'analyse argumentative. Les améliorations pourraient inclure de nouveaux endpoints pour des analyses plus fines, la gestion de requêtes asynchrones pour les analyses longues, une meilleure gestion de l'authentification et des permissions, ainsi qu'une documentation API interactive (Swagger/OpenAPI).

---
**Fichier:** `docs/projets/sujets/2.2.1_Optimisation_Performance_Moteur_Analyse.md`
**Résumé:**
Ce projet se concentre sur l'optimisation des performances du moteur d'analyse argumentative. Les tâches peuvent inclure le profilage du code, l'amélioration des algorithmes, la mise en cache des résultats, la parallélisation des traitements et la réduction de la consommation mémoire.

---
**Fichier:** `docs/projets/sujets/2.2.2_Scalabilite_Systeme_Distribué.md`
**Résumé:**
Ce projet aborde la scalabilité du système en envisageant une architecture distribuée. Il s'agit d'étudier comment répartir les différents composants (agents d'analyse, bases de connaissances) sur plusieurs nœuds pour gérer un volume important de requêtes et de données, en utilisant des technologies comme Docker, Kubernetes ou des systèmes de messagerie.

---
**Fichier:** `docs/projets/sujets/2.2.3_Integration_Base_Donnees_Graphe_Neo4j.md`
**Résumé:**
Ce projet explore l'intégration d'une base de données graphe comme Neo4j pour stocker et interroger les structures argumentatives. L'objectif est de bénéficier des capacités des bases de données graphe pour représenter nativement les relations entre arguments et faciliter des requêtes complexes sur ces structures.

---
**Fichier:** `docs/projets/sujets/2.2.4_Systeme_Monitoring_Logging_Avance.md`
**Résumé:**
Ce projet vise à développer un système de monitoring et de logging avancé pour le moteur d'analyse. Il s'agit de collecter des métriques de performance, de journaliser les événements importants, de détecter les anomalies et de fournir des tableaux de bord pour superviser l'état et le comportement du système en temps réel.

---
**Fichier:** `docs/projets/sujets/2.3.1_Agent_Explication_Raisonnements_Logiques.md`
**Résumé:**
Ce projet se concentre sur le développement d'un agent capable d'expliquer les raisonnements logiques effectués par le système. Pour une inférence donnée, l'agent devrait pouvoir générer une explication en langage naturel des étapes de déduction, des règles appliquées et des justifications pour la conclusion.

---
**Fichier:** `docs/projets/sujets/2.3.4_Agent_Ethique_Evaluation_Arguments_Sensibles.md`
**Résumé:**
Ce projet porte sur la création d'un agent éthique capable d'évaluer des arguments sur des sujets sensibles. Il doit identifier les implications éthiques, détecter les discours haineux ou discriminatoires, et potentiellement proposer des reformulations plus neutres ou respectueuses, tout en signalant les arguments problématiques.

---
**Fichier:** `docs/projets/sujets/2.3.5_Apprentissage_Renforcement_Strategies_Argumentatives.md`
**Résumé:**
Ce projet explore l'utilisation de l'apprentissage par renforcement pour développer des stratégies argumentatives optimales pour un agent. L'agent apprendrait à sélectionner les meilleurs arguments ou contre-arguments dans un débat en fonction de l'état du dialogue et des réactions de l'interlocuteur, afin de maximiser ses chances d'atteindre son objectif (persuasion, négociation).

---
**Fichier:** `docs/projets/sujets/2.4.2_Analyse_Evolution_Debats_Temporels.md`
**Résumé:**
Ce projet vise à analyser l'évolution des débats au fil du temps en utilisant l'index sémantique. Il s'agit de suivre comment les arguments émergent, gagnent ou perdent en popularité, se transforment, et comment les positions des participants évoluent dans des discussions qui s'étalent sur de longues périodes.

---
**Fichier:** `docs/projets/sujets/2.4.3_Comparaison_Automatique_Positions_Argumentatives.md`
**Résumé:**
Ce projet se concentre sur la comparaison automatique de positions argumentatives. À partir de deux ou plusieurs ensembles d'arguments représentant des positions différentes, le système devrait identifier les points d'accord, de désaccord, les contradictions et les arguments clés qui distinguent chaque position.

---
**Fichier:** `docs/projets/sujets/2.5.1_Evaluation_Comparative_Frameworks_Argumentation.md`
**Résumé:**
Ce projet propose une évaluation comparative de différents frameworks d'argumentation (Dung, ASPIC+, DeLP, etc.) sur un ensemble de cas d'usage. L'objectif est d'analyser leurs forces et faiblesses respectives en termes d'expressivité, de complexité computationnelle et de pertinence pour modéliser différents types de raisonnements.

---
**Fichier:** `docs/projets/sujets/2.5.2_Developpement_Langage_Domaine_Specifique_DSL_Argumentation.md`
**Résumé:**
Ce projet vise à développer un Langage Spécifique au Domaine (DSL) pour l'argumentation. Ce DSL permettrait de décrire des arguments, des relations et des schémas argumentatifs de manière concise et formelle, facilitant ainsi la création et la manipulation de modèles argumentatifs par les utilisateurs.

---
**Fichier:** `docs/projets/sujets/README.md`
**Résumé:**
Ce README est la page d'accueil de la section des sujets de projets pour le cours d'Intelligence Symbolique. Il introduit les différentes catégories de projets (Analyse d'Arguments, Logiques Formelles, Interfaces et Systèmes, Applications Avancées) et fournit des liens vers les descriptions détaillées de chaque sujet.

---
**Fichier:** `docs/projets/sujets/aide/CONTRIBUTING.md`
**Résumé:**
Ce document détaille les directives de contribution pour le dossier d'aide des projets étudiants. Il explique comment proposer de nouvelles ressources, la structure attendue, les standards de qualité pour le code et la documentation, ainsi que le processus de soumission via Pull Requests.

---
**Fichier:** `docs/projets/sujets/aide/GLOSSAIRE.md`
**Résumé:**
Ce glossaire définit les termes techniques et concepts clés utilisés dans les projets d'Intelligence Symbolique et d'analyse argumentative. Il vise à fournir une référence commune pour les étudiants afin d'assurer une compréhension uniforme du vocabulaire spécifique au domaine.

---
**Fichier:** `docs/projets/sujets/aide/LICENSE.md`
**Résumé:**
Ce fichier contient les informations de licence pour les ressources et le code fournis dans le dossier d'aide des projets étudiants. Il spécifie les conditions d'utilisation, de modification et de distribution du matériel pédagogique mis à disposition.

---
**Fichier:** `docs/projets/sujets/aide/PRESENTATION_KICKOFF.md`
**Résumé:**
Ce document est une présentation de lancement pour les projets Epita 2025 en Intelligence Symbolique. Il introduit le projet global d'analyse argumentative, son architecture système (Interface Web, API Web, Moteur d'analyse, TweetyProject, Serveur MCP), et détaille les objectifs spécifiques, technologies et planning pour les sous-projets Interface Web et Serveur MCP, tout en listant les ressources disponibles.

---
**Fichier:** `docs/projets/sujets/aide/README.md`
**Résumé:**
Ce README décrit l'objectif et l'organisation du dossier d'aide, qui vise à fournir des ressources pratiques spécialisées (code, exemples, solutions) pour chaque sujet de projet afin d'accélérer le développement. Il détaille la structure type des ressources par sujet, liste les ressources disponibles pour l'Interface Web d'Analyse Argumentative (démarrage rapide, guide API, troubleshooting, composants React) et explique comment utiliser et contribuer à ces ressources.

---
**Fichier:** `docs/projets/sujets/1.2.7_Argumentation_Dialogique.md`
**Résumé:**
Ce document guide le développement d'un système d'argumentation dialogique, couvrant les fondements théoriques (types de dialogues de Walton-Krabbe, protocoles), la modélisation formelle, l'implémentation computationnelle (architectures d'agents, moteur de dialogue) et l'intégration avec TweetyProject via `jpype` pour Python. Il inclut des exemples pratiques, des métriques d'évaluation et des applications potentielles.

---
**Fichier:** `docs/projets/sujets/1.4.1_Systemes_Maintenance_Verite_TMS.md`
**Résumé:**
Ce document décrit le projet de développement d'agents JTMS (Justification-based) et ATMS (Assumption-based) pour les Systèmes de Maintenance de la Vérité, en utilisant Python et `jpype` pour s'interfacer avec les fonctionnalités de révision de croyances de TweetyProject. Il aborde les fondements théoriques (raisonnement non-monotone, postulats AGM), les architectures TMS classiques, les algorithmes et l'intégration avec TweetyProject.

---
**Fichier:** `docs/projets/sujets/2.1.6_Gouvernance_Multi_Agents.md`
**Résumé:**
Ce document porte sur la gouvernance multi-agents, explorant les mécanismes de décision collective et de coordination. Il couvre les fondements théoriques (choix social, jeux coopératifs), les architectures d'agents (BDI, réactive), les protocoles de coordination (FIPA-ACL étendus), les mécanismes de consensus (Byzantin, Raft, vote quadratique) et l'intégration avec TweetyProject pour la validation argumentative des décisions.

---
**Fichier:** `docs/projets/sujets/2.3.2_Agent_Detection_Sophismes_Biais_Cognitifs.md`
**Résumé:**
Ce guide détaille la création d'un agent de détection de sophismes et biais cognitifs, incluant une taxonomie, l'utilisation de techniques NLP avancées (Spacy, Transformers), des modèles d'apprentissage automatique pour la classification, et un pipeline de détection intégré. Il aborde également la validation des détections via TweetyProject et l'implémentation temps réel.

---
**Fichier:** `docs/projets/sujets/2.3.3_Agent_Generation_Contre_Arguments.md`
**Résumé:**
Ce document guide le développement d'un agent capable de générer des contre-arguments. Il explore les théories de la contre-argumentation, les architectures de génération automatique (utilisant des Transformers et des LLMs), les stratégies rhétoriques, l'intégration avec TweetyProject pour la validation logique et les métriques d'évaluation de la qualité des contre-arguments générés.

---
**Fichier:** `docs/projets/sujets/2.3.6_Integration_LLMs_locaux_legers.md`
**Résumé:**
Ce guide pédagogique complet porte sur l'intégration de LLMs locaux légers (0.6B à 32B paramètres) pour l'analyse argumentative, en mettant l'accent sur l'utilisation d'Ollama et `llama.cpp`. Il couvre les aspects techniques (distillation, quantification, pruning), les frameworks, l'intégration pratique avec Semantic Kernel et LangChain, l'évaluation comparative de modèles (Qwen, Phi, Mistral) et les tests de performance, y compris avec `semantic-fleet`.

---
**Fichier:** `docs/projets/sujets/2.4.1_Index_Semantique_Arguments.md`
**Résumé:**
Ce document décrit la création d'un index sémantique d'arguments, en se concentrant sur l'utilisation de la bibliothèque `kernel-memory` de Microsoft. Il aborde les fondements théoriques (embeddings, bases vectorielles comme Chroma, Pinecone, Weaviate), l'architecture du système (pipeline d'indexation, moteur de recherche), l'intégration avec TweetyProject et des cas d'usage avancés comme la détection de contradictions et la recommandation d'arguments.

---
**Fichier:** `docs/projets/sujets/2.5.3_Developpement_Serveur_MCP_Analyse_Argumentative.md`
**Résumé:**
Ce document guide le développement d'un serveur MCP (Model Context Protocol) pour l'analyse argumentative, destiné à exposer les fonctionnalités du système (détection de sophismes, frameworks de Dung, validation logique) à des clients comme Claude ou Roo. Il détaille les spécifications techniques du protocole JSON-RPC 2.0, la structure des outils et ressources, la gestion des sessions, et l'intégration avec TweetyProject via `jpype`.

---
**Fichier:** `docs/README.md`
**Résumé:**
Ce README principal de la documentation du projet Intelligence Symbolique introduit la structure globale de la documentation, organisée en sections thématiques (Architecture, Composants, Guides, Intégration, Outils, Projets, Référence API, Images). Il liste également les documents principaux et fournit des conseils pour commencer et contribuer à la documentation.

---
**Fichier:** `docs/troubleshooting.md`
**Résumé:**
Ce guide de dépannage fournit des solutions aux problèmes courants rencontrés lors de l'utilisation du système d'analyse argumentative, classés par catégories (installation, exécution, API, analyse, visualisation). Il référence également des scripts de diagnostic et des tests pour aider à identifier et résoudre les erreurs.

---
**Fichier:** `examples/README.md`
**Résumé:**
Ce README guide l'utilisateur à travers le répertoire `examples/`, qui contient des scripts Python, des notebooks Jupyter et des fichiers textes illustrant l'utilisation des fonctionnalités du projet d'analyse argumentative. Il détaille la structure du répertoire, explique comment exécuter les exemples et fournit un guide pour contribuer en ajoutant de nouveaux exemples de textes.

---
**Fichier:** `docs/analysis/comparaison_sophismes.md`
**Résumé:**
Ce document compare les sophismes identifiés par un agent avec une documentation de référence, évaluant la précision de détection et de classification de l'agent. Il analyse la performance de l'agent, ses points forts, et les aspects à améliorer concernant l'identification des sophismes.

---
**Fichier:** `docs/analysis/conclusion_test_agent_informel.md`
**Résumé:**
Ce document conclut le test d'un agent informel sur sa capacité à identifier et analyser des sophismes complexes en explorant une taxonomie. Il résume la performance de l'agent, ses points forts et faibles, et propose des recommandations pour son amélioration future.

---
**Fichier:** `docs/analysis/README.md`
**Résumé:**
Ce fichier README présente le contenu du répertoire `docs/analysis`, qui héberge des analyses détaillées du projet, telles que des comparaisons de sophismes et des résultats de tests d'agents. Il décrit la structure, la méthodologie et l'objectif de ces analyses.

---
**Fichier:** `docs/analysis/synthese_test_agent_informel.md`
**Résumé:**
Ce document synthétise les résultats d'un test sur l'exploration progressive d'une taxonomie de sophismes par un agent informel. Il détaille la méthodologie, les performances de l'agent à chaque étape d'analyse, et identifie ses forces et faiblesses.

---

---
**Fichier:** `argumentation_analysis/agents/core/logic/README.md`
**Résumé:**
Ce module détaille les agents capables de raisonnement logique formel (propositionnel, premier ordre, modal) en s'appuyant sur `TweetyProject`. Il décrit la hiérarchie des agents, les composants clés comme `BeliefSet`, `TweetyBridge` (pour l'interaction Java/Python), `LogicAgentFactory` et `QueryExecutor`, ainsi que le flux de travail typique d'un agent logique.

---
**Fichier:** `argumentation_analysis/agents/core/pm/README.md`
**Résumé:**
Ce document décrit le `ProjectManagerAgent`, responsable de la planification stratégique et de la définition des tâches dans l'analyse d'argumentation, sans gérer directement leur exécution. Il opère en analysant l'état actuel, en définissant les tâches via des fonctions sémantiques (comme `DefineTasksAndDelegate`) et en rédigeant la conclusion finale (via `WriteAndSetConclusion`), fournissant des instructions à un orchestrateur.

---
**Fichier:** `argumentation_analysis/orchestration/README.md`
**Résumé:**
Ce document explique le mécanisme d'orchestration simple basé sur `AgentGroupChat` de Semantic Kernel, utilisé dans `analysis_runner.py`. Il détaille comment plusieurs agents collaborent via un état partagé (`RhetoricalAnalysisState`) et des stratégies de sélection (`BalancedParticipationStrategy`) et de terminaison (`SimpleTerminationStrategy`) pour analyser un texte.
**Fichier:** `docs/api/logic_endpoints.md`
**Résumé:**
Ce document détaille les endpoints de l'API REST pour les opérations logiques, incluant la conversion de texte en croyances, l'exécution et la génération de requêtes logiques, ainsi que l'interprétation des résultats. Il couvre les logiques propositionnelle, du premier ordre et modale.

---
**Fichier:** `docs/architecture/images/architecture_communication.md`
**Résumé:**
Ce fichier présente un diagramme Mermaid décrivant une architecture de communication hiérarchique. Il illustre les interactions entre les niveaux stratégique, tactique et opérationnel via des interfaces dédiées.

---
**Fichier:** `docs/architecture/images/architecture_multi_canal.md`
**Résumé:**
Ce document contient un diagramme Mermaid qui représente une architecture de communication multi-canal. Il détaille les interactions entre un middleware, divers canaux de communication spécialisés, et les différents niveaux hiérarchiques d'agents via des adaptateurs.

---
**Fichier:** `docs/architecture/analyse_architecture_orchestration.md`
**Résumé:**
Ce document analyse l'architecture d'orchestration actuelle du système d'analyse rhétorique, ses composants principaux comme l'état partagé et les stratégies d'orchestration. Il identifie les limitations de l'approche actuelle et suggère des améliorations en vue d'une architecture hiérarchique à trois niveaux.

---
**Fichier:** `docs/architecture/architecture_globale.md`
**Résumé:**
Ce document présente une vue d'ensemble de l'architecture globale du système d'analyse argumentative. Il détaille les composants majeurs tels que l'orchestration, les agents spécialisés, l'état partagé, et les services externes, ainsi que leurs interactions et le flux de données typique.

---
**Fichier:** `docs/architecture/architecture_hierarchique.md`
**Résumé:**
Ce document expose une architecture hiérarchique à trois niveaux (stratégique, tactique, opérationnel) pour le système d'analyse rhétorique. Il détaille les responsabilités, les agents, la gestion de l'état pour chaque niveau, ainsi que les mécanismes de communication et les flux d'information inter-niveaux.

---
**Fichier:** `docs/architecture/conception_multi_canal.md`
**Résumé:**
Ce document décrit la conception d'un système de communication multi-canal, incluant un middleware de messagerie et des canaux spécialisés. Il aborde les protocoles de communication, les structures de messages, les mécanismes de routage et la gestion des erreurs pour les interactions entre agents.

---
**Fichier:** `docs/architecture/current_state_analysis.md`
**Résumé:**
Ce rapport analyse la structure actuelle du projet, identifiant l'organisation du code, des scripts, des tests, et de la configuration. Il met en évidence les incohérences structurelles, les duplications et les problèmes potentiels liés à la dispersion des fichiers.

---
**Fichier:** `docs/architecture/etat_avancement.md`
**Résumé:**
Ce document fait le point sur l'état d'avancement de l'implémentation de l'architecture hiérarchique. Il liste les composants déjà réalisés, ceux en cours de développement, et les prochaines étapes prévues.

---
**Fichier:** `docs/architecture/rapport_analyse_architecture.md`
**Résumé:**
Ce rapport analyse l'architecture du projet "argumentiation_analysis", identifiant des problèmes structurels, d'importation et de documentation. Il formule des recommandations pour résoudre ces problèmes avant un déploiement étudiant.

---
**Fichier:** `docs/architecture/reorganization_proposal.md`
**Résumé:**
Ce document propose une nouvelle structure pour le projet afin d'améliorer sa cohérence et sa maintenabilité. Il détaille l'arborescence cible, les justifications des changements, un plan de migration et une liste d'opérations de réorganisation.

---
**Fichier:** `docs/cleaning_reports/final_cleanup_summary_report.md`
**Résumé:**
Ce document est un rapport de synthèse final pour le Lot 7 du nettoyage des tests. Il résume les principales réalisations, telles que la suppression de tests obsolètes et la standardisation de la structure, ainsi que les bénéfices attendus.

---
**Fichier:** `docs/cleaning_reports/lot1_analysis_plan.md`
**Résumé:**
Ce document présente le plan d'analyse et les actions proposées pour le Lot 1 du nettoyage des tests. Il cible des fichiers spécifiques à la racine du répertoire de tests pour améliorer leur organisation et documentation.

---
**Fichier:** `docs/cleaning_reports/lot1_completion_report.md`
**Résumé:**
Ce rapport détaille les actions de nettoyage et de réorganisation effectuées sur les fichiers de test du Lot 1. Il indique pour chaque fichier les modifications apportées, telles que suppression ou refactorisation, et les commits correspondants.

---
**Fichier:** `docs/cleaning_reports/lot2_analysis_plan.md`
**Résumé:**
Ce document établit le plan d'analyse et de nettoyage pour le Lot 2 des tests. Il se concentre sur l'organisation, la documentation et l'extraction de composants réutilisables pour les tests des agents informels et d'autres fichiers de test.

---
**Fichier:** `docs/cleaning_reports/lot2_completion_report.md`
**Résumé:**
Ce rapport résume les actions de nettoyage et de valorisation des tests effectuées pour le Lot 2. Il décrit les déplacements de fichiers, les refactorisations, la création de fixtures et les mises à jour de documentation.

---
**Fichier:** `docs/cleaning_reports/lot3_analysis_plan.md`
**Résumé:**
Ce document présente le plan d'analyse et de nettoyage pour le Lot 3 des tests. Il cible des tests d'environnement, d'orchestration tactique et de logique des agents, en vue d'améliorer leur organisation et documentation.

---
**Fichier:** `docs/cleaning_reports/lot3_completion_report.md`
**Résumé:**
Ce rapport détaille les actions de nettoyage et de réorganisation effectuées pour le Lot 3 des tests. Il inclut les déplacements de fichiers, les mises à jour de documentation, et note un problème Git ayant affecté les commits.

---
**Fichier:** `docs/cleaning_reports/lot4_analysis_plan.md`
**Résumé:**
Ce document établit le plan d'analyse et de nettoyage pour le Lot 4 des tests. Il se focalise sur les tests de logique des agents et des outils d'analyse rhétorique, visant à améliorer leur organisation et documentation.

---
**Fichier:** `docs/cleaning_reports/lot4_completion_report.md`
**Résumé:**
Ce rapport résume les actions de nettoyage et de valorisation des tests pour le Lot 4. Il inclut les mises à jour de documentation, l'identification de fichiers de test manquants ou mal placés, et des propositions de refactorisation.

---
**Fichier:** `docs/cleaning_reports/lot5_analysis_plan.md`
**Résumé:**
Ce document présente le plan d'analyse et de nettoyage pour le Lot 5 des tests. Il se concentre sur les tests des outils d'analyse des agents, ainsi que sur les tests fonctionnels et d'orchestration.

---
**Fichier:** `docs/cleaning_reports/lot5_completion_report.md`
**Résumé:**
Ce rapport détaille les actions de nettoyage et de valorisation des tests effectuées pour le Lot 5. Il comprend les mises à jour de documentation, l'identification de fichiers de test manquants et des propositions de refactorisation.

---
**Fichier:** `docs/cleaning_reports/lot6_analysis_plan.md`
**Résumé:**
Ce document établit le plan d'analyse et de nettoyage pour le Lot 6 des tests. Il se focalise sur la finalisation de la réorganisation des tests d'intégration, l'exploration des tests d'orchestration et l'analyse des tests de scripts et d'interface utilisateur.

---
**Fichier:** `docs/cleaning_reports/lot6_completion_report.md`
**Résumé:**
Ce rapport résume les actions de nettoyage et de valorisation des tests pour le Lot 6. Il inclut la suppression de fichiers obsolètes, des renommages, des refactorisations et des mises à jour de documentation.

---
**Fichier:** `docs/cleaning_reports/lot7_analysis_plan.md`
**Résumé:**
Ce document présente le plan d'analyse final (Lot 7) pour le nettoyage des tests. Il vise à réorganiser les tests restants, supprimer les fichiers obsolètes et extraire des tests unitaires pertinents.

---
**Fichier:** `docs/cleaning_reports/lot7_completion_report.md`
**Résumé:**
Ce rapport détaille les actions finales de nettoyage et de réorganisation de la structure des tests (Lot 7). Il inclut la suppression de fichiers, le déplacement de tests, la création de tests unitaires et les mises à jour de documentation.

---
**Fichier:** `docs/composants/agents_specialistes.md`
**Résumé:**
Ce document décrit les différents agents spécialistes du système d'analyse rhétorique, leurs rôles et responsabilités. Il aborde également l'architecture multi-agents, la communication, l'orchestration et l'extensibilité du système.

---
**Fichier:** `docs/composants/structure_projet.md`
**Résumé:**
Ce document détaille la structure globale du projet et de ses composants principaux, incluant les modules applicatifs, les tests et la gestion des données. Il explique également le flux de données, les interfaces entre composants et les possibilités d'extension.

---
**Fichier:** `docs/composants/synthese_collaboration.md`
**Résumé:**
Ce document analyse les mécanismes de collaboration entre les agents d'analyse rhétorique. Il identifie les points forts et faibles du système actuel et propose des recommandations pour améliorer l'interaction et l'orchestration des agents.

---
**Fichier:** `docs/diagrams/flux_donnees.md`
**Résumé:**
Ce fichier présente un diagramme Mermaid qui illustre le flux de données au sein du système d'analyse argumentative. Il montre le parcours des données depuis l'entrée du texte jusqu'à la génération des résultats.

---
**Fichier:** `docs/diagrams/interactions_composants.md`
**Résumé:**
Ce document contient un diagramme Mermaid qui représente les interactions entre les différents composants du système. Il met en évidence l'architecture hiérarchique et les services partagés.

---
**Fichier:** `docs/diagrams/README.md`
**Résumé:**
Ce fichier README décrit le contenu du répertoire `docs/diagrams`. Il liste les diagrammes disponibles et fournit des instructions pour leur visualisation et leur contribution.

---
**Fichier:** `docs/environnement/environnement_agent3_actuel.md`
**Résumé:**
Ce document spécifie la configuration de l'environnement de l'Agent 3. Il liste les versions logicielles, les variables d'environnement et les packages Python installés.

---
**Fichier:** `docs/guides/conventions_importation.md`
**Résumé:**
Ce document explique les conventions d'importation de modules Python et les mécanismes de redirection utilisés dans le projet. Il fournit des bonnes pratiques et des exemples pour assurer la cohérence du code.

---
**Fichier:** `docs/guides/exemples_logique_modale.md`
**Résumé:**
Ce guide présente des exemples d'utilisation de la logique modale, illustrant sa syntaxe et son application à divers types de raisonnements. Il couvre des cas basiques, intermédiaires et avancés, y compris des paradoxes et des cas d'utilisation réels.

---
**Fichier:** `docs/guides/exemples_logique_premier_ordre.md`
**Résumé:**
Ce guide offre des exemples d'application de la logique du premier ordre, détaillant sa syntaxe et son utilisation pour formaliser divers arguments. Il inclut des exemples de base, intermédiaires, avancés et des cas d'utilisation concrets.

---
**Fichier:** `docs/guides/guide_developpeur.md`
**Résumé:**
Ce guide s'adresse aux développeurs et explique comment étendre le système de communication multi-canal. Il couvre l'architecture détaillée, l'ajout de nouveaux composants (canaux, protocoles, adaptateurs) et les bonnes pratiques de développement.

---
**Fichier:** `docs/guides/guide_utilisation.md`
**Résumé:**
Ce guide explique comment utiliser le projet, de la configuration de l'environnement à l'exécution des exemples et des tests. Il couvre l'utilisation des scripts de démonstration, des notebooks et des données de test fournies.

---
**Fichier:** `docs/guides/integration_api_web.md`
**Résumé:**
Ce document guide les développeurs pour l'intégration avec l'API Web du système, permettant d'utiliser les agents logiques à distance. Il détaille les endpoints, fournit des exemples d'utilisation dans plusieurs langages et aborde la gestion des erreurs.

---
**Fichier:** `docs/images/architecture_communication_agents.md`
**Résumé:**
Ce fichier présente un diagramme Mermaid décrivant l'architecture de communication entre les agents. Il illustre les interactions entre les niveaux stratégique, tactique et opérationnel.

---
**Fichier:** `docs/images/architecture_multi_canal_proposee.md`
**Résumé:**
Ce document contient un diagramme Mermaid qui représente une proposition d'architecture de communication multi-canal. Il détaille les interactions entre un middleware, divers canaux de communication et les niveaux hiérarchiques d'agents.

---
**Fichier:** `docs/images/README.md`
**Résumé:**
Ce fichier README décrit le contenu du répertoire `docs/images`. Il liste les diagrammes d'architecture disponibles et fournit des instructions pour leur visualisation et leur contribution.

---
**Fichier:** `docs/integration/integration_complete.md`
**Résumé:**
Ce document est un rapport de clôture pour un projet d'intégration. Il résume le processus, les fonctionnalités intégrées (communication multi-canal, orchestration hiérarchique), et fournit des recommandations pour les développeurs ainsi que les prochaines étapes.

---
**Fichier:** `docs/integration/liste_verification_deploiement.md`
**Résumé:**
Ce document fournit une liste de vérification exhaustive pour le déploiement du projet. Il couvre tous les aspects, de la structure du projet et des tests à la documentation et la sécurité.

---
**Fichier:** `docs/integration/plan_integration.md`
**Résumé:**
Ce document détaille un plan pour l'intégration de modifications locales dans la branche principale du projet. Il inclut un résumé de l'état actuel, un plan d'action par étapes et des recommandations pour la gestion des conflits.

---
**Fichier:** `docs/integration/pull_request_summary.md`
**Résumé:**
Ce document est un résumé destiné à une Pull Request, décrivant les modifications apportées, les problèmes résolus et l'impact potentiel. Il couvre l'intégration de nouveaux outils d'analyse, d'un système de communication et d'une architecture hiérarchique.

---
**Fichier:** `docs/integration/README_cleanup_obsolete_files.md`
**Résumé:**
Ce README documente un script Python conçu pour nettoyer les fichiers obsolètes du projet. Il explique son utilisation, les options disponibles, et les mécanismes de sécurité pour la suppression et l'archivage des fichiers.

---
**Fichier:** `docs/integration/validation_integration.md`
**Résumé:**
Ce document présente une checklist et les résultats de la validation d'une intégration de modifications. Il couvre les tests unitaires, d'intégration et de performance, et fournit des recommandations pour l'utilisation des nouvelles fonctionnalités.

---
**Fichier:** `docs/integration/validation_systeme_communication.md`
**Résumé:**
Ce rapport détaille la validation du système de communication multi-canal. Il couvre les tests fonctionnels, de performance et de conformité, et conclut sur la robustesse du système tout en proposant des améliorations.

---
**Fichier:** `docs/outils/reference/argument_coherence_evaluator.md`
**Résumé:**
Ce document décrit l'outil `ArgumentCoherenceEvaluator`, son objectif d'évaluation de la cohérence logique des arguments, son utilisation en Python, ses paramètres et les résultats qu'il produit.

---
**Fichier:** `docs/outils/reference/coherence_evaluator.md`
**Résumé:**
Ce document présente l'outil `CoherenceEvaluator`, conçu pour évaluer la cohérence entre les arguments d'un texte. Il détaille son utilisation, ses paramètres, les résultats fournis (incluant un diagramme de flux sémantique) et comment l'étendre.

---
**Fichier:** `docs/outils/reference/complex_fallacy_analyzer.md`
**Résumé:**
Ce document décrit l'outil `EnhancedComplexFallacyAnalyzer`, qui analyse les structures argumentatives complexes pour y déceler des sophismes imbriqués. Il explique son utilisation, ses paramètres, les résultats (y compris un arbre de dépendances) et son extensibilité.

---
**Fichier:** `docs/outils/reference/contextual_fallacy_detector_advanced.md`
**Résumé:**
Ce document détaille les fonctionnalités avancées du `ContextualFallacyDetector`. Il explique comment cet outil analyse les facteurs contextuels pour identifier des sophismes subtils et évaluer l'adéquation des arguments.

---
**Fichier:** `docs/outils/reference/contextual_fallacy_detector.md`
**Résumé:**
Ce document présente l'outil `ContextualFallacyDetector`, qui identifie les erreurs rhétoriques en analysant les relations sémantiques entre arguments. Il détaille son utilisation, ses paramètres, les résultats (y compris une carte contextuelle) et son extensibilité.

---
**Fichier:** `docs/outils/reference/documentation_sophismes.md`
**Résumé:**
Ce document sert de référence pour l'évaluation d'un agent d'identification de sophismes. Il liste et explique les sophismes présents dans un texte d'exemple, en les classant par type et en indiquant le processus d'exploration attendu.

---
**Fichier:** `docs/outils/reference/enhanced_complex_fallacy_analyzer.md`
**Résumé:**
Ce document décrit l'outil `EnhancedComplexFallacyAnalyzer`, conçu pour analyser des structures argumentatives complexes et y détecter des sophismes imbriqués et des contradictions. Il explique son utilisation, ses paramètres, les résultats (y compris une visualisation) et comment le personnaliser.

---
**Fichier:** `docs/outils/reference/semantic_argument_analyzer.md`
**Résumé:**
Décrit l'Analyseur Sémantique d'Arguments, un outil qui implémente le modèle de Toulmin pour analyser la structure sémantique des arguments. Il identifie les composants tels que les revendications, données, garanties, fondements, réfutations et qualificateurs.

---
**Fichier:** `docs/outils/reference/visualizer.md`
**Résumé:**
Présente le Visualiseur de Résultats Rhétoriques, un outil conçu pour générer des représentations graphiques des analyses argumentatives. Il supporte différents styles comme Mermaid et permet de personnaliser le niveau de détail et le thème.

---
**Fichier:** `docs/outils/api_outils.md`
**Résumé:**
Détaille la référence API pour les outils d'analyse rhétorique, présentant une architecture modulaire en couches (Stratégique, Tactique, Opérationnel). Le document décrit les modules principaux, les améliorations techniques et fournit un exemple d'utilisation de l'API.

---
**Fichier:** `docs/outils/argument_coherence_evaluator.md`
**Résumé:**
Décrit l'Évaluateur de cohérence argumentative, un outil qui évalue la cohérence logique des arguments dans un texte. Il vérifie l'alignement entre les prémisses et la conclusion, et peut fournir des explications détaillées sur les incohérences.

---
**Fichier:** `docs/outils/coherence_evaluator.md`
**Résumé:**
Présente l'Évaluateur de Cohérence Argumentative, un outil qui évalue la cohérence logique entre les arguments d'un texte. Il identifie les ruptures de chaînage sémantique et peut générer des diagrammes de flux sémantique.

---
**Fichier:** `docs/outils/complex_fallacy_analyzer.md`
**Résumé:**
Décrit l'Analyseur de Sophismes Complexes, un outil qui analyse les structures argumentatives complexes pour identifier les erreurs logiques imbriquées. Il peut générer un arbre des dépendances logiques et suggérer des simplifications.

---
**Fichier:** `docs/outils/contextual_fallacy_detector.md`
**Résumé:**
Présente le Détecteur de Sophismes Contextuels, un outil qui identifie les erreurs rhétoriques en analysant les relations sémantiques entre les arguments. Il fournit une liste des sophismes avec leur type, position, gravité et des suggestions de reformulation.

---
**Fichier:** `docs/outils/developpement_outils.md`
**Résumé:**
Fournit un guide pour le développement et l'extension des outils rhétoriques au sein du projet. Il explique comment ajouter de nouveaux critères de cohérence, types de sophismes, ou créer de nouveaux outils, en suivant les bonnes pratiques et le workflow de développement.

---
**Fichier:** `docs/outils/enhanced_complex_fallacy_analyzer.md`
**Résumé:**
Décrit l'Analyseur de sophismes complexes amélioré, un outil conçu pour analyser des structures argumentatives complexes et détecter les sophismes imbriqués ainsi que les contradictions multiples. Il peut générer une structure hiérarchique des sophismes et une matrice de confiance entre arguments.

---
**Fichier:** `docs/outils/integration_outils.md`
**Résumé:**
Ce guide explique comment intégrer les outils d'analyse rhétorique dans des projets existants, que ce soit via une utilisation directe en Python ou via des frameworks web comme Flask ou FastAPI. Il aborde également la gestion des dépendances et le déploiement.

---
**Fichier:** `docs/outils/outils_analyse_rhetorique.md`
**Résumé:**
Présente une vue d'ensemble des outils d'analyse rhétorique améliorés, leur architecture modulaire en trois couches (Stratégique, Tactique, Opérationnel) et leurs objectifs. Il fournit un exemple d'utilisation du système global et les paramètres clés des principaux outils.

---
**Fichier:** `docs/outils/visualizer.md`
**Résumé:**
Décrit le Visualiseur de Résultats Rhétoriques, un outil qui génère des représentations graphiques des analyses argumentatives pour une meilleure compréhension. Il supporte différents styles (Mermaid, SVG) et niveaux de détail.

---
**Fichier:** `docs/planning_and_reports/plan_clarification_dossiers_dupliques.md`
**Résumé:**
Ce document expose un plan pour clarifier la fonction des dossiers nommés de manière similaire (`examples/` et `results/`) à la racine et dans `argumentation_analysis/`. La solution retenue est d'ajouter des fichiers README explicatifs dans chaque dossier concerné.

---
**Fichier:** `docs/planning_and_reports/rapport_corrections_appliquees.md`
**Résumé:**
Rapport finalisant les corrections appliquées à 13 problèmes identifiés, indiquant que 4 corrections ont été réussies. Il détaille les corrections, l'état actuel des tests, les problèmes restants et les recommandations pour les prochaines étapes.

---
**Fichier:** `docs/presentations/agents_logiques.md`
**Résumé:**
Présente une introduction générale aux agents logiques du système, couvrant les types d'agents (propositionnelle, premier ordre, modale), leur architecture commune et leurs fonctionnalités principales. Il aborde également leur intégration avec l'API Web et des cas d'utilisation.

---
**Fichier:** `docs/presentations/architecture_agents_logiques.md`
**Résumé:**
Détaille l'architecture des agents logiques, en exposant les principes de conception, un diagramme d'architecture, les composants principaux (AbstractLogicAgent, BeliefSet, TweetyBridge, LogicFactory), le flux de données et les mécanismes d'extension. Il aborde également des considérations techniques comme la performance et la sécurité.

---
**Fichier:** `docs/projets/sujets/aide/interface-web/DEMARRAGE_RAPIDE.md`
**Résumé:**
Fournit une checklist étape par étape pour démarrer rapidement le développement de l'interface web d'analyse argumentative. Il couvre la préparation de l'environnement, le lancement de l'API, la configuration de React et la création d'un premier composant de test.

---
**Fichier:** `docs/projets/sujets/aide/interface-web/GUIDE_UTILISATION_API.md`
**Résumé:**
Guide complet pour l'utilisation de l'API d'Analyse Argumentative, incluant l'installation, la configuration, le démarrage, la description des endpoints disponibles (analyse, validation, sophismes, framework de Dung), des exemples d'utilisation et des conseils pour l'intégration avec React.

---
**Fichier:** `docs/projets/sujets/aide/interface-web/TROUBLESHOOTING.md`
**Résumé:**
Guide de dépannage pour l'interface web d'analyse argumentative, couvrant les problèmes courants liés au démarrage de l'API, aux erreurs de connexion, CORS, dépendances, React, et aux erreurs d'analyse. Il propose des outils de diagnostic et des conseils pour demander de l'aide.

---
**Fichier:** `docs/projets/sujets/aide/interface-web/exemples-react/README.md`
**Résumé:**
Présente une collection d'exemples de composants React pour interagir avec l'API d'argumentation. Il décrit les composants disponibles (Demo, ArgumentAnalyzer, ValidationForm, FallacyDetector, FrameworkBuilder), le hook personnalisé `useArgumentationAPI`, et des utilitaires de formatage et validation.

---
**Fichier:** `docs/projets/sujets/aide/FAQ_DEVELOPPEMENT.md`
**Résumé:**
Foire Aux Questions (FAQ) destinée aux développeurs du projet d'analyse d'arguments. Elle couvre des sujets variés tels que la documentation générale, l'API Web, le moteur d'analyse, l'interface web, les tests, le déploiement et les bonnes pratiques de contribution.

---
**Fichier:** `docs/projets/sujets/aide/GUIDE_INTEGRATION_PROJETS.md`
**Résumé:**
Guide destiné aux étudiants pour faciliter l'intégration de leurs projets au sein du système global d'Intelligence Symbolique. Il présente une vue d'ensemble du projet, son architecture, et des conseils spécifiques pour les projets d'interface web et de serveur MCP.

---
**Fichier:** `docs/projets/sujets/2.5.6_Protection_Systemes_IA_Attaques_Adversariales.md`
**Résumé:**
Décrit un sujet de projet expert axé sur la protection des systèmes d'IA contre les attaques adversariales. Il aborde les fondements théoriques, les types d'attaques spécifiques aux systèmes argumentatifs et aux LLMs (jailbreaking, prompt injection), les mécanismes de défense, et l'implémentation pratique.

---
**Fichier:** `docs/projets/sujets/3.1.1_Interface_Web_Analyse_Argumentative.md`
**Résumé:**
Détaille un sujet de projet avancé pour la création d'une interface web pour l'analyse argumentative. Il couvre l'architecture de l'interface, les technologies frontend, l'intégration avec le backend API, les fonctionnalités argumentatives à implémenter, et la visualisation avancée.

---
**Fichier:** `docs/projets/sujets/Custom_Speech_to_Text_Analyse_Arguments_Fallacieux.md`
**Résumé:**
Guide pédagogique pour un projet combinant Speech-to-Text (STT) et analyse d'arguments fallacieux. Il décrit l'architecture du pipeline, l'intégration avec Whisper-WebUI, l'analyse des sophismes spécifiques à l'audio, et l'intégration potentielle avec TweetyProject.

---
**Fichier:** `docs/projets/sujets/sujet_1.1.5_formules_booleennes_quantifiees.md`
**Résumé:**
Présente un sujet de projet avancé sur l'analyse et la résolution de Formules Booléennes Quantifiées (QBF) en utilisant TweetyProject. Il détaille les objectifs, l'implémentation Python avec JPype, les tests et les livrables attendus pour créer un agent spécialiste QBF.

---
**Fichier:** `docs/projets/sujets/sujet_2.1.4_documentation_coordination.md`
**Résumé:**
Décrit un sujet de projet transversal axé sur la documentation et la coordination du projet global d'Intelligence Symbolique. Il définit les rôles, responsabilités, méthodologies et outils pour assurer la clarté, la cohérence et la fluidité du travail entre les équipes.

---
**Fichier:** `docs/projets/sujets/sujet_2.3.5_agent_evaluation_qualite.md`
**Résumé:**
Détaille un sujet de projet pour développer un agent d'évaluation de la qualité argumentative, allant au-delà de la simple détection de sophismes. Il aborde la taxonomie des vertus argumentatives, la conception de l'agent, les approches de détection et l'intégration avec l'agent de détection de sophismes.

---
**Fichier:** `docs/projets/ACCOMPAGNEMENT_ETUDIANTS.md`
**Résumé:**
Document centralisant les informations, conseils, problèmes connus et ressources pour accompagner les étudiants travaillant sur le projet 'argumentation_analysis'. Il aborde des points d'attention généraux, des problèmes spécifiques (comme l'import de `InformationObject` de Tweety) et les bonnes pratiques.

---
**Fichier:** `docs/projets/ACCUEIL_ETUDIANTS_SYNTHESE.md`
**Résumé:**
Synthèse d'accueil pour les étudiants du projet 'argumentation_analysis'. Il résume les objectifs du projet, les modalités de travail, le choix des sujets, les ressources techniques essentielles, le calendrier suggéré et les livrables attendus.

---
**Fichier:** `docs/projets/developpement_systeme.md`
**Résumé:**
Présente les sujets de projets axés sur le développement système et l'infrastructure du projet d'analyse argumentative. Il couvre l'architecture et l'orchestration des agents, la gestion des sources et données, le moteur agentique et les agents spécialistes, l'indexation sémantique, ainsi que l'automatisation et l'intégration MCP.

---
**Fichier:** `docs/projets/exemples_tweety_par_projet.md`
**Résumé:**
Fournit des extraits de code de la bibliothèque TweetyProject, organisés par sujet de projet. Ce document vise à aider les étudiants à trouver rapidement des exemples pertinents pour l'implémentation de leurs fonctionnalités spécifiques liées aux logiques formelles et aux frameworks d'argumentation.

---
**Fichier:** `docs/projets/exemples_tweety.md`
**Résumé:**
Guide connectant les concepts théoriques d'IA symbolique aux exemples pratiques du notebook `Tweety.ipynb`. Il aide à comprendre comment les fonctionnalités de TweetyProject (logiques formelles, frameworks d'argumentation, révision de croyances) peuvent être appliquées aux projets étudiants.

---
**Fichier:** `docs/projets/experience_utilisateur.md`
**Résumé:**
Présente les sujets de projets orientés vers l'expérience utilisateur et les applications concrètes du système d'analyse argumentative. Il couvre le développement d'interfaces utilisateurs (web, mobile, dashboard, éditeur visuel), les projets intégrateurs (débat assisté, éducation, aide à la décision) et les projets de lutte contre la désinformation.

---
**Fichier:** `docs/projets/fondements_theoriques.md`
**Résumé:**
Décrit les sujets de projets centrés sur les aspects formels, logiques et théoriques de l'argumentation. Il aborde l'intégration de diverses logiques (propositionnelle, FOL, modale, DL, QBF, CL), les frameworks d'argumentation (Dung, bipolaire, pondéré, ABA, VAF, ASPIC+, ADF), les taxonomies, la maintenance de la vérité et la vérification formelle.

---
**Fichier:** `docs/projets/matrice_interdependances.md`
**Résumé:**
Présente les relations et interdépendances entre les différents sujets de projets, organisées par grandes catégories (fondements théoriques, développement système, expérience utilisateur, lutte contre la désinformation). Il vise à aider à comprendre l'articulation des projets et à identifier les synergies.

---
**Fichier:** `docs/projets/message_annonce_etudiants.md`
**Résumé:**
Annonce officielle du projet 'argumentation_analysis' pour les étudiants de l'EPITA. Elle détaille les objectifs pédagogiques, les modalités de travail, les livrables attendus, les ressources disponibles, les critères d'évaluation, le calendrier suggéré et la structure des sujets de projets.

---
**Fichier:** `docs/projets/modeles_affaires_ia.md`
**Résumé:**
Explore différents modèles d'affaires et cas d'usage commerciaux pour les systèmes d'analyse argumentative et de lutte contre la désinformation. Il aborde les modèles SaaS, API, licences, les secteurs d'application (médias, éducation, politique, entreprises), des études de cas, les considérations éthiques et les stratégies de mise sur le marché.

---
**Fichier:** `docs/projets/SUIVI_PROJETS_ETUDIANTS.md`
**Résumé:**
Document destiné à centraliser les informations relatives à l'avancement des projets étudiants du module d'Intelligence Symbolique 2025. Il liste les projets avec leurs référents, liens vers les sujets, état d'avancement, prochains jalons et points de blocage.

---
**Fichier:** `docs/projets/sujets_projets_detailles.md`
**Résumé:**
Document central présentant en détail tous les sujets de projets disponibles pour le module d'Intelligence Symbolique, organisés en trois catégories principales : fondements théoriques et techniques, développement système et infrastructure, et expérience utilisateur et applications. Il fournit également des informations générales sur TweetyProject.

---
**Fichier:** `docs/projets/SYNTHESE_THEMATIQUE_PROJETS.md`
**Résumé:**
Propose une synthèse thématique des sujets de projets pour faciliter la compréhension des liens entre eux et encourager la collaboration. Il regroupe les projets par grandes thématiques : Fondements Théoriques, Développement Système et Infrastructure, et Expérience Utilisateur et Applications (incluant la lutte contre la désinformation).

---
**Fichier:** `docs/reference/agents/extract_agent_api.md`
**Résumé:**
Détaille l'API de l'Agent d'Extraction, responsable de l'identification et de l'extraction de segments pertinents dans un texte source. Il décrit son rôle, son architecture (plugin Semantic Kernel), les classes principales, les méthodes publiques (extraction, réparation, validation) et son interaction avec le StateManager.

---
**Fichier:** `docs/reference/agents/informal_agent_api.md`
**Résumé:**
Décrit l'API de l'Agent d'Analyse Informelle, chargé de l'identification des arguments et de l'analyse des sophismes. Il présente son rôle, son architecture (plugin Semantic Kernel), les méthodes publiques (identification d'arguments, analyse et attribution de sophismes, exploration de taxonomie) et son interaction avec le StateManager.

---
**Fichier:** `docs/reference/agents/pl_agent_api.md`
**Résumé:**
Présente l'API de l'Agent de Logique Propositionnelle (PL), responsable de la formalisation logique des arguments et de la vérification de leur validité en utilisant TweetyProject via JPype. Il détaille son rôle, son architecture (plugin Semantic Kernel), les prérequis techniques, les méthodes publiques (traduction texte vers BeliefSet, génération et exécution de requêtes) et la syntaxe BNF de Tweety.

---
**Fichier:** `docs/reference/agents/pm_agent_api.md`
**Résumé:**
Détaille l'API de l'Agent Project Manager (PM), le composant central d'orchestration du système d'analyse argumentative. Il décrit son rôle (planification, délégation, suivi, synthèse), son architecture (plugin Semantic Kernel), ses méthodes publiques (définition de tâches, écriture de conclusion) et son interaction avec le StateManager.

---
**Fichier:** `docs/reference/agents/README.md`
**Résumé:**
Fournit une vue d'ensemble des agents spécialisés du système d'analyse argumentative (Project Manager, Analyse Informelle, Logique Propositionnelle, Extraction). Il décrit leurs rôles respectifs, le flux de travail typique, les principes de conception communs et les interactions entre agents.

---
**Fichier:** `docs/reference/orchestration/analysis_runner.md`
**Résumé:**
Décrit l'API du module `analysis_runner.py` qui implémente l'approche d'orchestration simple via un `AgentGroupChat` de Semantic Kernel. Il détaille la fonction principale `run_analysis_conversation`, son fonctionnement, les stratégies d'orchestration utilisées (SimpleTerminationStrategy, DelegatingSelectionStrategy) et fournit un exemple d'appel.

---
**Fichier:** `docs/reference/orchestration/hierarchical_architecture_api.md`
**Résumé:**
Présente l'API de l'Architecture Hiérarchique, une approche d'orchestration avancée organisant le système en niveaux stratégique, tactique et opérationnel. Il décrit la structure du répertoire, les composants principaux de chaque niveau, les interfaces entre niveaux et un exemple de flux de travail.

---
**Fichier:** `docs/reference/orchestration/operational_level_api.md`
**Résumé:**
Détaille l'API du Niveau Opérationnel de l'architecture hiérarchique, responsable de l'exécution concrète des tâches d'analyse. Il décrit les composants principaux comme `OperationalManager`, `AgentRegistry`, l'interface `OperationalAgent` et les adaptateurs d'agents.

---
**Fichier:** `docs/reference/orchestration/README.md`
**Résumé:**
Fournit une vue d'ensemble de l'API d'Orchestration, qui définit les interfaces et composants pour la coordination des agents. Il compare l'approche d'orchestration simple (`analysis_runner.py`) et l'architecture hiérarchique, et donne des exemples d'utilisation pour chacune.

---
**Fichier:** `docs/reference/orchestration/strategic_level_api.md`
**Résumé:**
Décrit l'API du Niveau Stratégique de l'architecture hiérarchique, responsable de la planification globale, de l'allocation des ressources et des décisions de haut niveau. Il présente les composants `StrategicManager`, `ResourceAllocator`, `StrategicPlanner`, `StrategicState` et `StrategicTacticalInterface`.

---
**Fichier:** `docs/reference/orchestration/tactical_level_api.md`
**Résumé:**
Détaille l'API du Niveau Tactique de l'architecture hiérarchique, chargé de la coordination des tâches, de la résolution des conflits et de la supervision des agents opérationnels. Il décrit les composants `TaskCoordinator`, `ProgressMonitor`, `ConflictResolver`, `TacticalState` et `TacticalOperationalInterface`.

---
**Fichier:** `docs/reference/README.md`
**Résumé:**
Sert de point d'entrée pour la documentation de référence des API du système d'analyse argumentative. Il liste les documents disponibles pour l'API du système de communication, des agents et de l'orchestration, et explique l'organisation générale de cette référence.

---
**Fichier:** `docs/reference/reference_api.md`
**Résumé:**
Documentation de référence de l'API du système de communication multi-canal. Elle détaille le middleware de messagerie, les canaux de communication (hiérarchique, collaboration, données, négociation, feedback), les adaptateurs d'agents, la structure des messages et les protocoles de communication.

---
**Fichier:** `docs/reports/rapport_workflow_collaboratif/rapport_analyse_workflow_collaboratif.md`
**Résumé:**
Rapport d'analyse du workflow collaboratif du projet, synthétisant les analyses précédentes sur le flux de conversation, les capacités de l'agent informel et l'interaction avec l'état partagé. Il décrit l'architecture multi-agents, les mécanismes d'orchestration, l'exploration de la taxonomie des sophismes, et formule des recommandations d'amélioration.

---
**Fichier:** `docs/reports/etat_depot_couverture_tests.md`
**Résumé:**
Rapport sur l'état du dépôt Git et la couverture des tests au 21/05/2025. Il analyse l'état des branches, les derniers commits, la structure du projet, la couverture des tests par module, les problèmes d'importation rencontrés et formule des recommandations pour améliorer la couverture.

---
**Fichier:** `docs/reports/extraits_chiffres.md`
**Résumé:**
Documentation sur le fichier chiffré `extract_sources.json.gz.enc` qui contient des définitions d'extraits de texte. Il explique sa structure, le mécanisme de chiffrement, son rôle dans le système, les outils de manipulation et de réparation des extraits, et fournit des exemples d'utilisation.

---
**Fichier:** `docs/reports/rapport_final_tests.md`
**Résumé:**
Rapport consolidé sur l'amélioration et la validation des tests. Il détaille les actions effectuées pour corriger les problèmes d'environnement et de syntaxe, l'état actuel des tests (stables et globaux), la couverture de code obtenue, les problèmes restants et les recommandations pour l'amélioration continue. Il inclut également une section sur l'approche des tests mockés et leurs résultats.

---
**Fichier:** `docs/reports/rapport_suivi_tests.md`
**Résumé:**
Rapport de suivi des tests avec mesure de couverture, détaillant les modifications apportées pour permettre l'exécution de certains tests (mocks pour `ExtractAgent` et `jpype`). Il présente les résultats de couverture pour les modules de communication, les problèmes persistants et des recommandations. Il inclut également une section sur la correction d'un problème de déchiffrement et d'un blocage des tests asynchrones.

---
**Fichier:** `docs/reports/rapport_usage_corpus_chiffre.md`
**Résumé:**
Rapport authentique sur l'état réel des développements des agents logiques au 27 mai 2025, remplaçant un document précédent avec des données fictives. Il décrit l'architecture développée, les fonctionnalités réellement implémentées (opérationnelles, partielles, non implémentées), les limitations actuelles et formule des recommandations pour un développement authentique.

---
**Fichier:** `docs/reports/README.md`
**Résumé:**
Présente le répertoire des rapports d'analyse du projet. Il décrit la structure du répertoire, les types de rapports disponibles (performance, workflow, couverture de tests, extraits chiffrés), leur utilisation et comment générer de nouveaux rapports.

---