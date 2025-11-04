# /concept.add-action

Add user workflows and actions to your conceptual model.

## Purpose

Document how users accomplish tasks in your application. Actions capture the step-by-step mental journey users take, focusing on what they think at each step rather than technical implementation.

## Usage

```
/concept.add-action <action-name>
```

## Workflow

When this command is executed, follow these steps:

### 1. Locate Conceptual Model

Find the active conceptual model file in `docs/`.

### 2. Validate Action Doesn't Exist

Check the "User Actions & Workflows" section:
- If action already exists: Ask if user wants to update it
- If not: Proceed with creation

### 3. Gather Workflow Details

Use AskUserQuestion for structured input:

**Question 1: Action Type**
- Header: "Action Type"
- Question: "What type of action is this?"
- Options:
  - Creation (Making something new - e.g., Create Post, Add Recipe)
  - Modification (Changing existing - e.g., Edit Profile, Update Task)
  - Navigation (Moving around - e.g., Browse Feed, Search Recipes)
  - Interaction (Engaging with content - e.g., Like Post, Comment)
  - Organization (Arranging things - e.g., Sort List, Create Folder)
  - Deletion (Removing things - e.g., Delete Post, Archive Task)

**Question 2: Complexity**
- Header: "Complexity"
- Question: "How complex is this workflow?"
- Options:
  - Simple (1-3 steps - e.g., Like a post)
  - Medium (4-7 steps - e.g., Create a post with media)
  - Complex (8+ steps - e.g., Checkout process)

Then gather via text input:
- **Action name**: User-friendly name (e.g., "Creating a Recipe", not "RecipeCreation")
- **User's mental model**: What users think they're doing (1 sentence)
- **Trigger**: What makes users want to do this?
- **Success outcome**: What does success look like to the user?

### 4. Gather Step-by-Step Flow

For each step, collect:
- **Step number**
- **User action**: What they do (e.g., "Click 'New Recipe' button")
- **Mental model**: What they're thinking (e.g., "I want to add a recipe")
- **Objects involved**: Which objects from the model are touched
- **Feedback**: What confirms the step worked

Guide user to provide 3-8 steps (adjust based on complexity).

### 5. Create Workflow Entry

Use template from `templates/sections/workflows.md`:

```markdown
### <ActionName>

**User's mental model:** "<what-user-thinks-they-are-doing>"

**Type:** <Creation | Modification | Navigation | Interaction | Organization | Deletion>

**Trigger:** <what-motivates-this-action>

**Success outcome:** <what-success-looks-like>

**Objects involved:** <Object1>, <Object2>, <Object3>

#### Flow

**Step 1: <action>**
- What user does: <concrete-action>
- What user thinks: "<mental-model-quote>"
- Objects: <which-objects-involved>
- Feedback: <what-confirms-success>

**Step 2: <action>**
- What user does: <concrete-action>
- What user thinks: "<mental-model-quote>"
- Objects: <which-objects-involved>
- Feedback: <what-confirms-success>

[... continue for all steps ...]

**Step N: Complete**
- What user does: <final-action>
- What user thinks: "<mental-model-quote>"
- Objects: <which-objects-involved>
- Feedback: <confirmation-message>

#### Edge Cases & Errors

**If <error-condition>:**
- User sees: "<error-message>"
- User thinks: "<user-interpretation>"
- Recovery: <how-to-fix>

#### Success Indicators

- ✅ <indicator-1>
- ✅ <indicator-2>
- ✅ <indicator-3>
```

### 6. Insert into Workflows Section

Add to "5. User Actions & Workflows":
- Group by action type if multiple workflows exist
- Maintain logical order (common actions first)
- Keep consistent formatting

### 7. Update Related Objects

Go back to object cards and add action references:

```markdown
**Related workflows:**
- <ActionName> (see User Actions & Workflows)
```

### 8. Confirm Addition

Display success message:

```
✅ Added workflow: <ActionName>

📋 Workflow details:
   Type: <action-type>
   Steps: <count>
   Objects: <object-list>
   Complexity: <simple|medium|complex>

📊 Model progress:
   Objects: <count>
   Relationships: <count>
   Workflows: <count>
   Completeness: ~<percentage>%

Next steps:
→ Add more workflows: /concept.add-action <action-name>
→ Review model: /concept.review
→ Generate final document: /concept.generate

Suggested workflows to add:
• <SuggestedAction1>
• <SuggestedAction2>
• <SuggestedAction3>
```

## Important Guidelines

1. **User-Centric Steps**: Describe what users think, not system operations
2. **Concrete Actions**: Use specific verbs (click, type, select, not "interact with")
3. **Mental Models**: Include what users are thinking at each step
4. **Error Handling**: Document what happens when things go wrong
5. **Success Clarity**: Make success outcomes obvious

## Examples

### Example 1: Creating a Recipe

```
User: /concept.add-action create-recipe

Inputs:
- Type: Creation
- Complexity: Medium
- Mental model: "Saving a new recipe to my collection"
- Trigger: "I found a recipe I want to remember"
- Success: "Recipe is saved and I can find it later"

Steps:
1. Click "Add Recipe"
   - Think: "I want to save a new recipe"
   - Objects: User interface
   - Feedback: Form appears

2. Enter recipe title
   - Think: "Give it a memorable name"
   - Objects: Recipe
   - Feedback: Title appears in field

3. Add ingredients
   - Think: "List what I need to make this"
   - Objects: Recipe, Ingredients
   - Feedback: Ingredients appear in list

4. Write instructions
   - Think: "Explain how to make it step by step"
   - Objects: Recipe
   - Feedback: Instructions appear in editor

5. Click "Save"
   - Think: "Keep this for later"
   - Objects: Recipe, User collection
   - Feedback: "Recipe saved!" confirmation

Result: Added to docs/conceptual-model-recipe-book.md
```

### Example 2: Completing a Task

```
User: /concept.add-action complete-task

Inputs:
- Type: Modification
- Complexity: Simple
- Mental model: "Marking something as done"
- Trigger: "I finished this task"
- Success: "Task is checked off my list"

Steps:
1. Find task in list
   - Think: "Where's that task I finished?"
   - Objects: Task, List
   - Feedback: Task is highlighted

2. Click checkbox
   - Think: "Mark it done"
   - Objects: Task
   - Feedback: Checkbox fills, task gets strikethrough

3. Task moves to completed
   - Think: "It's out of my way"
   - Objects: Task, List
   - Feedback: Task animates to 'Completed' section

Result: Added to docs/conceptual-model-todo-app.md
```

### Example 3: Searching Recipes

```
User: /concept.add-action search-recipes

Inputs:
- Type: Navigation
- Complexity: Simple
- Mental model: "Finding a specific recipe"
- Trigger: "I want to make something specific"
- Success: "I found the recipe I was looking for"

Steps:
1. Click search box
   - Think: "I need to find that recipe"
   - Objects: User interface
   - Feedback: Search box is active, keyboard appears

2. Type search term
   - Think: "Let me search for 'chocolate cake'"
   - Objects: Recipe collection
   - Feedback: Results appear as I type

3. Browse results
   - Think: "Looking for the right one"
   - Objects: Recipe list
   - Feedback: Matching recipes displayed

4. Click on recipe
   - Think: "This is the one!"
   - Objects: Recipe
   - Feedback: Recipe details open

Result: Added to docs/conceptual-model-recipe-book.md
```

## Error Handling

- **No conceptual model**: Guide to `/concept.init`
- **Action name too vague**: Suggest being more specific
- **No objects involved**: Remind to reference objects from the model
- **Too many steps**: Suggest breaking into sub-workflows

## Best Practices

### ✅ Good Step Descriptions

**What user does:**
- "Click 'New Post' button" (specific)
- "Type post content" (concrete)
- "Select photo from library" (clear)

**What user thinks:**
- "I want to share this" (mental model)
- "Add a picture to make it interesting" (motivation)
- "Let everyone see it" (intent)

### ❌ Avoid Technical Descriptions

**Bad:**
- "System validates input" (system-centric)
- "POST request sent to API" (technical)
- "Database updated" (implementation)

**Good:**
- "Form checks if required fields are filled" (user-visible)
- "Saving..." message appears (feedback)
- "Post appears in feed" (outcome)

### Action Naming Patterns

**Creation Actions:**
- Creating a Recipe
- Adding a Task
- Starting a Project
- Posting Content

**Modification Actions:**
- Editing Profile
- Updating Task Status
- Changing Settings
- Rearranging Items

**Navigation Actions:**
- Browsing Feed
- Searching Recipes
- Filtering Tasks
- Exploring Categories

**Interaction Actions:**
- Liking a Post
- Commenting on Recipe
- Sharing Content
- Saving Favorites

## Reference

- See `examples/` for complete workflow examples
- Check `templates/sections/workflows.md` for structure
- Read `conceptual-modeling.md` section on "User Actions and Mental Operations"
