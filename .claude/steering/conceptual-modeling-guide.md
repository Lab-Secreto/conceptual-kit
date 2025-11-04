# Conceptual Modeling Guide

This guide provides the theoretical foundation and best practices for creating user-centric conceptual models.

## What is a Conceptual Model?

A conceptual model is a high-level description of how users think about and understand a system. It's **not** about technical implementation—it's about the **mental models** users form when interacting with your application.

### Key Principle

> "Design what users think they're using, not what the system actually does."
> — Johnson & Henderson (1991)

## Why Conceptual Models Matter

1. **Align Teams**: Everyone shares the same understanding of how users think
2. **Design Consistently**: Features feel cohesive because they follow the same mental model
3. **Onboard Faster**: New team members quickly grasp user perspectives
4. **Build Better UX**: Start from user expectations, not technical constraints
5. **Guide Development**: User-centric principles inform technical decisions

## Core Components

### 1. Objects

**What are objects?**
Objects are the "things" users think about and interact with in your application.

**Good object definitions:**
- ✅ "A recipe is instructions for making a dish" (user perspective)
- ✅ "A task is something I need to do" (mental model)
- ✅ "A shopping cart is where I keep items I want to buy" (metaphor)

**Bad object definitions:**
- ❌ "A recipe is a database record with fields" (technical)
- ❌ "A task has a boolean completion status" (implementation)
- ❌ "A cart is a session array" (system architecture)

**Object attributes:**
Focus on what users **see and care about**, not internal data:
- ✅ Title, description, photo, date, author
- ❌ UUID, created_at timestamp, foreign keys

### 2. Relationships

**What are relationships?**
How objects connect in the user's mind.

**Express relationships in user language:**
- ✅ "A user has many recipes they've saved"
- ✅ "Each recipe uses several ingredients"
- ✅ "Tasks are organized into projects"

**Not in technical terms:**
- ❌ "User table has one-to-many with Recipe via user_id"
- ❌ "Recipe_Ingredient junction table for many-to-many"

**Cardinality matters to users:**
- **1:1** - "Each user has one profile"
- **1:n** - "A user can save many recipes"
- **n:n** - "Recipes can have multiple tags, tags apply to multiple recipes"

### 3. Actions & Workflows

**What are workflows?**
Step-by-step descriptions of what users **think** as they accomplish tasks.

**Good workflow steps:**
```markdown
1. Click "Add Recipe"
   - User thinks: "I want to save a new recipe"
   - Objects: UI, Recipe

2. Enter title
   - User thinks: "Give it a name I'll remember"
   - Objects: Recipe

3. Add ingredients
   - User thinks: "List what I need"
   - Objects: Recipe, Ingredients
```

**Bad workflow steps:**
```markdown
1. POST request to /api/recipes
2. Validate input schema
3. Insert into database
```

The first describes **user mental models**. The second describes **system operations**.

### 4. Mental Models vs. System Models

| User's Mental Model | System's Actual Model |
|---------------------|----------------------|
| "My recipes" | Database records filtered by user_id |
| "Saving a recipe" | INSERT INTO recipes... |
| "My shopping cart" | Session cookie with product IDs |
| "Deleting a post" | Soft delete, set deleted_at |

**Design for the mental model, then implement the system model.**

## Methodology

### Step 1: Identify Core Objects

Ask: "What are the main **things** users think about?"

For a recipe app:
- Recipe
- Ingredient
- User
- Collection

Not:
- API endpoints
- Database tables
- Microservices

### Step 2: Define Mental Models

For each object, write: **"What users think it is"**

Example:
```markdown
### Recipe

**What users think it is:**
"A set of instructions to make a dish I want to cook"

Not: "A JSON document with preparation metadata"
```

### Step 3: Map Relationships

How do objects connect **in users' minds**?

```
User "has" Recipes (ownership)
Recipe "uses" Ingredients (composition)
Recipe "belongs to" Collections (organization)
```

### Step 4: Document Workflows

Capture **mental journey**, not technical flow.

Ask at each step:
- What is the user **doing**?
- What are they **thinking**?
- What **confirms** it worked?

### Step 5: Validate with Users

Test your model:
- Does this language match how users talk?
- Would users understand these descriptions?
- Are we using metaphors users recognize?

## Best Practices

### ✅ Use User Language

**Good:**
- "Mark it done"
- "Save for later"
- "Add to my collection"
- "Check it off"

**Bad:**
- "Update completion boolean"
- "Persist to favorites table"
- "Append to user collection array"
- "Set status = completed"

### ✅ Focus on What, Not How

**Good:**
- What: "User can favorite a recipe"
- Mental model: "Save it so I can find it easily later"

**Bad:**
- How: "User_favorites junction table with foreign keys"
- Implementation: "AJAX call to POST /api/favorites"

### ✅ Include Real Examples

**Good:**
```markdown
"Sarah has 127 recipes in her cookbook. She organized them into 5 collections:
Breakfast, Desserts, Quick Meals, Vegetarian, and Holiday Favorites."
```

**Bad:**
```markdown
"Users can create collections. Recipes can be in multiple collections."
```

The first is concrete and relatable. The second is abstract.

### ✅ Think in Metaphors

Good conceptual models use **familiar metaphors**:

- **Desktop metaphor**: Files, folders, trash
- **Library metaphor**: Books, shelves, collections
- **Shopping metaphor**: Cart, checkout, receipt
- **Social metaphor**: Friends, feed, posts

### ❌ Avoid Technical Jargon

Don't write:
- "OAuth2 authentication flow"
- "RESTful API endpoints"
- "Normalized database schema"
- "Polymorphic associations"

Instead write:
- "How users sign in"
- "Actions users can perform"
- "How information is organized"
- "How objects relate to each other"

## Common Patterns

### Pattern: Ownership
```
User owns/has Posts
User owns/has Tasks
User owns/has Recipes
```

### Pattern: Hierarchy
```
Folder contains Files
Project contains Tasks
Album contains Photos
```

### Pattern: Association
```
Post references Tags
Recipe uses Ingredients
Task links to Project
```

### Pattern: State Transitions
```
Task: Open → In Progress → Completed
Post: Draft → Published → Archived
Order: Cart → Checkout → Confirmed → Shipped
```

## Section-by-Section Guide

### 1. Executive Summary
- App name, purpose, users
- 2-3 sentence overview
- Initial objects list

### 2. Core Conceptual Model
- Central metaphor (e.g., "A personal cookbook")
- 3-5 key principles
- Overall mental model

### 3. Object Model
- Each object gets a card
- Mental model description
- Visible attributes
- Actions users perform
- States (if applicable)

### 4. Relationships & Rules
- How objects connect
- Cardinality (1:1, 1:n, n:n)
- User language descriptions
- Relationship diagram (ASCII)

### 5. User Actions & Workflows
- Key user tasks
- Step-by-step mental journey
- Objects involved
- Success criteria

### 6-15. Supporting Sections
- Information architecture
- State models
- Error handling
- Design principles
- Platform adaptations
- Implementation notes
- Validation approach

## Quality Checklist

**Mental Model Clarity:**
- [ ] Each object has "what users think it is" description
- [ ] Relationships use user language, not technical terms
- [ ] Workflows include mental models at each step
- [ ] Real-world examples throughout

**User-Centric Language:**
- [ ] No database terminology
- [ ] No API/technical implementation details
- [ ] Using verbs users would use
- [ ] Descriptions users would understand

**Completeness:**
- [ ] 3+ core objects defined
- [ ] Key relationships mapped
- [ ] 2-3 primary workflows documented
- [ ] States and errors considered

**Consistency:**
- [ ] Same metaphor throughout
- [ ] Consistent terminology
- [ ] Parallel structure in descriptions

## Examples to Study

### Simple: Todo App
- Objects: Task, List, User
- Metaphor: "Checklist"
- See: `examples/todo-app/`

### Medium: E-Commerce
- Objects: Product, Cart, Order, User
- Metaphor: "Shopping at a store"
- See: `examples/e-commerce/`

### Complex: Google Calendar
- Objects: Event, Calendar, Reminder, Guest
- Metaphor: "Personal schedule book"
- See: `examples/google-calendar/`

## References

### Foundational Papers
- **Johnson, J., & Henderson, A. (1991)** - "Conceptual Models: Begin by Designing What to Design"
- **Norman, D. (2013)** - "The Design of Everyday Things"
- **Nielsen, J. (2010)** - "Mental Models"

### Related Frameworks
- **Jobs to Be Done** - User motivations
- **User Story Mapping** - User journeys
- **Domain-Driven Design** - Ubiquitous language

### Tools
- **Conceptual Kit** - This framework
- **C4 Model** - Technical architecture diagrams
- **User Flow Diagrams** - Visual workflows

---

## Quick Reference

**Remember:**
1. Design what users **think**, not what systems **do**
2. Use **user language**, not technical jargon
3. Focus on **mental models**, not implementation
4. Include **real examples** to make it concrete
5. **Validate** with actual users

**When in doubt, ask:**
- Would a user understand this description?
- Is this how users talk about it?
- Am I describing the user's perspective or the system's?

---

*For more guidance, see examples in `examples/` directory and command references in `.claude/commands/`.*
