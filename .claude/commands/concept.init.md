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

### 1. Gather Initial Information with AskUserQuestion

**IMPORTANT:** You MUST use the `AskUserQuestion` tool to gather information interactively. Do NOT skip this step.

Use the AskUserQuestion tool to collect structured data:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What is the main purpose of this application?",
      header: "Purpose",
      multiSelect: false,
      options: [
        {
          label: "Productivity",
          description: "Help users get things done (tasks, notes, organization)"
        },
        {
          label: "Social",
          description: "Connect people (messaging, profiles, sharing)"
        },
        {
          label: "E-commerce",
          description: "Buy/sell products (shopping, checkout, payments)"
        },
        {
          label: "Content",
          description: "Create/consume content (blog, media, publishing)"
        }
      ]
    },
    {
      question: "Who are the primary users?",
      header: "Users",
      multiSelect: true,
      options: [
        {
          label: "General consumers",
          description: "Everyday people using it personally"
        },
        {
          label: "Professionals",
          description: "People using it for work"
        },
        {
          label: "Creators",
          description: "People making content"
        },
        {
          label: "Teams",
          description: "Groups working together"
        }
      ]
    },
    {
      question: "How complex is the application?",
      header: "Complexity",
      multiSelect: false,
      options: [
        {
          label: "Simple",
          description: "Few features, straightforward flow (like a todo list)"
        },
        {
          label: "Medium",
          description: "Multiple features, some integrations (like a recipe app)"
        },
        {
          label: "Complex",
          description: "Many features, complex workflows (like a project manager)"
        }
      ]
    }
  ]
})
```

### 2. Deep Dive Questions

After the initial questions, engage in a conversation to understand deeply:

**Ask the user to describe in their own words:**

1. **"What problem does this application solve for users?"**
   - Listen for pain points, frustrations, needs
   - Ask follow-up: "Can you give me a specific example?"

2. **"Describe a typical user scenario - what would they do in the app?"**
   - Walk through a complete user journey
   - Identify the key actions and objects

3. **"What are the 3-5 main 'things' users interact with?"**
   - These become your core objects
   - For each one, ask: "What would users call this? What do they think it is?"

4. **"What's the ONE thing users must be able to do in this app?"**
   - Identifies the core workflow
   - Helps establish priority

5. **"Are there any real-world metaphors users would understand?"**
   - E.g., "It's like a digital notebook", "It's like a shopping mall"
   - This becomes the central metaphor

**Example conversation:**
```
Claude: "What problem does this application solve for users?"
User: "People want to save recipes they find online and organize them"

Claude: "Can you give me a specific example of when someone would use this?"
User: "Like when my mom sees a recipe on Instagram, she wants to save it and add her own notes"

Claude: "Great! So what are the main things users interact with? Let me guess - recipes, collections, maybe ingredients?"
User: "Yes! And also the ability to share recipes with family"

Claude: "Perfect. Is there a real-world metaphor that fits? Like a cookbook, recipe box, etc?"
User: "Yes! Like a digital cookbook you can share with family"
```

### 3. Synthesize Information

Before creating the file, summarize what you learned:

```
📋 Summary of <AppName>

**Problem it solves:** <user's explanation>

**Central metaphor:** <the metaphor they mentioned>

**Target users:** <list of user types>

**Core objects identified:**
1. <Object1> - "<what users think it is>"
2. <Object2> - "<what users think it is>"
3. <Object3> - "<what users think it is>"

**Primary workflow:** <the ONE thing users must do>

**Complexity level:** <Simple/Medium/Complex>
```

Show this summary to the user and ask: **"Does this capture your vision? Anything to add or change?"**

Wait for confirmation before proceeding.

### 4. Create Conceptual Model File

**File location:** `docs/conceptual-model-<app-name-kebab-case>.md`

Use the template from `templates/base-model.md` as the foundation.

### 5. Fill Executive Summary with Rich Detail

Populate the Executive Summary section with:

```markdown
# Conceptual Model: <ApplicationName>

**Version:** 1.0.0
**Created:** <current-date>
**Status:** Draft

## Executive Summary

### Application Overview

**<ApplicationName>** is <detailed description based on user's explanation>.

### Problem Statement

Users currently face <problem from conversation>. <AppName> solves this by <solution approach>.

**Example scenario:** <the specific example user mentioned>

### Target Users

Primary users include:
- **<UserType1>**: <description from conversation>
- **<UserType2>**: <description from conversation>

### Central Metaphor

"<The metaphor user described>" - Users think of this application as <expanded metaphor explanation>.

This metaphor guides the entire design:
- <How metaphor influences feature 1>
- <How metaphor influences feature 2>
- <How metaphor influences interaction patterns>

### Core Objects

Users interact with these main objects:

1. **<Object1>**
   *What users think it is:* "<mental model from conversation>"
   *Role:* <purpose in the application>

2. **<Object2>**
   *What users think it is:* "<mental model from conversation>"
   *Role:* <purpose in the application>

3. **<Object3>**
   *What users think it is:* "<mental model from conversation>"
   *Role:* <purpose in the application>

### Primary User Workflow

The core interaction is: <describe the ONE thing workflow in user's words>

This workflow embodies the central metaphor and guides all other features.
```

### 6. Initialize Core Sections

Create detailed starter content for key sections:

**Section 2: Core Conceptual Model**
```markdown
## 2. Core Conceptual Model

### 2.1 Central Metaphor

**Primary Metaphor:** "<The metaphor>"

Users understand <AppName> through the lens of <metaphor explanation>.

**How the metaphor works:**
- <Concrete example 1>
- <Concrete example 2>
- <Concrete example 3>

**Metaphor boundaries:**
What the metaphor includes: <what fits>
What it doesn't include: <what doesn't fit>

### 2.2 Key Principles

Based on the central metaphor, these principles guide design:

1. **<Principle 1>**: <Description tied to user needs>
2. **<Principle 2>**: <Description tied to metaphor>
3. **<Principle 3>**: <Description tied to workflow>
```

**Section 3: Object Model**
```markdown
## 3. Object Model

### Objects to Define

The following objects need detailed definition:

- [ ] <Object1> - Priority: High
- [ ] <Object2> - Priority: High
- [ ] <Object3> - Priority: Medium

Use `/concept.add-object <name>` to define each object.
```

**Section 5: User Actions & Workflows**
```markdown
## 5. User Actions & Workflows

### Primary Workflow

**<Name of primary workflow>**

*Status:* To be defined with `/concept.add-action`

This is the core interaction: <brief description>

### Secondary Workflows

Workflows to document:
- [ ] <Workflow2>
- [ ] <Workflow3>
```

### 7. Confirm Creation

Display a detailed success message:

```
✅ Created conceptual model for <AppName>

📄 File: docs/conceptual-model-<app-name>.md

📋 Summary of what we captured:

**Problem:** <brief problem statement>
**Metaphor:** <the metaphor>
**Complexity:** <Simple/Medium/Complex>

**Core objects identified:**
   • <Object1> - "<what users think it is>"
   • <Object2> - "<what users think it is>"
   • <Object3> - "<what users think it is>"

**Primary workflow:** <the ONE thing>

📊 Model status: ~25% complete

🎯 Next steps (in recommended order):

1. Define your core objects:
   → /concept.add-object <Object1>
   → /concept.add-object <Object2>
   → /concept.add-object <Object3>

2. Map how objects relate:
   → /concept.add-relationship <Object1> <Object2>

3. Document the primary workflow:
   → /concept.add-action <workflow-name>

4. Check progress:
   → /concept.status

💡 Tip: Focus on the most important object first - usually the one users
   interact with most frequently.

Happy modeling! 🎨🧠
```

## Important Guidelines

### Before Creating the File

1. **MUST use AskUserQuestion tool** - This is not optional
2. **Have a conversation** - Don't just collect data, understand deeply
3. **Get confirmation** - Show summary before creating file
4. **Wait for approval** - User must confirm the summary

### When Creating the File

1. **File Naming**: Always use kebab-case for filenames (e.g., `recipe-app`, not `RecipeApp`)
2. **Rich Context**: Include everything learned in the conversation, not just bullet points
3. **User's Words**: Quote the user's language, especially for mental models
4. **Specific Examples**: Include the concrete scenarios they mentioned
5. **Template Structure**: Use all 15 sections from the base template

### File Organization

1. **Validation**: Ensure the docs/ directory exists, create if needed
2. **No Overwrite**: If file exists, ask user if they want to overwrite or create a new version
3. **Backup**: If overwriting, suggest they can check git history

### Quality Checks

Before finishing, verify:
- ✅ Used AskUserQuestion tool
- ✅ Had conversational deep-dive
- ✅ Captured central metaphor
- ✅ Identified 3-5 core objects with mental models
- ✅ Documented primary workflow
- ✅ Included specific user examples
- ✅ Filled Executive Summary with rich detail
- ✅ Created starter content for key sections
- ✅ Showed summary and got confirmation

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
