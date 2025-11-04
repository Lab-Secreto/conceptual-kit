# /concept.add-object

Add a new object to your conceptual model.

## Purpose

Define a core object that users interact with in your application. Objects represent the primary "things" users think about and manipulate.

## Usage

```
/concept.add-object <object-name>
```

## Workflow

When this command is executed, follow these steps:

### 1. Locate Conceptual Model

Find the active conceptual model file:
- Look in `docs/` directory for `conceptual-model-*.md` files
- If multiple exist, ask user which one to update
- If none exist, guide user to run `/concept.init` first

### 2. Validate Object Doesn't Exist

Check if the object is already defined in the "Object Model" section:
- If exists: Inform user and ask if they want to update it
- If not: Proceed with creation

### 3. Gather Object Definition

Use AskUserQuestion for structured input:

**Question 1: Mental Model Category**
- Header: "Mental Model"
- Question: "What do users think this object IS?"
- Options:
  - Container (Holds other things - e.g., Folder, Cart, Playlist)
  - Item (A single thing - e.g., File, Product, Song)
  - Action (Something that happens - e.g., Event, Task, Reminder)
  - Space (A place or area - e.g., Dashboard, Feed, Timeline)
  - Person (User or entity - e.g., Profile, Contact, Team)
  - Collection (Group of items - e.g., Library, Album, List)

Then gather via text input:
- **Mental model description**: "In user's words, what is this object?" (1-2 sentences)
- **Visible attributes**: What can users see? (comma-separated: title, date, status, etc.)
- **User actions**: What can users do with this object? (comma-separated: create, edit, delete, share, etc.)
- **Possible states**: Does it have different states? (optional, comma-separated: draft, published, archived, etc.)

### 4. Create Object Card

Use the template from `templates/components/object-card.md` to create:

```markdown
### <ObjectName>

**What users think it is:**
"<mental-model-description>"

**Mental model category:** <category>

**Visible attributes:**
- <attribute1>
- <attribute2>
- <attribute3>

**Actions users can perform:**
- <action1> - <what it does>
- <action2> - <what it does>
- <action3> - <what it does>

**States:**
- <state1>: <description>
- <state2>: <description>

**Example in user language:**
"<real-world example of how users talk about this object>"
```

### 5. Insert into Object Model Section

Add the object card to section "3. Object Model" in the conceptual model file:
- Maintain alphabetical order (optional but recommended)
- Keep consistent formatting
- Update the object count in the section header

### 6. Update Hierarchy Diagram

Add the object to the mental model hierarchy (ASCII diagram):

```
Application
├── <ExistingObject1>
├── <NewObject>  ← Add here
└── <ExistingObject2>
```

If relationships are implied, show them:

```
User
├── <NewObject> (owns)
└── <ExistingObject>
```

### 7. Confirm Addition

Display success message:

```
✅ Added <ObjectName> to conceptual model

📝 Definition:
   Mental Model: "<description>"
   Attributes: <count> defined
   Actions: <count> defined
   States: <count> states

Next steps:
→ Add another object: /concept.add-object <name>
→ Map relationships: /concept.add-relationship <from> <to>
→ Review model: /concept.review

Suggested relationships to explore:
• User ↔ <ObjectName>
• <ObjectName> ↔ <RelatedObject>
```

## Important Guidelines

1. **User-Centric Language**: Describe what users think, not technical implementation
2. **Object Naming**: Use PascalCase (e.g., ShoppingCart, not shopping_cart)
3. **Mental Model First**: Focus on user perception before system design
4. **Real Examples**: Include phrases users actually say
5. **Consistency**: Maintain tone and style with existing objects

## Examples

### Example 1: Recipe Object

```
User: /concept.add-object Recipe

Inputs:
- Mental model: "A set of instructions to make a dish"
- Category: Item
- Attributes: title, ingredients, steps, prep time, servings, photo
- Actions: create, edit, delete, share, favorite, print
- States: draft, published, archived

Result: Added to docs/conceptual-model-recipe-book.md
```

### Example 2: Task Object

```
User: /concept.add-object Task

Inputs:
- Mental model: "Something I need to do"
- Category: Item + Action hybrid
- Attributes: title, description, due date, priority, assignee
- Actions: create, complete, edit, delete, postpone, assign
- States: open, in-progress, completed, cancelled

Result: Added to docs/conceptual-model-todo-app.md
```

## Error Handling

- **No conceptual model**: Guide to `/concept.init`
- **Object already exists**: Offer to update or rename
- **No object name provided**: Ask for object name
- **Invalid object name**: Suggest proper naming (PascalCase, no spaces)

## Best Practices

### ✅ Good Mental Models

- "A chunk of my time dedicated to something" (Event)
- "Something I need to do" (Task)
- "Things I'm planning to buy" (Shopping Cart)
- "A collection of my saved recipes" (Recipe Book)

### ❌ Avoid Technical Descriptions

- "A database record with time attributes"
- "A boolean status flag with metadata"
- "A session-scoped collection object"
- "An ORM model with foreign keys"

### Good Action Descriptions

- ✅ "Mark as done" (user language)
- ❌ "Update status boolean to true" (technical)

- ✅ "Add to cart" (user language)
- ❌ "Append item to session array" (technical)

## Reference

- See `examples/` for complete object definitions
- Check `templates/components/object-card.md` for template structure
- Read `conceptual-modeling.md` section on "Objects and Attributes"
