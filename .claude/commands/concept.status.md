# /concept.status

Quick overview of current conceptual model state.

## Purpose

Get a fast, compact summary of your model's progress without a full review. Perfect for quick check-ins during development.

## Usage

```
/concept.status
```

## Workflow

When this command is executed, follow these steps:

### 1. Locate Conceptual Model

Find the active conceptual model file in `docs/`:
- If multiple exist, show status for all (or ask which one)
- If none exist, guide user to `/concept.init`

### 2. Count Elements

Quickly scan the model and count:

**Objects:**
- Count entries in "3. Object Model" section
- Note which objects are fully defined (have mental model, attributes, actions)
- Identify incomplete objects

**Relationships:**
- Count entries in "4. Relationships & Rules" section
- Note types (1:1, 1:n, n:n)

**Workflows:**
- Count entries in "5. User Actions & Workflows" section
- Note complexity (simple, medium, complex)

**Sections:**
- Check which of 15 sections have content
- Calculate section completeness

### 3. Calculate Quick Completeness

Use simplified formula:
```
Objects Score = (Complete Objects / 5 target) * 30%
Relationships Score = (Relationships / Expected) * 30%
Workflows Score = (Workflows / 3 target) * 20%
Sections Score = (Filled Sections / 15) * 20%

Total = Objects + Relationships + Workflows + Sections
```

Expected relationships = (Objects * (Objects - 1)) / 2

### 4. Identify Next Step

Based on what's missing, suggest ONE specific next action:

**Priority Logic:**
1. If <3 objects → Add objects
2. If objects but no relationships → Map relationships
3. If relationships but no workflows → Add workflows
4. If basic complete → Review for gaps
5. If >70% complete → Generate final document

### 5. Display Compact Status

```
┌─────────────────────────────────────────────┐
│ Conceptual Model: <ApplicationName>        │
├─────────────────────────────────────────────┤
│                                             │
│ 📦 Objects:         <count>                 │
│    <Object1>, <Object2>, <Object3>...       │
│    └─ <X> complete, <Y> need work           │
│                                             │
│ 🔗 Relationships:   <count> mapped          │
│    └─ <count> of ~<expected> possible       │
│                                             │
│ ⚡ Workflows:        <count> defined        │
│    • <Workflow1>                            │
│    • <Workflow2>                            │
│    [...]                                    │
│                                             │
│ 📊 Completeness:    ~<percentage>%          │
│    ████████░░░░░░░░                         │
│                                             │
│ 📝 Sections:        <filled>/<total>        │
│    ✅ Executive Summary                     │
│    ✅ Core Model                            │
│    ✅ Object Model                          │
│    ⚠️  Relationships (incomplete)           │
│    ❌ Error Handling (empty)                │
│    [... show all 15 sections ...]          │
│                                             │
├─────────────────────────────────────────────┤
│ 🎯 Next Suggested Step:                     │
│                                             │
│ → /concept.add-relationship User Recipe    │
│                                             │
│ Why: You have objects but relationships     │
│ need to be mapped to show how they connect  │
│                                             │
├─────────────────────────────────────────────┤
│ Quick Actions:                              │
│ • Review model: /concept.review             │
│ • Add object: /concept.add-object <name>    │
│ • Generate doc: /concept.generate           │
└─────────────────────────────────────────────┘

Last modified: <date-time>
```

## Important Guidelines

1. **Be Fast**: No deep analysis, just counts and quick assessment
2. **Be Specific**: Reference actual object names, not placeholders
3. **One Suggestion**: Only provide ONE next step to avoid overwhelm
4. **Visual Progress**: Use progress bar for quick visual reference
5. **Compact Format**: Fit everything in one screenful

## Status Levels

### 🔴 Getting Started (0-30%)
```
Status: Just beginning
Message: "Let's build out your core objects first"
Next: /concept.add-object <name>
```

### 🟡 Building (30-60%)
```
Status: Making progress
Message: "Good foundation, now connect the pieces"
Next: /concept.add-relationship <from> <to>
```

### 🟢 Maturing (60-80%)
```
Status: Looking solid
Message: "Model is taking shape, add workflows"
Next: /concept.add-action <action>
```

### 🔵 Nearly Complete (80-95%)
```
Status: Almost ready
Message: "Polish remaining sections"
Next: /concept.review (for final checks)
```

### ✅ Complete (95-100%)
```
Status: Ready to generate
Message: "Model is comprehensive and ready"
Next: /concept.generate
```

## Examples

### Example 1: Early Stage

```
User: /concept.status

Output:
┌─────────────────────────────────────────────┐
│ Conceptual Model: RecipeBook                │
├─────────────────────────────────────────────┤
│ 📦 Objects:         2                       │
│    Recipe, User                             │
│    └─ 1 complete, 1 incomplete              │
│                                             │
│ 🔗 Relationships:   0 mapped                │
│    └─ 0 of ~1 possible                      │
│                                             │
│ ⚡ Workflows:        0 defined               │
│                                             │
│ 📊 Completeness:    ~28%                    │
│    ████░░░░░░░░░░░░░                        │
│                                             │
├─────────────────────────────────────────────┤
│ 🎯 Next: /concept.add-object Ingredient     │
│    Build your core objects first            │
└─────────────────────────────────────────────┘
```

### Example 2: Mid-Stage

```
User: /concept.status

Output:
┌─────────────────────────────────────────────┐
│ Conceptual Model: RecipeBook                │
├─────────────────────────────────────────────┤
│ 📦 Objects:         5                       │
│    Recipe, User, Ingredient, Tag,           │
│    Collection                               │
│    └─ 5 complete                            │
│                                             │
│ 🔗 Relationships:   3 mapped                │
│    └─ 3 of ~10 possible                     │
│                                             │
│ ⚡ Workflows:        1 defined               │
│    • Creating a Recipe                      │
│                                             │
│ 📊 Completeness:    ~58%                    │
│    ████████████░░░░░                        │
│                                             │
├─────────────────────────────────────────────┤
│ 🎯 Next: /concept.add-relationship Recipe   │
│          Ingredient                         │
│    Connect your objects to show structure   │
└─────────────────────────────────────────────┘
```

### Example 3: Nearly Complete

```
User: /concept.status

Output:
┌─────────────────────────────────────────────┐
│ Conceptual Model: RecipeBook                │
├─────────────────────────────────────────────┤
│ 📦 Objects:         5 (all complete)        │
│ 🔗 Relationships:   8 mapped                │
│ ⚡ Workflows:        4 defined               │
│ 📊 Completeness:    ~83%                    │
│    █████████████████░░                      │
│                                             │
├─────────────────────────────────────────────┤
│ 🎯 Next: /concept.review                    │
│    Final review before generating           │
└─────────────────────────────────────────────┘
```

## Comparison: Status vs Review

**Use /concept.status when:**
- Quick check-in
- Want to know what to do next
- Need motivation (see progress)
- During active development

**Use /concept.review when:**
- Deep analysis needed
- Finding gaps and issues
- Before generating final doc
- Quality assurance

## Error Handling

- **No conceptual model**: "No model found. Start with /concept.init <name>"
- **Empty model**: "Model exists but is empty. Add objects with /concept.add-object"
- **Multiple models**: Show status for all or ask which one

## Suggested Next Steps Logic

```python
if objects < 3:
    suggest: /concept.add-object <name>
    reason: "Build your core objects first"

elif relationships == 0:
    suggest: /concept.add-relationship <obj1> <obj2>
    reason: "Connect your objects to show structure"

elif workflows < 2:
    suggest: /concept.add-action <action>
    reason: "Document how users accomplish tasks"

elif completeness < 70:
    suggest: /concept.review
    reason: "Review model for gaps and improvements"

else:
    suggest: /concept.generate
    reason: "Model is ready for final document generation"
```

## Progress Bar Rendering

```
0-20%:   ████░░░░░░░░░░░░░░
20-40%:  ████████░░░░░░░░░░
40-60%:  ████████████░░░░░░
60-80%:  ████████████████░░
80-100%: ██████████████████
```

## Reference

- Compare with `/concept.review` for detailed analysis
- See `examples/` for models at different stages
- Use `/concept.generate` when status shows >70% complete
