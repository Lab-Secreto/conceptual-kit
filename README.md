# Conceptual Model Kit

A framework for creating comprehensive conceptual models for applications, based on **Johnson & Henderson's Conceptual Models Framework**. Inspired by [GitHub Spec Kit](https://github.com/github/spec-kit).

## What is this?

The Conceptual Model Kit helps you document how users think about and interact with your application. Instead of focusing on technical implementation, it captures the **mental models** users form when using your product.

### Why use it?

- **Align teams** around how users think, not just what features do
- **Design consistently** by understanding user expectations
- **Onboard faster** with clear mental model documentation
- **Build better UX** by starting from user perspective
- **Guide development** with user-centric principles

## Quick Start

### Installation

Install the Conceptual Kit CLI tool using `uv` (recommended):

```bash
# Using uv (recommended)
uv tool install conceptual-kit --from git+https://github.com/Lab-Secreto/conceptual-kit.git

# Or using pip
pip install git+https://github.com/Lab-Secreto/conceptual-kit.git
```

### Initialize a Project

```bash
# Basic project initialization
conceptual init my-project

# Initialize with specific AI assistant
conceptual init my-project --ai claude

# Initialize in current directory
conceptual init . --ai claude
# or use the --here flag
conceptual init --here --ai claude

# Force merge into current (non-empty) directory without confirmation
conceptual init . --force --ai claude

# Skip git initialization
conceptual init my-project --no-git

# Check system requirements
conceptual check
```

### What Gets Installed

When you run `conceptual init`, the following structure is created:

```
my-project/
├── .claude/
│   ├── commands/              # 7 slash commands for Claude Code
│   │   ├── concept-init.md
│   │   ├── concept-add-object.md
│   │   ├── concept-add-relationship.md
│   │   ├── concept-add-action.md
│   │   ├── concept-review.md
│   │   ├── concept-generate.md
│   │   └── concept-status.md
│   └── steering/
│       └── conceptual-modeling-guide.md
├── .github/
│   └── copilot-instructions.md  # For GitHub Copilot compatibility
├── docs/                         # Your conceptual models go here
├── examples/                     # Reference models
├── templates/                    # Document templates
└── README.md                     # Getting started guide
```

### Your First Conceptual Model

After initialization, open your project in Claude Code and use the slash commands:

```bash
# 1. Navigate to your project
cd my-project

# 2. Open Claude Code
claude

# 3. Inside Claude Code, use slash commands:

# Initialize a new model
/concept.init MyApp

# Add your core objects
/concept.add-object User
/concept.add-object Post
/concept.add-object Comment

# Map relationships
/concept.add-relationship User Post
/concept.add-relationship Post Comment

# Add user workflows
/concept.add-action create-post
/concept.add-action add-comment

# Review completeness
/concept.review

# Generate final document
/concept.generate
```

**Important:** The commands are **slash commands** (e.g., `/concept.init`) that you use **inside Claude Code**, not CLI commands.

## Available Slash Commands

All commands below are **slash commands** to use inside Claude Code after running `conceptual init`.

### `/concept.init <app-name>`

Start a new conceptual model. You'll be guided through:
- Application purpose
- Target users
- Initial objects

**Example:**
```
/concept.init RecipeApp
```

Creates: `docs/conceptual-model-recipe-app.md`

---

### `/concept.add-object <object-name>`

Add a new object to your model. Define:
- What users think it is (mental model)
- Visible attributes
- Actions users can perform
- Object states

**Example:**
```
/concept.add-object Recipe
```

---

### `/concept.add-relationship <from> <to>`

Map relationships between objects:
- Type (1:1, 1:n, n:n)
- User's mental model of the relationship
- Real-world examples

**Example:**
```
/concept.add-relationship User Recipe
```

---

### `/concept.add-action <action-name>`

Document user workflows:
- User's mental model of the action
- Step-by-step flow
- Objects involved

**Example:**
```
/concept.add-action create-recipe
```

---

### `/concept.review`

Get a comprehensive review of your model:
- Completeness checklist
- Suggestions for improvements
- Progress percentage
- Next recommended steps

**Example:**
```
/concept.review
```

**Output:**
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
║ ❌ Only 1 of 3 relationships mapped   ║
║ ⚠️  Missing user workflows            ║
╟───────────────────────────────────────╢
║ Progress: ████████░░ 65%              ║
╚═══════════════════════════════════════╝
```

---

### `/concept.generate`

Create final formatted document:
- Complete markdown file
- PDF export (if pandoc available)
- Table of contents
- Formatted diagrams

**Example:**
```
/concept.generate
```

Creates:
- `docs/conceptual-model-<name>-final.md`
- `docs/conceptual-model-<name>.pdf` (if pandoc installed)

---

### `/concept.status`

Quick overview of current model state:
- Object count
- Relationship count
- Workflow count
- Completeness percentage
- Next suggested step

**Example:**
```
/concept.status
```

## Examples

The kit includes three complete examples at different complexity levels:

### 1. Google Calendar (Complex)
**Location:** `examples/google-calendar/`

A comprehensive model showing:
- Multiple object types (Events, Calendars, Reminders)
- Complex relationships
- Platform-specific adaptations
- State models
- Error handling

**Best for:** Learning how to model complex applications with many features.

---

### 2. Todo App (Simple)
**Location:** `examples/todo-app/`

A simple, focused model showing:
- Basic objects (Tasks, Lists)
- Simple relationships
- Core workflows
- Clean structure

**Best for:** Understanding the fundamentals and getting started.

---

### 3. E-Commerce (Medium)
**Location:** `examples/e-commerce/`

A balanced model showing:
- Multiple object types (Products, Cart, Orders)
- Various relationships
- User workflows (browse, checkout, track)
- State transitions

**Best for:** Most real-world applications fall in this complexity range.

## Document Structure

Each conceptual model includes:

1. **Executive Summary** - High-level overview
2. **Core Conceptual Model** - Central metaphor and principles
3. **Object Model** - Primary objects users interact with
4. **Relationships & Rules** - How objects connect
5. **User Actions & Workflows** - What users do
6. **Information Architecture** - How information is organized
7. **State Model** - Object states and transitions
8. **Error Handling** - How errors are communicated
9. **Metaphorical Consistency** - Language and terminology
10. **Progressive Disclosure** - Complexity layers
11. **Platform Adaptations** - Desktop, mobile, tablet
12. **Design Principles** - Key decisions from the model
13. **Implementation Notes** - Guidance for designers
14. **Validation & Testing** - How to validate the model
15. **Appendices** - Glossary, related docs, versions

## Best Practices

### Writing Mental Models

✅ **Good:** "What users think it is"
- "A chunk of my time dedicated to something" (Event in Calendar)
- "Something I need to do" (Task in Todo App)
- "Things I'm planning to buy" (Shopping Cart)

❌ **Avoid:** Technical descriptions
- "A database record with time attributes"
- "A boolean status flag with metadata"
- "A session-scoped collection object"

### Using User Language

✅ **Good:**
- "Check it off", "Mark as done"
- "Add to cart", "Checkout"
- "My calendar", "Invite guests"

❌ **Avoid:**
- "Update status boolean to true"
- "Append item to session array"
- "Query calendar entity"

### Creating Workflows

Focus on user thoughts at each step:

```markdown
#### Creating a Recipe

**Mental model:** "Saving a new recipe to my collection"

**Flow:**
1. Click create → "I want to add a recipe"
2. Enter title → "Give it a name"
3. Add ingredients → "List what I need"
4. Add steps → "Explain how to make it"
5. Save → "Keep it for later"
```

## Templates

### Object Card Template
Located at: `templates/components/object-card.md`

Defines structure for each object in your model.

### Workflow Template
Located at: `templates/components/workflow-steps.md`

Defines structure for user action flows.

### Relationship Template
Located at: `templates/components/relationship-diagram.md`

Defines structure for object relationships.

### Base Model Template
Located at: `templates/base-model.md`

Complete document structure with all sections.

## Tips & Tricks

### 1. Start Simple

Don't try to model everything at once:
```bash
# Start with 3-5 core objects
model add-object User
model add-object Content
model add-object Comment
```

### 2. Use Real User Language

Listen to how users describe your app:
- User testing transcripts
- Support tickets
- User interviews
- Online reviews

### 3. Iterate Based on Review

```bash
# Check progress regularly
model review

# Fill in gaps
model add-relationship User Content
model add-action create-content
```

### 4. Reference Examples

Stuck? Look at examples:
- Simple app? → See `examples/todo-app/`
- Complex app? → See `examples/google-calendar/`
- E-commerce? → See `examples/e-commerce/`

### 5. Keep It User-Focused

Ask yourself:
- Would a user understand this description?
- Is this how users actually think about it?
- Am I using technical jargon?

## PDF Generation

To generate PDFs, install pandoc:

```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
```

Then use:
```bash
claude-code "concept generate"
```

Will create both `.md` and `.pdf` files.

## Integration with Development

### Use in Design Reviews

```bash
# Before designing a feature
model review

# Check if mental model supports new feature
# Add new objects/workflows as needed
```

### Use in Documentation

Generated models can be:
- Shared with stakeholders
- Added to design system docs
- Used in onboarding materials
- Referenced in PRD templates

### Use in User Research

- Validate mental models with users
- Test if conceptual model matches reality
- Iterate based on findings

## FAQ

### Q: How is this different from a spec?

**A:** Specs focus on *what* the system does (features, requirements). Conceptual models focus on *how users think* about the system (mental models, metaphors).

### Q: When should I create a conceptual model?

**A:**
- Before starting a new product
- When redesigning an existing product
- When user feedback shows confusion
- When onboarding new team members

### Q: How detailed should it be?

**A:** Aim for 60-80% completeness. The model should:
- Cover all main objects
- Map key relationships
- Document primary workflows
- Define the central metaphor

Perfect is the enemy of good!

### Q: Can I use this for APIs?

**A:** Yes! API conceptual models focus on:
- Resources (objects)
- Endpoints (actions)
- Request/response flow (workflows)
- Developer mental models

### Q: How do I keep it up to date?

**A:**
- Review quarterly or after major features
- Use `concept review` to find gaps
- Version the document (see Appendices)
- Make updates part of design process

## Contributing

This is a framework template. Adapt it to your needs:

- Modify templates in `templates/`
- Adjust commands in `.github/copilot-instructions.md`
- Add your own examples
- Customize for your domain

## Resources

### Theoretical Foundation
- [Johnson & Henderson - Conceptual Models (1991)](https://www.sciencedirect.com/science/article/abs/pii/S0953543805800340)
- Don Norman - "The Design of Everyday Things"
- Jakob Nielsen - Mental Models

### Related Tools
- [GitHub Spec Kit](https://github.com/github/spec-kit) - Inspiration for this kit
- [C4 Model](https://c4model.com/) - Software architecture diagrams
- [User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/) - User-centered planning

## License

MIT License - Feel free to use and adapt for your projects.

---

## What's Next?

```bash
# Try it now!
claude-code "concept init MyApp"
```

Start documenting how users think about your application. Build better products by understanding user mental models.

**Happy modeling!** 🎨🧠
