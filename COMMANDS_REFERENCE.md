# Commands Reference

Quick reference for all Conceptual Model Kit commands.

## Command Syntax

```bash
claude-code "concept <command> [arguments]"
```

---

## Commands Overview

| Command | Purpose | Arguments | Example |
|---------|---------|-----------|---------|
| `init` | Start new model | `<app-name>` | `concept init RecipeApp` |
| `add-object` | Add object | `<object-name>` | `concept add-object Recipe` |
| `add-relationship` | Map relationship | `<from> <to>` | `concept add-relationship User Recipe` |
| `add-action` | Add workflow | `<action-name>` | `concept add-action create-recipe` |
| `review` | Review model | none | `concept review` |
| `generate` | Generate final doc | none | `concept generate` |
| `status` | Quick overview | none | `concept status` |

---

## Detailed Command Reference

### `concept init <app-name>`

**Purpose:** Initialize a new conceptual model

**What it does:**
- Creates `docs/conceptual-model-<app-name>.md`
- Prompts for application details via form
- Sets up document structure
- Initializes executive summary

**Form fields:**
- Application name
- Purpose/description
- Target users
- Initial objects (3-5)

**Example:**
```bash
claude-code "concept init RecipeApp"
```

**Output file:** `docs/conceptual-model-recipe-app.md`

---

### `concept add-object <object-name>`

**Purpose:** Add a new object to the model

**What it does:**
- Prompts for object definition via form
- Adds to "Object Model" section
- Updates hierarchy diagram
- Saves document

**Form fields:**
- Mental model (what users think it is)
- Visible attributes (comma-separated)
- Actions users can perform
- Object states (optional)

**Example:**
```bash
claude-code "concept add-object Recipe"
```

**Best practices:**
- Use PascalCase for object names (Recipe, not recipe)
- Focus on user perspective
- List 5-10 attributes
- Include 5-10 actions

---

### `concept add-relationship <from-object> <to-object>`

**Purpose:** Define relationship between two objects

**What it does:**
- Validates both objects exist
- Prompts for relationship details via form
- Adds to "Relationships & Rules" section
- Updates relationship diagram
- Saves document

**Form fields:**
- Cardinality (1:1, 1:n, n:n)
- User mental model phrase
- Example usage

**Example:**
```bash
claude-code "concept add-relationship User Recipe"
```

**Cardinality options:**
- **1:1** (one-to-one): Each A has exactly one B
- **1:n** (one-to-many): Each A has multiple Bs
- **n:n** (many-to-many): Multiple As, multiple Bs

**Best practices:**
- Use user language: "A user has many recipes"
- Avoid technical terms: "user_id foreign key to recipes table"

---

### `concept add-action <action-name>`

**Purpose:** Document a user workflow

**What it does:**
- Prompts for workflow details via form
- Adds to "User Actions & Workflows" section
- Saves document

**Form fields:**
- User mental model (what they think they're doing)
- Sequential steps
- User thoughts at each step
- Objects involved

**Example:**
```bash
claude-code "concept add-action create-recipe"
```

**Best practices:**
- Use kebab-case for action names
- Include 4-8 steps
- Add user thoughts in quotes: "I want to save this"
- Reference objects used

---

### `concept review`

**Purpose:** Review model completeness and get suggestions

**What it does:**
- Analyzes current model
- Checks all sections
- Calculates completion percentage
- Provides specific suggestions
- Offers to help with gaps

**No arguments needed**

**Example:**
```bash
claude-code "concept review"
```

**Output includes:**
- ✅ Completed items
- ❌ Missing items
- ⚠️  Partial items
- Progress percentage
- Prioritized suggestions
- Next recommended command

---

### `concept generate`

**Purpose:** Generate final formatted document

**What it does:**
- Validates model completeness (>50%)
- Fills template with all data
- Formats ASCII diagrams
- Generates table of contents
- Adds metadata (date, version)
- Creates markdown file
- Optionally creates PDF (if pandoc available)

**No arguments needed**

**Example:**
```bash
claude-code "concept generate"
```

**Output files:**
- `docs/conceptual-model-<name>-final.md` (always)
- `docs/conceptual-model-<name>.pdf` (if pandoc installed)

**Requirements for PDF:**
```bash
# Install pandoc
brew install pandoc  # macOS
```

---

### `concept status`

**Purpose:** Quick overview of model state

**What it does:**
- Counts objects
- Counts relationships
- Counts workflows
- Calculates completeness
- Suggests next step

**No arguments needed**

**Example:**
```bash
claude-code "concept status"
```

**Output:**
```
Current Model: RecipeApp
──────────────────────────────────────
📦 Objects: 3
🔗 Relationships: 2
⚡ Workflows: 1
📊 Completeness: ~60%
```

---

## Workflow Examples

### Basic Workflow (Minimum Viable Model)

```bash
# 1. Initialize
claude-code "concept init MyApp"

# 2. Add core objects (3-5)
claude-code "concept add-object User"
claude-code "concept add-object Content"
claude-code "concept add-object Comment"

# 3. Map key relationships (2-3)
claude-code "concept add-relationship User Content"
claude-code "concept add-relationship Content Comment"

# 4. Add primary workflow (1-2)
claude-code "concept add-action create-content"

# 5. Generate
claude-code "concept generate"
```

**Result:** ~60% complete model, ready for review

---

### Complete Workflow (Comprehensive Model)

```bash
# 1. Initialize
claude-code "concept init MyApp"

# 2. Add all objects (5-10)
claude-code "concept add-object User"
claude-code "concept add-object Content"
claude-code "concept add-object Comment"
claude-code "concept add-object Category"
claude-code "concept add-object Tag"

# 3. Map all relationships (5-8)
claude-code "concept add-relationship User Content"
claude-code "concept add-relationship Content Comment"
claude-code "concept add-relationship User Comment"
claude-code "concept add-relationship Content Category"
claude-code "concept add-relationship Content Tag"

# 4. Add all workflows (3-5)
claude-code "concept add-action create-content"
claude-code "concept add-action add-comment"
claude-code "concept add-action search-content"
claude-code "concept add-action organize-by-category"

# 5. Review
claude-code "concept review"

# 6. Fill gaps based on review
# (add missing items)

# 7. Generate
claude-code "concept generate"
```

**Result:** 80-90% complete model, comprehensive

---

### Iterative Workflow (Build Over Time)

```bash
# Week 1: Core objects
claude-code "concept init MyApp"
claude-code "concept add-object User"
claude-code "concept add-object Content"
claude-code "concept status"

# Week 2: Relationships
claude-code "concept add-relationship User Content"
claude-code "concept status"

# Week 3: Workflows
claude-code "concept add-action create-content"
claude-code "concept review"

# Week 4: Polish
# (fill gaps from review)
claude-code "concept generate"
```

**Result:** Gradual build-up, less overwhelming

---

## Form Response Tips

### For Objects (add-object)

**Mental Model:**
- ✅ "A collection of saved articles"
- ❌ "A many-to-many relational table"

**Attributes:**
- ✅ "title, author, date, content, tags"
- ❌ "id, user_id, created_at, updated_at"

**Actions:**
- ✅ "save, share, edit, delete"
- ❌ "INSERT, UPDATE, DELETE"

---

### For Relationships (add-relationship)

**Type Selection:**
- One-to-one: "Each user has one profile"
- One-to-many: "Each user has many posts"
- Many-to-many: "Users can follow many users"

**Mental Model:**
- ✅ "A user can save many articles"
- ❌ "user_id foreign key in articles table"

---

### For Workflows (add-action)

**Mental Model:**
- ✅ "Saving an article to read later"
- ❌ "Creating a bookmark record"

**Steps:**
- ✅ Include user thoughts: Click save → "Keep for later"
- ❌ Technical steps: "Execute INSERT query"

---

## Common Patterns

### E-Commerce Pattern
```bash
model add-object Product
model add-object Cart
model add-object Order
model add-relationship User Cart
model add-relationship Cart Product
model add-relationship User Order
model add-action add-to-cart
model add-action checkout
```

### Social Media Pattern
```bash
model add-object User
model add-object Post
model add-object Comment
model add-object Like
model add-relationship User Post
model add-relationship Post Comment
model add-relationship User Like
model add-action create-post
model add-action add-comment
```

### Content Management Pattern
```bash
model add-object User
model add-object Article
model add-object Category
model add-object Tag
model add-relationship User Article
model add-relationship Article Category
model add-relationship Article Tag
model add-action publish-article
model add-action organize-content
```

---

## Keyboard-Friendly Commands

For faster workflow, create aliases:

```bash
# In your shell config (.bashrc, .zshrc)
alias mi='claude-code "concept init'
alias mo='claude-code "concept add-object'
alias mr='claude-code "concept add-relationship'
alias ma='claude-code "concept add-action'
alias ms='claude-code "concept status"'
alias mrev='claude-code "concept review"'
alias mgen='claude-code "concept generate"'
```

**Usage:**
```bash
mi RecipeApp"
mo Recipe"
mo User"
mr User Recipe"
ms
```

---

## Troubleshooting

### "Object doesn't exist"
**Problem:** Trying to create relationship before objects defined
**Solution:** Create both objects first with `add-object`

### "Model not found"
**Problem:** No model initialized
**Solution:** Run `concept init <name>` first

### "Can't generate - model incomplete"
**Problem:** Model is less than 30% complete
**Solution:** Add more objects and workflows, or confirm to generate anyway

### "PDF not generated"
**Problem:** Pandoc not installed
**Solution:** `brew install pandoc` (macOS) or skip PDF generation

---

## See Also

- [README.md](README.md) - Full documentation
- [QUICK_START.md](QUICK_START.md) - Complete example walkthrough
- [examples/](examples/) - Real-world examples
- [templates/](templates/) - Templates reference

---

**Quick help anytime:**
```bash
claude-code "help with conceptual model commands"
```
