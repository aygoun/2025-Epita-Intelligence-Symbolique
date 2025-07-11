# Outils d'Analyse Rhétorique

Ce répertoire contient des outils spécialisés pour l'analyse rhétorique, conçus pour améliorer les capacités des agents spécialistes dans l'identification et l'évaluation des sophismes et des arguments.

## Structure

- `contextual_fallacy_analyzer.py` - Outil pour l'analyse contextuelle des sophismes
- `fallacy_severity_evaluator.py` - Outil pour l'évaluation de la gravité des sophismes
- `complex_fallacy_analyzer.py` - Outil pour l'analyse des sophismes complexes
- `rhetorical_result_analyzer.py` - Outil pour l'analyse des résultats d'une analyse rhétorique
- `rhetorical_result_visualizer.py` - Outil pour la visualisation des résultats d'une analyse rhétorique
- `enhanced/` - Versions améliorées des outils d'analyse rhétorique
- `new/` - Nouveaux outils d'analyse rhétorique

## Versions améliorées et nouvelles

Le répertoire contient également des versions améliorées et de nouveaux outils d'analyse rhétorique :

### Outils améliorés

Les [outils améliorés](./enhanced/README.md) offrent des fonctionnalités plus avancées et une meilleure précision par rapport aux versions de base :
- `EnhancedComplexFallacyAnalyzer` - Version améliorée de l'analyseur de sophismes complexes
- `EnhancedContextualFallacyAnalyzer` - Version améliorée de l'analyseur contextuel de sophismes
- `EnhancedFallacySeverityEvaluator` - Version améliorée de l'évaluateur de gravité des sophismes
- `EnhancedRhetoricalResultAnalyzer` - Version améliorée de l'analyseur de résultats rhétoriques

### Nouveaux outils

Les [nouveaux outils](./new/README.md) introduisent des fonctionnalités innovantes :
- `SemanticArgumentAnalyzer` - Analyseur sémantique d'arguments basé sur le modèle de Toulmin
- `ArgumentCoherenceEvaluator` - Évaluateur de cohérence entre arguments
- `ArgumentStructureVisualizer` - Visualiseur interactif de structures argumentatives
- `ContextualFallacyDetector` - Détecteur avancé de sophismes contextuels

## Utilisation

Ces outils sont conçus pour être utilisés par les agents spécialistes, en particulier l'agent Informel, pour améliorer leurs capacités d'analyse rhétorique. Ils peuvent être utilisés individuellement ou combinés pour une analyse plus complète.

### Exemple d'utilisation de l'analyseur contextuel de sophismes

```python
from argumentation_analysis.agents.tools.analysis.contextual_fallacy_analyzer import ContextualFallacyAnalyzer

# Initialiser l'analyseur
analyzer = ContextualFallacyAnalyzer()

# Analyser un argument dans son contexte
results = analyzer.analyze_context(
    text="Les experts sont unanimes : ce produit est sûr.",
    context="Discours commercial pour un produit controversé"
)

# Identifier les sophismes contextuels
fallacies = analyzer.identify_contextual_fallacies(
    argument="Les experts sont unanimes : ce produit est sûr.",
    context="Discours commercial pour un produit controversé"
)

print(f"Sophismes identifiés: {fallacies}")
```

### Exemple d'utilisation de l'évaluateur de gravité des sophismes

```python
from argumentation_analysis.agents.tools.analysis.fallacy_severity_evaluator import FallacySeverityEvaluator

# Initialiser l'évaluateur
evaluator = FallacySeverityEvaluator()

# Évaluer la gravité d'un sophisme
severity = evaluator.evaluate_severity(
    fallacy_type="Appel à l'autorité",
    argument="Les experts sont unanimes : ce produit est sûr.",
    context="Discours commercial pour un produit controversé"
)

print(f"Gravité du sophisme: {severity}")
```

## Intégration avec les Agents

Ces outils peuvent être intégrés aux agents spécialistes de plusieurs façons:

1. **Utilisation directe** - Les agents peuvent instancier et utiliser ces outils directement dans leur code.
2. **Intégration via plugins** - Les outils peuvent être encapsulés dans des plugins Semantic Kernel et exposés aux agents via des fonctions kernel.
3. **Extension des prompts** - Les insights générés par ces outils peuvent être utilisés pour enrichir les prompts des agents.

## Développement

Pour étendre ces outils ou en créer de nouveaux, suivez ces principes:

1. **Modularité** - Chaque outil doit avoir une responsabilité unique et bien définie.
2. **Compatibilité** - Les outils doivent être compatibles avec l'architecture existante et les conventions du projet.
3. **Documentation** - Chaque outil doit être bien documenté, avec des exemples d'utilisation.
4. **Tests** - Chaque outil doit être accompagné de tests unitaires et d'intégration.

## Voir aussi

- [Documentation des outils améliorés](./enhanced/README.md)
- [Documentation des nouveaux outils](./new/README.md)
- [Documentation des tests des outils](../../tests/tools/README.md)
- [Documentation de l'architecture hiérarchique](../../../orchestration/hierarchical/README.md)