# /concept.init

Initialize a new conceptual model for an application.

## Purpose

Start a new conceptual model document based on Johnson & Henderson's Conceptual Models Framework. This creates a structured document that captures how users think about and interact with your application.

## Usage

```
/concept.init <app-name>
```

## Workflow

When this command is executed, follow these steps:

### 1. Gather Initial Information

Use the AskUserQuestion tool to collect:

**Question 1: Application Purpose**
- Header: "Purpose"
- Question: "What is the main purpose of this application?"
- Options:
  - Productivity (Help users get things done)
  - Social (Connect people)
  - E-commerce (Buy/sell products)
  - Content (Create/consume content)
  - Collaboration (Work together)
  - Education (Learn/teach)

**Question 2: Primary Users**
- Header: "Users"
- Question: "Who are the primary users?" (multiSelect: true)
- Options:
  - General consumers (Everyday people)
  - Professionals (Work/business context)
  - Creators (Content makers)
  - Administrators (Manage systems)
  - Students (Learning context)
  - Teams (Collaborative groups)

After gathering structured inputs, ask for text inputs:
- Application name (pre-filled with <app-name>)
- Brief description (1-2 sentences)
- Initial 3-5 main objects users will interact with (comma-separated)

### 2. Create Conceptual Model File

**File location:** `docs/conceptual-model-<app-name-kebab-case>.md`

Use the template from `templates/base-model.md` as the foundation.

### 3. Fill Executive Summary

Populate the Executive Summary section with:
- Application name
- Purpose statement
- Target users
- Initial objects (as a list)
- Creation date
- Version (1.0.0)

### 4. Initialize Core Sections

Create placeholder sections for:
- Core Conceptual Model (add central metaphor placeholder)
- Object Model (list initial objects to be defined)
- Relationships & Rules (empty, to be filled)
- User Actions & Workflows (empty, to be filled)

### 5. Confirm Creation

Display a success message:

```
✅ Created conceptual model for <AppName>

📄 File: docs/conceptual-model-<app-name>.md

📦 Initial objects to define:
   • <Object1>
   • <Object2>
   • <Object3>

Next steps:
→ Define objects: /concept.add-object <object-name>
→ Check status: /concept.status
→ Review examples: Check examples/ directory

Happy modeling! 🎨🧠
```

## Important Guidelines

1. **File Naming**: Always use kebab-case for filenames (e.g., `recipe-app`, not `RecipeApp`)
2. **User-Centric Language**: Use how users think, not technical terms
3. **Template Structure**: Maintain all 15 sections from the base template
4. **Validation**: Ensure the docs/ directory exists, create if needed
5. **No Overwrite**: If file exists, ask user if they want to overwrite or create a new version

## Examples

### Example 1: Simple Todo App

```
User: /concept.init todo-app

Questions answered:
- Purpose: Productivity
- Users: General consumers
- Description: "A simple app to track tasks and to-do items"
- Initial objects: Task, List, User

Result: Creates docs/conceptual-model-todo-app.md
```

### Example 2: Recipe App

```
User: /concept.init RecipeBook

Questions answered:
- Purpose: Content
- Users: General consumers, Creators
- Description: "A platform to save, organize, and share recipes"
- Initial objects: Recipe, User, Ingredient, Collection

Result: Creates docs/conceptual-model-recipe-book.md
```

## Error Handling

- **No app name provided**: Ask user for application name
- **File already exists**: Confirm overwrite or suggest versioning
- **No templates/ directory**: Show error and suggest running conceptual init first
- **Invalid characters in name**: Sanitize to kebab-case automatically

## Reference

- See `examples/` directory for complete conceptual models
- Read `conceptual-modeling.md` for theoretical foundation
- Check `templates/base-model.md` for full document structure
