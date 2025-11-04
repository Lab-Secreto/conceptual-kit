# /concept.add-relationship

Map relationships between objects in your conceptual model.

## Purpose

Define how objects connect and relate to each other from the user's perspective. Relationships help users understand how different parts of the application work together.

## Usage

```
/concept.add-relationship <from-object> <to-object>
```

## Workflow

When this command is executed, follow these steps:

### 1. Locate Conceptual Model

Find the active conceptual model file in `docs/`.

### 2. Validate Objects Exist

Check that both objects are defined in the "Object Model" section:
- If either doesn't exist: Show error and suggest adding objects first with `/concept.add-object`
- If both exist: Proceed with relationship definition

### 3. Check for Existing Relationship

Look in the "Relationships & Rules" section:
- If relationship already exists: Ask if user wants to update it
- If not: Proceed with creation

### 4. Gather Relationship Details

Use AskUserQuestion for structured input:

**Question 1: Relationship Type**
- Header: "Cardinality"
- Question: "What type of relationship is this?"
- Options:
  - One-to-one (1:1) - Each A has exactly one B (e.g., User has one Profile)
  - One-to-many (1:n) - Each A has multiple Bs (e.g., User has many Recipes)
  - Many-to-many (n:n) - Multiple As, multiple Bs (e.g., Recipes have many Tags, Tags have many Recipes)

**Question 2: Directionality**
- Header: "Direction"
- Question: "How do users think about this relationship?"
- Options:
  - Ownership (A owns/has B - e.g., "User has Recipes")
  - Association (A relates to B - e.g., "Recipe uses Ingredients")
  - Hierarchy (A contains B - e.g., "Folder contains Files")
  - Reference (A links to B - e.g., "Task references Project")

Then gather via text input:
- **User mental model phrase**: How would a user describe this? (e.g., "A user has many recipes they've saved")
- **Real-world example**: A concrete example (e.g., "Jane has 45 recipes in her collection")
- **Bidirectional**: Can users navigate both ways? (yes/no)

### 5. Create Relationship Entry

Add to "4. Relationships & Rules" section:

```markdown
#### <FromObject> → <ToObject>

**Cardinality:** <1:1 | 1:n | n:n>

**User's mental model:**
"<mental-model-phrase>"

**Type:** <Ownership | Association | Hierarchy | Reference>

**Bidirectional:** <Yes | No>
- Forward: "<FromObject> → <ToObject>" (e.g., "User sees their Recipes")
- Reverse: "<ToObject> → <FromObject>" (e.g., "Recipe belongs to User")

**Real-world example:**
"<concrete-example>"

**Implications for users:**
- <What this means for user workflows>
- <How users navigate this relationship>
- <Any constraints users should know>
```

### 6. Update Relationship Diagram

Update the ASCII relationship diagram in section 4:

```
┌─────────┐           ┌─────────┐
│  User   │ 1 ─────n  │ Recipe  │
└─────────┘  owns     └─────────┘
                           │
                          n│
                           │uses
                           │1
                      ┌─────────────┐
                      │ Ingredient  │
                      └─────────────┘
```

### 7. Update Object Cards

Go back to both object cards in section "3. Object Model" and add relationship notes:

For `<FromObject>`:
```markdown
**Relationships:**
- Has <ToObject> (<cardinality>)
```

For `<ToObject>`:
```markdown
**Relationships:**
- Belongs to <FromObject> (<cardinality>)
```

### 8. Confirm Addition

Display success message:

```
✅ Added relationship: <FromObject> → <ToObject>

🔗 Relationship details:
   Type: <cardinality>
   Mental Model: "<phrase>"
   Bidirectional: <yes/no>

📊 Model progress:
   Objects: <count>
   Relationships: <count>
   Completeness: ~<percentage>%

Next steps:
→ Map more relationships: /concept.add-relationship <from> <to>
→ Add user workflows: /concept.add-action <action-name>
→ Review model: /concept.review

Suggested relationships:
• <FromObject> ↔ <SuggestedObject>
• <ToObject> ↔ <AnotherSuggestedObject>
```

## Important Guidelines

1. **User Perspective**: Describe relationships how users think, not database schema
2. **Bidirectional Thinking**: Consider if users can navigate both directions
3. **Real Examples**: Always include concrete user scenarios
4. **Consistency**: Use consistent language with existing relationships
5. **Visual Diagrams**: Keep ASCII diagrams clean and readable

## Examples

### Example 1: User → Recipe (1:n)

```
User: /concept.add-relationship User Recipe

Inputs:
- Type: One-to-many (1:n)
- Direction: Ownership
- Mental model: "A user can save and organize multiple recipes"
- Example: "Sarah has 127 recipes in her cookbook"
- Bidirectional: Yes
  - Forward: "User browses their saved recipes"
  - Reverse: "Recipe shows who saved it"

Result: Added to docs/conceptual-model-recipe-book.md
```

### Example 2: Recipe → Ingredient (n:n)

```
User: /concept.add-relationship Recipe Ingredient

Inputs:
- Type: Many-to-many (n:n)
- Direction: Association
- Mental model: "A recipe needs multiple ingredients, and the same ingredient appears in many recipes"
- Example: "Chocolate Cake uses flour, sugar, eggs. Flour is used in 234 recipes"
- Bidirectional: Yes
  - Forward: "Recipe lists required ingredients"
  - Reverse: "Ingredient shows which recipes use it"

Result: Added to docs/conceptual-model-recipe-book.md
```

### Example 3: Task → Project (n:1)

```
User: /concept.add-relationship Task Project

Inputs:
- Type: Many-to-one (n:1)
- Direction: Hierarchy
- Mental model: "Multiple tasks belong to a project"
- Example: "Website Redesign project has 23 tasks"
- Bidirectional: Yes
  - Forward: "Task shows which project it's part of"
  - Reverse: "Project lists all its tasks"

Result: Added to docs/conceptual-model-project-manager.md
```

## Error Handling

- **Missing objects**: "Error: <ObjectName> doesn't exist. Add it first with /concept.add-object"
- **No conceptual model**: Guide to `/concept.init`
- **Invalid object names**: "Error: Couldn't find objects. Check spelling and capitalization"
- **Duplicate relationship**: Ask to confirm update or skip
- **Missing parameters**: Ask for object names

## Best Practices

### ✅ Good Relationship Descriptions

- "A user has many recipes they've collected" (user language)
- "Each recipe uses several ingredients" (natural phrasing)
- "Tasks are organized into projects" (how users think)

### ❌ Avoid Technical Descriptions

- "User has foreign key to Recipe table" (database terms)
- "Recipe.ingredients is a many-to-many junction" (technical jargon)
- "Task.project_id references Project.id" (implementation details)

### Relationship Patterns

**Ownership (Has/Owns)**
- User has Profile
- User has Posts
- Folder has Files

**Containment (Contains/Includes)**
- Project contains Tasks
- Album contains Photos
- Playlist contains Songs

**Association (Uses/References)**
- Recipe uses Ingredients
- Post references Tags
- Task links to Documents

**Hierarchy (Parent/Child)**
- Category has Subcategories
- Comment has Replies
- Folder has Subfolders

## Reference

- See `examples/` for relationship modeling examples
- Check `templates/components/relationship-diagram.md` for ASCII art patterns
- Read `conceptual-modeling.md` section on "Relationships and Structure"
