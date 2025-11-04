# Quick Start Guide

## Complete Example: Creating a Recipe App Model

This guide walks through creating a complete conceptual model from scratch.

### Step 1: Initialize

```bash
claude-code "concept init RecipeApp"
```

You'll be asked:
- **Purpose:** "Help users discover, save, and share recipes"
- **Target users:** "Home cooks who want to organize their recipes"
- **Main objects:** "Recipe, User, Ingredient, Collection"

**Result:** Creates `docs/conceptual-model-recipe-app.md` with initial structure.

---

### Step 2: Define Core Objects

#### Add Recipe Object

```bash
claude-code "concept add-object Recipe"
```

**Form responses:**
- **Mental model:** "A set of instructions to make a dish"
- **Visible attributes:** "title, ingredients, steps, prep time, servings, photos"
- **Actions:** "view, save, share, rate, edit, delete"

---

#### Add User Object

```bash
claude-code "concept add-object User"
```

**Form responses:**
- **Mental model:** "Someone who saves and creates recipes"
- **Visible attributes:** "name, profile photo, saved recipes, created recipes"
- **Actions:** "create recipe, save recipe, follow others, rate recipes"

---

#### Add Ingredient Object

```bash
claude-code "concept add-object Ingredient"
```

**Form responses:**
- **Mental model:** "Something needed to make a recipe"
- **Visible attributes:** "name, quantity, unit, optional/required"
- **Actions:** "add, remove, substitute, check off"

---

#### Add Collection Object

```bash
claude-code "concept add-object Collection"
```

**Form responses:**
- **Mental model:** "A folder of related recipes"
- **Visible attributes:** "name, description, recipes, cover photo"
- **Actions:** "create, add recipes, share, delete"

---

### Step 3: Map Relationships

#### User → Recipe

```bash
claude-code "concept add-relationship User Recipe"
```

**Form responses:**
- **Type:** One-to-many (1:n)
- **Mental model:** "A user can create many recipes"
- **Example:** "Sarah has 45 recipes in her cookbook"

---

#### Recipe → Ingredient

```bash
claude-code "concept add-relationship Recipe Ingredient"
```

**Form responses:**
- **Type:** Many-to-many (n:n)
- **Mental model:** "Recipes use multiple ingredients, ingredients appear in multiple recipes"
- **Example:** "This pasta recipe needs 5 ingredients"

---

#### User → Collection

```bash
claude-code "concept add-relationship User Collection"
```

**Form responses:**
- **Type:** One-to-many (1:n)
- **Mental model:** "A user can organize recipes into collections"
- **Example:** "Sarah has 3 collections: Desserts, Quick Dinners, Italian"

---

#### Collection → Recipe

```bash
claude-code "concept add-relationship Collection Recipe"
```

**Form responses:**
- **Type:** Many-to-many (n:n)
- **Mental model:** "Collections contain multiple recipes, recipes can be in multiple collections"
- **Example:** "The 'Italian' collection has 12 recipes"

---

### Step 4: Define User Workflows

#### Create Recipe Workflow

```bash
claude-code "concept add-action create-recipe"
```

**Form responses:**
- **Mental model:** "Saving a new recipe to my cookbook"
- **Steps:**
  1. Click "New Recipe" → "I want to add a recipe"
  2. Enter title → "Give it a name"
  3. Add ingredients → "List what I need"
  4. Add cooking steps → "Explain how to make it"
  5. Upload photo → "Show how it looks"
  6. Set prep time & servings → "How long and how much"
  7. Save → "Add to my cookbook"
- **Objects involved:** Recipe, Ingredient, User

---

#### Save Recipe Workflow

```bash
claude-code "concept add-action save-recipe"
```

**Form responses:**
- **Mental model:** "Bookmarking a recipe I want to try"
- **Steps:**
  1. Browse recipes → "Looking for ideas"
  2. Find interesting recipe → "This looks good"
  3. Click save/bookmark → "Remember this for later"
  4. Optionally add to collection → "Organize it"
  5. See confirmation → "Got it saved"
- **Objects involved:** Recipe, User, Collection

---

#### Search Recipes Workflow

```bash
claude-code "concept add-action search-recipes"
```

**Form responses:**
- **Mental model:** "Finding recipes I'm in the mood for"
- **Steps:**
  1. Enter search term → "What do I want to make?"
  2. Filter by criteria → "Any dietary restrictions?"
  3. Browse results → "See what matches"
  4. Click recipe → "Tell me more"
  5. Decide: save or skip → "Keep or move on"
- **Objects involved:** Recipe, Ingredient (filters), User

---

### Step 5: Review Progress

```bash
claude-code "concept review"
```

**Sample output:**

```
╔═══════════════════════════════════════╗
║  Conceptual Model Review              ║
╟───────────────────────────────────────╢
║ Model: RecipeApp                      ║
╠═══════════════════════════════════════╣
║ Completeness                          ║
╟───────────────────────────────────────╢
║ ✅ Central metaphor defined           ║
║ ✅ 4 objects defined                  ║
║ ✅ All object attributes complete     ║
║ ✅ 4 relationships mapped             ║
║ ✅ 3 user workflows defined           ║
║ ⚠️  Missing error handling section    ║
║ ⚠️  No platform adaptations yet       ║
╟───────────────────────────────────────╢
║ Progress: ██████████████░░ 75%        ║
╠═══════════════════════════════════════╣
║ Suggestions                           ║
╟───────────────────────────────────────╢
║ 1. Add error handling scenarios       ║
║ 2. Define mobile vs desktop UX        ║
║ 3. Add state model for recipes        ║
╚═══════════════════════════════════════╝

Next recommended command:
→ Add error handling scenarios

Want me to help with any of these? (yes)
```

---

### Step 6: Check Status Anytime

```bash
claude-code "concept status"
```

**Sample output:**

```
Current Model: RecipeApp
──────────────────────────────────────
📦 Objects: 4 (User, Recipe, Ingredient, Collection)
🔗 Relationships: 4 mapped
⚡ Workflows: 3 defined
📊 Completeness: ~75%

Missing:
• Error handling scenarios
• Platform-specific adaptations
• State model

Next suggested step:
→ concept add-action rate-recipe
```

---

### Step 7: Generate Final Document

```bash
claude-code "concept generate"
```

**Output:**

```
✅ Generated final conceptual model

Files created:
📄 docs/conceptual-model-recipe-app-final.md
📄 docs/conceptual-model-recipe-app.pdf

Model Statistics:
─────────────────
• Objects: 4
• Relationships: 4
• Workflows: 3
• Sections: 15
• Completeness: 75%

Ready for review and sharing!
```

---

## What You Get

### Generated Document Includes:

1. **Executive Summary**
   - Purpose and scope
   - Key stakeholders
   - Object overview

2. **Core Conceptual Model**
   - Central metaphor: "Your digital cookbook"
   - Mental model hierarchy
   - Key principles

3. **Object Model**
   - Recipe (detailed definition)
   - User (detailed definition)
   - Ingredient (detailed definition)
   - Collection (detailed definition)

4. **Relationships & Rules**
   - Visual diagrams (ASCII art)
   - User mental models
   - System constraints

5. **User Actions & Workflows**
   - Create recipe flow
   - Save recipe flow
   - Search recipes flow

6. **Additional Sections**
   - Information architecture
   - State models
   - Error handling
   - Design principles
   - Validation tests

---

## Next Steps

### Share with Team

```bash
# Send to stakeholders
# Add to design docs
# Use in user research
```

### Iterate Based on Feedback

```bash
# Add missing objects
claude-code "concept add-object Meal Plan"

# Add missing relationships
claude-code "concept add-relationship User Meal Plan"

# Add more workflows
claude-code "concept add-action plan-week"

# Re-generate
claude-code "concept generate"
```

### Keep Updated

```bash
# Review quarterly
claude-code "concept review"

# Update as features change
# Version in git
# Reference in PRDs
```

---

## Tips for RecipeApp Specifically

### Good Mental Models for Recipes

✅ **Good:**
- "A recipe is instructions to make a dish"
- "Saving a recipe is like bookmarking it"
- "Collections are like recipe folders"
- "Rating is sharing my experience"

❌ **Avoid:**
- "A recipe is a database entry with fields"
- "Saving updates a many-to-many relation"
- "Collections are category taxonomies"
- "Rating is a numeric value with user_id"

### User Language

✅ **Use:**
- "My cookbook"
- "Save recipe"
- "Make this"
- "Add to favorites"

❌ **Avoid:**
- "Recipe database"
- "Persist entity"
- "Execute query"
- "Update relation"

---

## Try It Yourself

```bash
# Start your own model now!
claude-code "concept init YourApp"
```

Reference this guide anytime you need help with the workflow.
