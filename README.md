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

Le workflow enchaîne 6 agents spécialisés, chacun attendant la fin du précédent.
Chaque agent hérite des règles communes définies dans [`AGENTS.md`](./AGENTS.md).

```
/workflow <description de la tâche>
```

### Les 6 étapes

| Étape | Agent | Rôle |
|---|---|---|
| **1. PLAN** | `@plan` | Analyse le codebase (`docs/adr/` inclus), découpe la demande en sous-tâches. Applique l'heuristique d'`AGENTS.md` : fichiers disjoints → tâches séparées, même module → tâche groupée. **Ne touche à aucun fichier.** |
| **2. BUILD** | `@build` | Implémente le code planifié, lance les tests, itère jusqu'à ce que tout passe (max 5 tentatives). |
| **3. TEST** | `@test` | Vérifie les tests existants, en ajoute si nécessaire, exécute et valide (max 2 tentatives). |
| **4. DOGFOOD** | `@dogfood` | Teste la **surface publique** comme un utilisateur final, sans accès au code source. Si FAIL → retour à l'étape 2 (max 2 cycles). |
| **5. REVIEW** | `@review` | Analyse le diff final (lisibilité, conventions, sécurité, performance). Si une décision structurante a été prise, délègue à `@adr`. |
| **6. COMMIT** | — | Commit conventionnel + draft PR. |

### Boucle de correction Dogfood

Si `@dogfood` détecte un échec, le workflow revient à `@build` pour correction,
puis relance `@dogfood`. Maximum 2 cycles. Au-delà, documenter dans la PR.

### ADRs — Mémoire architecturale

Les décisions structurantes sont documentées dans `docs/adr/` sous forme
d'ADR (Architectural Decision Records), suivant le template `000-template.md`.

`@adr` est appelé par `@review` uniquement si une décision mérite d'être
formalisée (nouveau pattern, dépendance majeure, choix de stockage, etc.).
Si rien de structurant n'a été décidé, aucune ADR n'est créée.

### Agents personnalisés

Les agents sont définis dans `.opencode/agents/` et chargés automatiquement par opencode.

| Fichier | Modèle | Rôle |
|---|---|---|
| `.opencode/agents/plan.md` | DeepSeek V4 Pro | Planification uniquement |
| `.opencode/agents/build.md` | DeepSeek V4 Flash | Implémentation + tests |
| `.opencode/agents/test.md` | DeepSeek V4 Flash | Vérification des tests |
| `.opencode/agents/dogfood.md` | DeepSeek V4 Flash | Test surface publique (sandboxé) |
| `.opencode/agents/review.md` | DeepSeek V4 Flash | Revue qualité |
| `.opencode/agents/adr.md` | DeepSeek V4 Flash | Documentation architecturale |

### Règles globales — AGENTS.md

Tous les agents héritent des instructions d'[`AGENTS.md`](./AGENTS.md) :
- Ne jamais renverser une ADR sans la mentionner explicitement dans le plan
- Fragmentation des tâches : fichiers disjoints ok, même module = un seul agent
- `@review` délègue à `@adr` pour documenter les décisions structurantes

### Utilisation

```bash
# Dans opencode, taper :
/workflow ajouter le support des litres/gallons
```

Le pipeline exécute alors les 6 étapes séquentiellement.

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
