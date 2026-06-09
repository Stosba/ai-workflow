# AGENTS

Instructions globales pour tous les agents du projet.

## Architectural Decisions

Avant de proposer un changement qui touche à la structure ou aux choix
fondamentaux du projet, lis `/docs/adr/` pour comprendre les décisions
existantes.

**Règle** : ne jamais renverser une ADR sans la mentionner explicitement
dans le plan (`@plan`), avec la référence ADR-XXX et le rationnel original.

Si une nouvelle décision structurante est prise pendant le workflow,
`@review` délègue à `@adr` pour la documenter.

## Fragmentation des tâches

`@plan` applique l'heuristique suivante :
- **Fichiers modifiés disjoints** → tâches séparées, un agent par tâche
- **Même module touché par plusieurs tâches** → regrouper sous un seul agent

Si le plan fragmente des tâches qui touchent le même module, ajouter
une section "Contrats d'interface" explicitant le contrat entre agents.
