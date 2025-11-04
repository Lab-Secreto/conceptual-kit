# /concept.review

Review conceptual model completeness and get improvement suggestions.

## Purpose

Analyze the current state of your conceptual model, identify gaps, and provide specific recommendations for improvement. This helps ensure your model is comprehensive and user-centric.

## Usage

```
/concept.review
```

## Workflow

When this command is executed, follow these steps:

### 1. Locate Conceptual Model

Find the active conceptual model file in `docs/`:
- If multiple exist, ask which one to review
- If none exist, guide user to `/concept.init`

### 2. Analyze Completeness

Systematically check all sections:

#### Executive Summary (5%)
- ✅/❌ Application name defined
- ✅/❌ Purpose statement clear
- ✅/❌ Target users identified
- ✅/❌ Creation date present

#### Core Conceptual Model (10%)
- ✅/❌ Central metaphor defined
- ✅/❌ Key principles listed
- ✅/❌ Mental model explained

#### Object Model (25%)
- ✅/❌ At least 3 objects defined
- ✅/❌ All objects have mental models
- ✅/❌ All objects have attributes
- ✅/❌ All objects have actions
- ✅/❌ States defined where applicable

#### Relationships & Rules (20%)
- ✅/❌ Relationships mapped
- ✅/❌ At least 50% of possible relationships defined
- ✅/❌ Relationship diagram present
- ✅/❌ Cardinality specified

#### User Actions & Workflows (20%)
- ✅/❌ At least 2 workflows defined
- ✅/❌ Steps include mental models
- ✅/❌ Objects referenced in workflows
- ✅/❌ Success criteria defined

#### Information Architecture (5%)
- ✅/❌ Navigation structure outlined
- ✅/❌ Content organization described

#### State Model (5%)
- ✅/❌ Object states documented
- ✅/❌ State transitions defined

#### Error Handling (5%)
- ✅/❌ Error scenarios listed
- ✅/❌ User-facing messages defined

#### Other Sections (5%)
- ✅/❌ Design principles present
- ✅/❌ Platform adaptations considered

### 3. Calculate Completeness Percentage

Weight each section by importance:
- Core sections (Objects, Relationships, Workflows): 65%
- Supporting sections (States, Errors, Architecture): 25%
- Documentation (Summary, Principles): 10%

Formula:
```
Completeness = (Checked Items / Total Items) * 100
```

### 4. Identify Missing Relationships

Analyze which objects should be related but aren't:
- For each object, check if it relates to other objects
- Identify obvious missing connections
- Suggest 3-5 relationships to add

### 5. Suggest Next Steps

Based on what's missing, provide prioritized suggestions:
1. Critical gaps (objects without definitions)
2. Important additions (missing relationships)
3. Nice-to-haves (additional workflows)

### 6. Generate Review Report

Create formatted output:

```
╔═════════════════════════════════════════════════════╗
║  Conceptual Model Review                            ║
╟─────────────────────────────────────────────────────╢
║ Model: <ApplicationName>                            ║
║ File: docs/conceptual-model-<name>.md               ║
║ Last modified: <date>                               ║
╠═════════════════════════════════════════════════════╣
║ COMPLETENESS ANALYSIS                               ║
╟─────────────────────────────────────────────────────╢
║                                                     ║
║ Executive Summary                         [✅] 100% ║
║ ✅ Application name defined                         ║
║ ✅ Purpose statement clear                          ║
║ ✅ Target users identified                          ║
║                                                     ║
║ Core Conceptual Model                     [⚠️] 60%  ║
║ ✅ Central metaphor defined                         ║
║ ⚠️  Key principles incomplete                       ║
║ ❌ Mental model needs more detail                   ║
║                                                     ║
║ Object Model                              [✅] 85%  ║
║ ✅ 5 objects defined                                ║
║ ✅ All objects have mental models                   ║
║ ✅ Attributes defined                               ║
║ ⚠️  2 objects missing action lists                  ║
║                                                     ║
║ Relationships & Rules                     [⚠️] 45%  ║
║ ✅ 3 relationships mapped                           ║
║ ❌ 7 potential relationships missing                ║
║ ⚠️  Relationship diagram incomplete                 ║
║                                                     ║
║ User Actions & Workflows                  [❌] 30%  ║
║ ✅ 1 workflow defined                               ║
║ ❌ Need at least 2-3 more core workflows            ║
║ ❌ Missing navigation workflows                     ║
║                                                     ║
║ Supporting Sections                       [❌] 20%  ║
║ ❌ Error handling section empty                     ║
║ ❌ State model incomplete                           ║
║ ⚠️  Information architecture needs work             ║
║                                                     ║
╟─────────────────────────────────────────────────────╢
║ Overall Progress: ████████░░░░░░ 58%                ║
╠═════════════════════════════════════════════════════╣
║ RECOMMENDATIONS                                     ║
╟─────────────────────────────────────────────────────╢
║                                                     ║
║ 🔴 CRITICAL (Do These First)                        ║
║                                                     ║
║ 1. Complete action lists for Ingredient and Tag    ║
║    → /concept.add-object Ingredient (update)       ║
║                                                     ║
║ 2. Map missing key relationships:                  ║
║    → /concept.add-relationship User Collection     ║
║    → /concept.add-relationship Recipe Tag          ║
║    → /concept.add-relationship Collection Recipe   ║
║                                                     ║
║ 3. Add core workflows:                             ║
║    → /concept.add-action search-recipes            ║
║    → /concept.add-action share-recipe              ║
║                                                     ║
║ 🟡 IMPORTANT (Do These Next)                        ║
║                                                     ║
║ 4. Define error handling scenarios                 ║
║    - What happens when recipe save fails?          ║
║    - How are network errors communicated?          ║
║                                                     ║
║ 5. Complete state model                            ║
║    - Recipe states: draft → published → archived   ║
║    - User states: active → inactive                ║
║                                                     ║
║ 🟢 NICE TO HAVE (Polish)                            ║
║                                                     ║
║ 6. Add platform-specific adaptations               ║
║    - Mobile vs desktop differences                 ║
║                                                     ║
║ 7. Expand design principles                        ║
║    - Add 2-3 more key principles                   ║
║                                                     ║
╟─────────────────────────────────────────────────────╢
║ MISSING RELATIONSHIPS DETECTED                      ║
╟─────────────────────────────────────────────────────╢
║                                                     ║
║ Based on your objects, these relationships          ║
║ are likely missing:                                 ║
║                                                     ║
║ • User ↔ Collection (ownership)                     ║
║   Users probably have collections                   ║
║                                                     ║
║ • Recipe ↔ Tag (categorization)                     ║
║   Recipes are likely tagged for search              ║
║                                                     ║
║ • Collection ↔ Recipe (containment)                 ║
║   Collections contain recipes                       ║
║                                                     ║
║ • User ↔ Recipe (interaction)                       ║
║   Users might favorite/like recipes                 ║
║                                                     ║
╟─────────────────────────────────────────────────────╢
║ QUALITY CHECKS                                      ║
╟─────────────────────────────────────────────────────╢
║                                                     ║
║ ✅ Using user-centric language                      ║
║ ✅ Mental models are clear                          ║
║ ⚠️  Some workflows need more detail                 ║
║ ⚠️  ASCII diagrams could be improved                ║
║ ✅ Consistent naming conventions                    ║
║                                                     ║
╚═════════════════════════════════════════════════════╝

Next recommended command:
→ /concept.add-relationship User Collection

Would you like me to help with any of these improvements? (yes/no)
```

### 7. Offer Interactive Help

If user says yes, ask which improvement to tackle:
- Present numbered list of top 5 recommendations
- Execute the command they choose
- Return to review after completion

## Important Guidelines

1. **Be Specific**: Reference actual object names, not generic placeholders
2. **Prioritize**: Focus on critical gaps first
3. **Actionable**: Every recommendation should have a command to execute
4. **Encouraging**: Acknowledge progress, not just gaps
5. **Realistic**: Don't expect 100% completeness

## Completeness Targets

### Minimum Viable Model (50-60%)
- Executive summary complete
- 3+ objects with basic definitions
- 2+ key relationships
- 1-2 core workflows

### Good Model (70-80%)
- All core objects defined with full details
- Most relationships mapped
- 3-5 workflows covering main use cases
- Basic error handling

### Excellent Model (85-95%)
- All objects thoroughly defined
- All relationships mapped
- Comprehensive workflows
- States, errors, and edge cases documented
- Platform adaptations considered

### Note on 100%
Very few models reach 100%. A model at 75-85% is typically sufficient for most purposes.

## Examples

### Example 1: Early-Stage Model

```
User: /concept.review

Analysis:
- Objects: 3 defined (User, Recipe, Ingredient)
- Relationships: 1 mapped
- Workflows: 0
- Completeness: 35%

Critical gaps:
1. No workflows defined
2. Missing Recipe-Ingredient relationship
3. Objects need more detail

Recommendation: Start with /concept.add-action create-recipe
```

### Example 2: Nearly Complete Model

```
User: /concept.review

Analysis:
- Objects: 6 defined (all complete)
- Relationships: 8 mapped
- Workflows: 5 defined
- Completeness: 82%

Minor gaps:
1. Error handling section empty
2. Could add 1-2 more edge-case workflows

Recommendation: Add error scenarios or generate final document
```

## Error Handling

- **No conceptual model**: Guide to `/concept.init`
- **Empty model**: "Model is empty. Start with /concept.add-object"
- **Multiple models**: Ask which one to review

## Best Practices

### What to Check

**Object Completeness:**
- Every object has mental model description
- Attributes list is not empty
- Actions are defined
- States present if object changes over time

**Relationship Quality:**
- Clear cardinality (1:1, 1:n, n:n)
- User-facing description
- Bidirectionality considered

**Workflow Depth:**
- Steps include mental models
- Objects are referenced
- Success criteria defined
- Error cases considered

### Red Flags

- ❌ Objects without mental model descriptions
- ❌ Relationships without cardinality
- ❌ Workflows without step-by-step details
- ❌ Technical jargon instead of user language
- ❌ Empty critical sections (Objects, Relationships, Workflows)

### Green Flags

- ✅ Consistent user-centric language
- ✅ Real-world examples throughout
- ✅ Clear mental model descriptions
- ✅ Comprehensive but not over-engineered
- ✅ Workflows reference actual objects

## Reference

- See `examples/` for complete model comparisons
- Read `conceptual-modeling.md` for quality criteria
- Check other models at different completion stages
