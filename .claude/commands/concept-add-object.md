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

### 3. Gather Object Definition with AskUserQuestion

**IMPORTANT:** You MUST use the `AskUserQuestion` tool. Do NOT skip this step.

Use AskUserQuestion for structured input:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What category best describes this object from a user's perspective?",
      header: "Category",
      multiSelect: false,
      options: [
        {
          label: "Container",
          description: "Holds other things (Folder, Cart, Playlist, Album)"
        },
        {
          label: "Item",
          description: "A single thing (File, Product, Song, Recipe)"
        },
        {
          label: "Action/Event",
          description: "Something that happens (Task, Meeting, Reminder)"
        },
        {
          label: "Space",
          description: "A place or area (Dashboard, Feed, Timeline)"
        }
      ]
    },
    {
      question: "What visibility level does this object have?",
      header: "Visibility",
      multiSelect: false,
      options: [
        {
          label: "Always visible",
          description: "Users see it all the time (like a dashboard widget)"
        },
        {
          label: "On-demand",
          description: "Users navigate to see it (like viewing a document)"
        },
        {
          label: "Background",
          description: "Hidden but affects the experience (like settings)"
        }
      ]
    }
  ]
})
```

### 4. Deep Dive Conversation

After the form, have a conversation to understand deeply:

**Ask these specific questions:**

1. **"In the user's own words, what is a <ObjectName>?"**
   - Listen for natural language, not technical terms
   - Example: "A recipe is instructions for making something yummy"
   - NOT: "A recipe is a data structure with fields"

2. **"Can you describe a specific example of this object?"**
   - Get concrete details
   - Example: "My grandma's chocolate chip cookie recipe"
   - Use these details in the definition

3. **"What information about this object do users care about?"**
   - These become the visible attributes
   - Focus on what users SEE, not database fields
   - Example: "They want to know: who made it, how long it takes, difficulty level"

4. **"Walk me through what users can DO with this object"**
   - Get the complete list of actions
   - Ask for the sequence: "What's the first thing? Then what?"
   - Example: "First they create it, then add ingredients, then they can share it or print it"

5. **"Does this object change over time? What states does it have?"**
   - Only ask if relevant
   - Example: "A recipe can be 'draft' when they're writing it, then 'published' when they share it"

**Conversational approach:**
```
Claude: "In the user's own words, what is a Recipe?"
User: "It's like a set of instructions for making food"

Claude: "Perfect! Can you give me a specific example? Maybe one you use?"
User: "Sure, like my mom's lasagna recipe - it has the ingredients list and step-by-step instructions"

Claude: "Great! So when users look at a recipe, what information matters to them?"
User: "The title, how many servings, cooking time, difficulty level, and of course the ingredients and steps"

Claude: "And what can users do with a recipe once they have it?"
User: "They can save it, edit it, add notes, share with family, or print it out"

Claude: "Does a recipe have different states? Like draft vs published?"
User: "Yes! Sometimes I'm still working on a recipe, and sometimes it's ready to share"
```

### 5. Synthesize and Confirm

Before creating the object card, show a summary:

```
📋 <ObjectName> Definition

**User's description:** "<what they said>"

**Category:** <Container/Item/Action/Space>

**Concrete example:** <the specific example they gave>

**What users see:**
- <attribute1>
- <attribute2>
- <attribute3>

**What users can do:**
1. <action1>
2. <action2>
3. <action3>

**States:** <if applicable>
- <state1> → <state2> → <state3>

**Real-world comparison:** "<metaphor or comparison>"
```

Ask: **"Does this capture the essence of <ObjectName>? Anything to add or clarify?"**

Wait for confirmation.

### 6. Create Rich Object Card

Use the template from `templates/components/object-card.md` to create a DETAILED card:

```markdown
### <ObjectName>

**What users think it is:**
"<mental-model-description in user's exact words>"

**Mental model category:** <category>

**Concrete example:**
<The specific example user provided - e.g., "Mom's lasagna recipe with handwritten notes">

**Why users care:**
<Explain the value/purpose from user perspective>

#### Visible Attributes

Information users see and care about:

- **<Attribute1>**: <Why it matters to users>
  *Example:* "<Concrete example from conversation>"

- **<Attribute2>**: <Why it matters to users>
  *Example:* "<Concrete example from conversation>"

- **<Attribute3>**: <Why it matters to users>
  *Example:* "<Concrete example from conversation>"

#### Actions Users Can Perform

What users can do with this object:

1. **<Action1>**: <What it does>
   - User thinks: "<Mental model of this action>"
   - Triggers when: <Context>

2. **<Action2>**: <What it does>
   - User thinks: "<Mental model of this action>"
   - Triggers when: <Context>

3. **<Action3>**: <What it does>
   - User thinks: "<Mental model of this action>"
   - Triggers when: <Context>

#### Object States

<If the object has states, describe the lifecycle>

```
<State1> ──[action]──> <State2> ──[action]──> <State3>
```

- **<State1>**: <What this means to users>
- **<State2>**: <What this means to users>
- **<State3>**: <What this means to users>

#### User Language Examples

How users talk about this object:

- "<Example phrase 1 from conversation>"
- "<Example phrase 2 from conversation>"
- "<Example phrase 3 from conversation>"

#### Relationships

<To be defined - will be mapped with /concept.add-relationship>

Likely relates to:
- <Related Object 1>
- <Related Object 2>
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
