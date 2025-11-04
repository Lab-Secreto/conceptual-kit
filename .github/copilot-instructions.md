# Conceptual Model Kit - Custom Commands

This project uses the Conceptual Model Kit for creating application conceptual models based on Johnson & Henderson's Conceptual Models Framework.

## Available Commands

### `concept init <app-name>`

**Purpose:** Initialize a new conceptual model for an application.

**Flow:**
1. Use AskUserQuestion tool to gather initial information:
   - Application name (pre-filled with <app-name>)
   - Purpose/description
   - Target users
   - Main objects (3-5 initial objects)
2. Create file: `docs/conceptual-model-<app-name>.md`
3. Use template: `templates/base-model.md`
4. Fill Executive Summary section with gathered info
5. Confirm creation and suggest next step

**Required Information:**
- Application name
- Brief purpose statement
- Who will use it (target users)
- 3-5 main objects users will interact with

**Example Usage:**
```
User: "concept init recipe-app"

Claude Code:
1. Presents AskUserQuestion form with fields
2. Creates docs/conceptual-model-recipe-app.md
3. Confirms: "✅ Created conceptual model for RecipeApp. Ready to add objects with 'concept add-object <name>'"
```

**Important:**
- Always create file in `docs/` directory
- Use kebab-case for filename
- Initialize with template structure
- Add initial objects to pending list if provided

---

### `concept add-object <object-name>`

**Purpose:** Add a new object to the conceptual model.

**Flow:**
1. Read current conceptual model from `docs/` (find most recent or ask which one)
2. Use AskUserQuestion to gather object definition:
   - Object name (pre-filled)
   - Mental model description (what users think it is)
   - Visible attributes (comma-separated)
   - Actions users can perform (list)
   - Possible states (if applicable)
3. Use template: `templates/components/object-card.md`
4. Insert into "3. Object Model" section
5. Update mental model hierarchy diagram (ASCII art)
6. Save file
7. Confirm and suggest next step

**Required Information:**
- What users think this object is (mental model)
- Attributes visible to users
- Actions users can perform on this object

**Example Usage:**
```
User: "concept add-object Recipe"

Claude Code:
1. Presents form asking:
   - "What do users think a Recipe is?"
   - "What attributes can users see?" (title, ingredients, steps, etc)
   - "What actions can users perform?" (create, edit, delete, share, etc)
2. Adds Recipe object to Object Model section
3. Updates hierarchy diagram
4. Confirms: "✅ Added Recipe object. Add another object or map relationships?"
```

**Important:**
- Validate object doesn't already exist
- Use consistent naming (PascalCase for object names)
- Maintain ASCII art hierarchy
- Keep user-centric language

---

### `concept add-relationship <from-object> <to-object>`

**Purpose:** Define a relationship between two objects in the model.

**Flow:**
1. Read current conceptual model
2. Validate both objects exist in the model
3. Use AskUserQuestion to gather relationship details:
   - Relationship type (1:1, 1:n, n:n)
   - How users think of this relationship
   - Bidirectional nature
4. Add to "4. Relationships & Rules" section
5. Update relationship diagram (ASCII art)
6. Save file
7. Confirm and suggest next step

**Required Information:**
- Cardinality (one-to-one, one-to-many, many-to-many)
- User's mental model of the relationship
- Example phrase users would say

**Example Usage:**
```
User: "concept add-relationship User Recipe"

Claude Code:
1. Verifies User and Recipe objects exist
2. Presents form:
   - Type: ( ) 1:1  (•) 1:n  ( ) n:n
   - "How do users think of this?": "A user has many recipes"
3. Updates Relationships section
4. Updates relationship diagram
5. Confirms: "✅ Added User → Recipe (1:n) relationship. Continue mapping relationships?"
```

**Important:**
- Both objects must exist before creating relationship
- Use user language for relationship description
- Update both object relationship diagram and rules section
- Consider bidirectional vs unidirectional

---

### `concept add-action <action-name>`

**Purpose:** Add a user workflow or action flow to the model.

**Flow:**
1. Read current conceptual model
2. Use AskUserQuestion to gather workflow details:
   - Action name (pre-filled)
   - User's mental model of this action
   - Step-by-step flow
   - Objects involved
3. Use template: `templates/sections/workflows.md`
4. Add to "5. User Actions & Workflows" section
5. Save file
6. Confirm and suggest next step

**Required Information:**
- What users think they're doing (mental model)
- Sequential steps in the workflow
- Which objects are involved at each step

**Example Usage:**
```
User: "concept add-action create-recipe"

Claude Code:
1. Presents form:
   - Mental model: "Saving a new recipe to my collection"
   - Steps:
     1. Click create → "I want to add a recipe"
     2. Enter title → "Give it a name"
     3. Add ingredients → "List what I need"
     4. Add steps → "Explain how to make it"
     5. Save → "Keep it for later"
2. Adds to User Actions & Workflows section
3. Confirms: "✅ Added 'Create Recipe' workflow. Add more workflows or review model?"
```

**Important:**
- Use user-centric language for steps
- Include mental model quotes ("what user thinks")
- Reference objects involved
- Keep sequential and clear

---

### `concept review`

**Purpose:** Review the current conceptual model and suggest improvements.

**Flow:**
1. Read current conceptual model from `docs/`
2. Analyze completeness:
   - ✅/❌ Has central metaphor defined?
   - ✅/❌ All objects have attributes?
   - ✅/❌ All objects have actions?
   - ✅/❌ Relationships mapped?
   - ✅/❌ User workflows defined?
   - ✅/❌ Has visual representations?
   - ✅/❌ Error handling covered?
3. Present formatted review with checklist
4. Calculate completeness percentage
5. Suggest specific next steps
6. Offer to help with missing pieces

**Output Format:**
```
╔═══════════════════════════════════════╗
║  Conceptual Model Review              ║
╟───────────────────────────────────────╢
║ Model: RecipeApp                      ║
╠═══════════════════════════════════════╣
║ Completeness                          ║
╟───────────────────────────────────────╢
║ ✅ Central metaphor defined           ║
║ ✅ 3 objects defined                  ║
║ ✅ Object attributes complete         ║
║ ❌ Only 1 of 3 relationships mapped   ║
║ ❌ Missing user workflows             ║
║ ⚠️  No error handling section         ║
╟───────────────────────────────────────╢
║ Progress: ████████░░ 65%              ║
╠═══════════════════════════════════════╣
║ Suggestions                           ║
╟───────────────────────────────────────╢
║ 1. Map User → Recipe relationship     ║
║ 2. Map Recipe → Ingredient relation   ║
║ 3. Add "Create Recipe" workflow       ║
║ 4. Add "Search Recipes" workflow      ║
║ 5. Add error handling section         ║
╚═══════════════════════════════════════╝

Next recommended command:
→ concept add-relationship Recipe Ingredient

Want me to help with any of these? (yes/no)
```

**Important:**
- Be specific in suggestions
- Prioritize by importance
- Reference actual object names from the model
- Offer to execute suggested improvements

---

### `concept generate`

**Purpose:** Generate final formatted conceptual model document.

**Flow:**
1. Read current conceptual model from `docs/`
2. Validate model is reasonably complete (>50%)
3. Use template: `templates/base-model.md`
4. Fill all sections with collected data
5. Format all ASCII diagrams properly
6. Generate table of contents with links
7. Add metadata (date, version)
8. Save as `docs/conceptual-model-<name>-final.md`
9. Check if `pandoc` is available
10. If yes, generate PDF: `docs/conceptual-model-<name>.pdf`
11. Confirm outputs created

**Output:**
```
✅ Generated final conceptual model

Files created:
📄 docs/conceptual-model-recipe-app-final.md
📄 docs/conceptual-model-recipe-app.pdf (pandoc)

Model Statistics:
─────────────────
• Objects: 3
• Relationships: 3
• Workflows: 2
• Pages: 12
• Completeness: 85%

Ready for review and sharing!
```

**Important:**
- Always generate markdown
- PDF is optional (requires pandoc)
- Add generation timestamp
- Keep original working file intact
- Format for readability

---

### `concept status`

**Purpose:** Quick overview of current model state.

**Flow:**
1. Read current conceptual model
2. Count objects, relationships, workflows
3. Calculate completeness percentage
4. Identify what's missing
5. Present compact summary
6. Suggest logical next step

**Output Format:**
```
Current Model: RecipeApp
──────────────────────────────────────
📦 Objects: 3 (User, Recipe, Ingredient)
🔗 Relationships: 2 mapped
⚡ Workflows: 1 defined
📊 Completeness: ~60%

Missing:
• Recipe → Ingredient relationship
• User workflows (search, share, etc)
• Error handling scenarios

Next suggested step:
→ concept add-relationship Recipe Ingredient
```

**Important:**
- Keep output concise
- Show progress clearly
- Be specific about what's missing
- Suggest actionable next step

---

## Form Templates (Using AskUserQuestion)

### Discovery Form (model init)

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What is the main purpose of this application?",
      header: "Purpose",
      options: [
        {label: "Productivity", description: "Help users get things done"},
        {label: "Social", description: "Connect people"},
        {label: "E-commerce", description: "Buy/sell products"},
        {label: "Content", description: "Create/consume content"}
      ],
      multiSelect: false
    },
    {
      question: "Who are the primary users?",
      header: "Users",
      options: [
        {label: "General consumers", description: "Everyday people"},
        {label: "Professionals", description: "Work/business context"},
        {label: "Creators", description: "Content makers"},
        {label: "Administrators", description: "Manage systems"}
      ],
      multiSelect: true
    }
  ]
})
```

Then follow up with text input for:
- Application name
- Brief description
- Initial 3-5 objects

### Object Definition Form (model add-object)

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What do users think this object IS? (mental model)",
      header: "Mental Model",
      options: [
        {label: "Container", description: "Holds other things"},
        {label: "Item", description: "A single thing"},
        {label: "Action", description: "Something that happens"},
        {label: "Space", description: "A place or area"}
      ],
      multiSelect: false
    }
  ]
})
```

Then gather via text:
- Visible attributes (comma-separated)
- Actions users can perform (list)
- States (if applicable)

### Relationship Form (model add-relationship)

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What type of relationship is this?",
      header: "Cardinality",
      options: [
        {label: "One-to-one (1:1)", description: "Each A has exactly one B"},
        {label: "One-to-many (1:n)", description: "Each A has multiple Bs"},
        {label: "Many-to-many (n:n)", description: "Multiple As, multiple Bs"}
      ],
      multiSelect: false
    }
  ]
})
```

Then gather:
- User mental model phrase (e.g., "A user has many recipes")

---

## Important Guidelines

### Always Follow:
1. **User-Centric Language**: Use how users think, not technical terms
2. **Validate Before Acting**: Check objects exist before relationships
3. **Preserve Content**: Never overwrite existing sections
4. **ASCII Diagrams**: Use text-based diagrams for compatibility
5. **Incremental Build**: One step at a time, confirm after each
6. **Reference Examples**: Point to `examples/` for inspiration

### File Naming:
- Working file: `docs/conceptual-model-<app-name>.md`
- Final file: `docs/conceptual-model-<app-name>-final.md`
- PDF: `docs/conceptual-model-<app-name>.pdf`

### Section Order (from template):
1. Executive Summary
2. Core Conceptual Model
3. Object Model
4. Relationships & Rules
5. User Actions & Workflows
6. Information Architecture
7. State Model
8. Error & Exception Handling
9. Metaphorical Consistency
10. Progressive Disclosure Model
11. Platform-Specific Adaptations
12. Design Principles from Model
13. Implementation Notes for Designers
14. Validation & Testing
15. Appendices

### ASCII Diagram Style:
```
User (Owner)
├── Personal Calendar
│   ├── Work Events
│   └── Personal Events
├── Shared Calendars
│   └── Team Calendar
└── Subscriptions
    └── Holidays
```

---

## Examples Reference

Users can reference these complete examples:

- **`examples/google-calendar/`** - Complex application (many objects, relationships)
- **`examples/todo-app/`** - Simple application (good for learning)
- **`examples/e-commerce/`** - Medium complexity (good balance)

---

## Command Workflow Example

```bash
# 1. Initialize
claude-code "concept init CookBook"

# 2. Add core objects
claude-code "concept add-object Recipe"
claude-code "concept add-object User"
claude-code "concept add-object Ingredient"

# 3. Map relationships
claude-code "concept add-relationship User Recipe"
claude-code "concept add-relationship Recipe Ingredient"

# 4. Add workflows
claude-code "concept add-action create-recipe"
claude-code "concept add-action search-recipes"

# 5. Review
claude-code "concept review"

# 6. Generate final
claude-code "concept generate"
```

---

## Technical Notes

### Dependencies:
- `pandoc` (optional) - for PDF generation
- Works with markdown editors that support ASCII art

### File Structure Created:
```
your-project/
├── docs/
│   ├── conceptual-model-<name>.md          # Working file
│   ├── conceptual-model-<name>-final.md    # Generated final
│   └── conceptual-model-<name>.pdf         # PDF (if pandoc available)
```

### Version Control:
- Commit working file regularly
- Final file can be regenerated
- PDF is generated artifact (optional in git)

---

## Error Handling

If user tries to:
- Add relationship before objects exist → Error with helpful message
- Generate before model is >30% complete → Warning, ask to confirm
- Use command without model initialized → Guide to `concept init`

---

## Support

For questions or issues:
- Check `examples/` directory for reference
- See `README.md` for detailed usage guide
- Review `templates/` for structure reference
