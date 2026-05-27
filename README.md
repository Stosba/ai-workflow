# convert

CLI Python de conversion d'unités — distance (km/miles), masse (kg/lbs), température (°C/°F).

```bash
convert 10 km miles
# → 10.0 km = 6.21371 miles

convert 100 celsius fahrenheit
# → 100.0 celsius = 212.0 fahrenheit

convert 1 km kg
# → Error: Cannot convert km (distance) to kg (mass)
```

---

## 🤖 Workflow agentic (opencode)

Ce projet utilise un pipeline agentic orchestré par **opencode** via la commande `/workflow`.

### Principe

Le workflow enchaîne 4 agents spécialisés, chacun attendant la fin du précédent :

```
/workflow <description de la tâche>
```

### Les 5 étapes

| Étape | Agent | Rôle |
|---|---|---|
| **1. PLAN** | `@plan` | Analyse le codebase, découpe la demande en sous-tâches précises, fichiers concernés, critères de succès. **Ne touche à aucun fichier.** |
| **2. BUILD** | `@build` | Implémente le code planifié, lance les tests, itère jusqu'à ce que tout passe (max 5 tentatives). |
| **3. TEST** | `@test` | Vérifie les tests existants, en ajoute si nécessaire, exécute et valide (max 2 tentatives). |
| **4. REVIEW** | `@review` | Analyse le diff final (lisibilité, conventions, sécurité, performance). **Ne modifie rien.** |
| **5. COMMIT** | — | Commit conventionnel + draft PR. |

### Agents personnalisés

Les agents sont définis dans `.opencode/agents/` et chargés automatiquement par opencode.

| Fichier | Modèle | Rôle |
|---|---|---|
| `.opencode/agents/plan.md` | DeepSeek V4 Pro | Planification uniquement |
| `.opencode/agents/build.md` | DeepSeek V4 Flash | Implémentation + tests |
| `.opencode/agents/test.md` | DeepSeek V4 Flash | Vérification des tests |
| `.opencode/agents/review.md` | DeepSeek V4 Flash | Revue qualité |

### Utilisation

```bash
# Dans opencode, taper :
/workflow ajouter le support des litres/gallons
```

Le pipeline exécute alors les 5 étapes séquentiellement.

### Configuration

La commande `/workflow` est définie dans `opencode.json` à la racine du projet, dans la section `command`. Les agents sont déclarés dans la section `agent` et leurs prompts se trouvent dans `.opencode/agents/`.

Après modification de `opencode.json` ou des agents, **redémarrer opencode** pour appliquer les changements.

---

## Installation

```bash
pip install -e .
```

## Tests

```bash
pytest tests/ -v
```
