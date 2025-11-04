# Conceptual Model & Object Mapping

## Todo App

Based on Johnson & Henderson's Conceptual Models Framework

---

## 1. Executive Summary

**Purpose:** Define the conceptual model users form when interacting with a simple Todo application.

Following Johnson & Henderson's principles, this document focuses on:

- **Objects:** Tasks, lists, and tags users interact with
- **Attributes:** Title, status, due date, priority
- **Actions:** Creating, completing, organizing, filtering
- **Relationships:** How tasks relate to lists and tags
- **Mental Models:** Todo app as a "digital checklist" and "task inbox"

**Key Stakeholders:**

- Product Team
- Design Team
- Mobile Development

---

## 2. Core Conceptual Model

### 2.1 The Central Metaphor

**"Your Digital Checklist"**

Users think of the Todo App as a simple checklist where they can:

- Write down things they need to do
- Check off completed items
- Organize tasks into groups
- See what's urgent vs. what can wait

### 2.2 Mental Model Hierarchy

```
Todo System
├── My Tasks (The Inbox)
│   ├── Today
│   ├── Upcoming
│   └── Someday
├── Lists (Categories)
│   ├── Work
│   ├── Personal
│   └── Shopping
└── Views (Filters)
    ├── All Tasks
    ├── Completed
    └── By Priority
```

### 2.3 Key Conceptual Principles

1. **Task as Item:** Each task is a discrete item to check off
2. **Lists as Containers:** Lists group related tasks together
3. **Status is Binary:** Tasks are either done or not done
4. **Visual Completion:** Checked items show progress
5. **Inbox Zero:** The goal is to complete all tasks

---

## 3. Object Model

### 3.1 Primary Objects

#### TASK (The Todo Item)

**What users think it is:** "Something I need to do"

**Attributes visible to users:**

- Title (what needs to be done)
- Status (done/not done)
- Due date (when it's due)
- Priority (high/medium/low)
- List (which category)
- Notes (additional details)

**Actions users can perform:**

- Create task
- Mark as complete
- Edit title
- Set due date
- Change priority
- Move to different list
- Delete task
- Add notes

**System attributes (hidden from users):**

- Task ID
- Creation date
- Last modified
- User ID

**User-visible structure:**

```
┌─────────────────────────────┐
│ ☐ Buy groceries             │
│ 📅 Today  🔴 High priority  │
│ 📋 Personal                 │
└─────────────────────────────┘
```

---

#### LIST (The Category)

**What users think it is:** "A group of related tasks"

**Attributes visible to users:**

- Name (e.g., "Work", "Personal")
- Color (visual identifier)
- Task count (how many tasks)
- Icon (optional emoji)

**Actions users can perform:**

- Create list
- Rename list
- Change color
- Delete list
- Reorder lists

**System attributes (hidden from users):**

- List ID
- Creation date
- Sort order

---

### 3.2 Object Types & Categories

#### QUICK TASK (Simple Item)

**Mental model:** "Quick thing to remember"

**User-visible structure:**

```
┌─────────────────────┐
│ ☐ Call mom          │
└─────────────────────┘
```

---

#### SCHEDULED TASK (Time-bound Item)

**Mental model:** "Something due on a specific date"

**User-visible structure:**

```
┌─────────────────────────────┐
│ ☐ Submit report             │
│ 📅 Tomorrow  🔴 High        │
└─────────────────────────────┘
```

---

#### COMPLETED TASK (Done Item)

**Mental model:** "Something I've finished"

**User-visible structure:**

```
┌─────────────────────────────┐
│ ✅ Buy groceries            │
│ ~~Completed 2 hours ago~~   │
└─────────────────────────────┘
```

---

### 3.3 Layout/Structure System

**Mental model:** "A vertical list I scroll through"

**Visual representation:**

```
Today
┌──────────────────────┐
│ ☐ Morning standup    │
│ ☐ Review PRs         │
│ ☐ Write tests        │
└──────────────────────┘

Tomorrow
┌──────────────────────┐
│ ☐ Team planning      │
└──────────────────────┘

Completed
┌──────────────────────┐
│ ✅ Buy groceries     │
│ ✅ Call dentist      │
└──────────────────────┘
```

---

## 4. Relationships & Rules

### 4.1 Object Relationships

```
User (1) ───── owns ─────→ Lists (n)
List (1) ───── contains ──→ Tasks (0..n)
Task (1) ───── belongs to ─→ List (1)
Task (1) ───── has ───────→ Due Date (0..1)
```

### 4.2 Conceptual Rules (User's Understanding)

1. **One Task, One List:** "Each task lives in exactly one list"
2. **Checkbox = Done:** "Click the box to mark it complete"
3. **Strike-through = Finished:** "Crossed out means I did it"
4. **Red = Urgent:** "Red tasks need attention now"
5. **Empty List = Success:** "No tasks means I'm caught up"

### 4.3 System Constraints (Learned Through Use)

- Maximum task title: 500 characters
- Lists per account: Unlimited (practical limit ~50)
- Tasks per list: Unlimited (performance degrades after 1000)
- Due dates: Cannot be in the past (unless editing existing task)

---

## 5. User Actions & Workflows

### 5.1 Primary Action Flows

#### Creating a Task (Capture Flow)

**Mental model:** "Writing down something I need to do"

**Flow:**

1. Click "Add task" → "I need to remember something"
2. Type task name → "What is it?"
3. Optionally set due date → "When do I need to do it?"
4. Optionally set priority → "How urgent is it?"
5. Save → "Got it, won't forget"

**Objects involved:**

- Task
- List (default or selected)

---

#### Completing a Task (Achievement Flow)

**Mental model:** "Checking something off my list"

**Flow:**

1. Click checkbox → "I finished this"
2. Task strikes through → "Visual confirmation"
3. Task moves to completed → "Out of my way"

**Objects involved:**

- Task
- Status change

---

#### Daily Review (Planning Flow)

**Mental model:** "Seeing what I need to do today"

**Flow:**

1. Open app → "What's on my plate?"
2. Check "Today" section → "What's due now?"
3. Check priorities → "What's most important?"
4. Reorder if needed → "Let me prioritize"
5. Start working → "Time to get things done"

**Objects involved:**

- Task list
- Filters
- Views

---

## 6. Information Architecture

### 6.1 Conceptual Hierarchy (User's View)

```
My Todo App
├── Inbox (Default)
│   ├── Today
│   ├── Tomorrow
│   └── Upcoming
├── My Lists
│   ├── Work
│   ├── Personal
│   ├── Shopping
│   └── Projects
└── Views
    ├── All Tasks
    ├── Completed
    ├── High Priority
    └── No Due Date
```

### 6.2 Visual Hierarchy Principles

- **Unchecked = Active:** Open checkboxes are things to do
- **Red = Urgent:** High priority items stand out
- **Gray = Done:** Completed items fade visually
- **Bold = Today:** Today's tasks are emphasized
- **Position = Time:** Earlier tasks appear higher

---

## 7. State Model

### 7.1 Task States (User Perception)

```
┌─────────────┐
│   CREATED   │
│ "Need to do"│
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  COMPLETED  │
│ "All done"  │
└─────────────┘
```

### 7.2 List States (User Perception)

- **Active:** Has uncompleted tasks
- **Empty:** No tasks in list
- **Archived:** Hidden from main view

---

## 8. Error & Exception Handling

### 8.1 Conceptual Error Messages

| System Error | User Sees | User Thinks |
|-------------|-----------|-------------|
| Empty task title | "Please enter a task name" | "I forgot to type it" |
| Network error | "Offline - changes saved locally" | "It'll sync later" |
| List not found | "This list was deleted" | "Someone removed it" |

### 8.2 Graceful Degradation

When services fail, the conceptual model remains intact:

- No network → Changes queue for sync
- Sync conflict → Show both versions, let user choose
- List deleted → Move orphaned tasks to inbox

---

## 9. Metaphorical Consistency

### 9.1 Metaphors Throughout

| System Concept | Metaphor | User Language |
|---------------|----------|---------------|
| Task database | "Checklist" | "My todo list" |
| Completion status | "Checkbox" | "Check it off" |
| List container | "Category" | "My work list" |
| Priority level | "Urgency flag" | "High priority" |

### 9.2 Language & Terminology

**Use ✅**

- Task, todo, item
- List, category
- Complete, done, finished
- Priority, urgent
- Due date, deadline

**Avoid ❌**

- Record (too technical)
- Entity (too abstract)
- Status flag (implementation detail)
- Boolean (developer term)

---

## 10. Progressive Disclosure Model

### 10.1 Complexity Layers

**Layer 1: Novice (First Day)**

- **Sees:** Simple task list, checkbox, add button
- **Thinks:** "It's a digital checklist"
- **Can do:** Add tasks, check them off

**Layer 2: Regular (First Week)**

- **Sees:** Lists, due dates, priorities
- **Thinks:** "I can organize by category and time"
- **Can do:** Create lists, set due dates, prioritize

**Layer 3: Power User (1+ Month)**

- **Sees:** Filters, search, keyboard shortcuts
- **Thinks:** "This is my task management system"
- **Can do:** Advanced filtering, batch operations, quick entry

---

## 11. Platform-Specific Adaptations

### 11.1 Mental Model Shifts

- **Desktop:** "Full view of all my tasks - organize and plan"
- **Mobile:** "Quick capture and check-off - on the go"

### 11.2 Interaction Patterns

| Gesture/Input | Desktop Action | Mobile Action | User Expects |
|--------------|---------------|---------------|--------------|
| Click/Tap | Toggle checkbox | Toggle checkbox | "Mark done" |
| Double-click | Edit task | - | "Change details" |
| Drag | Reorder task | Reorder/swipe | "Change position" |
| Swipe | - | Delete/complete | "Quick action" |

---

## 12. Design Principles from Model

### 12.1 Core Principles

1. **Simplicity First:** Don't overwhelm with options
2. **Immediate Feedback:** Checkboxes respond instantly
3. **Visual Progress:** Show what's done vs. what's left
4. **Quick Capture:** Add tasks with minimal friction
5. **Forgiving:** Easy to undo mistakes

### 12.2 Key Design Decisions

- **Checkbox-centric:** Primary interaction is checking off
- **List-based layout:** Vertical scrolling matches mental model
- **Minimal required fields:** Only title is required
- **Strike-through completion:** Visual satisfaction of crossing off
- **Today view default:** Most relevant view first

---

## 13. Implementation Notes for Designers

### 13.1 Visual Cues for Object Types

- **Active task:** Open checkbox, black text
- **Completed task:** Checked box, gray strike-through text
- **High priority:** Red accent, filled circle indicator
- **Due today:** Bold text, yellow highlight
- **Overdue:** Red text, urgent indicator

### 13.2 Maintaining Conceptual Integrity

Critical rules to never break:

- Checkbox always on the left (consistent position)
- Completed tasks always strike through
- Lists remain distinct by color
- Today's tasks always easily accessible

---

## 14. Validation & Testing

### 14.1 Conceptual Model Validation Tests

1. **First-use test:** Can users add a task without instructions?
2. **Completion test:** Do users understand how to mark tasks done?
3. **List comprehension:** Do users grasp organizing by lists?

### 14.2 Success Metrics

- Time to create first task < 10 seconds
- Task completion success rate > 99%
- Users who create lists within first day > 60%

---

## Summary

**Core Metaphor:** Todo App is a digital checklist for capturing and completing tasks.

**Key Principles:**

- Simple and focused on core function
- Immediate visual feedback
- Minimal friction to add tasks
- Satisfying to complete items

**Critical Success Factors:**

- Add task in seconds
- Check off is obvious
- Lists organize naturally
- Works offline

---

## Appendices

### A. Glossary of Terms

- **Task:** An item that needs to be done
- **List:** A collection of related tasks
- **Checkbox:** The control for marking tasks complete
- **Priority:** How urgent or important a task is
- **Due date:** When a task needs to be completed

### B. Related Documents

- Mobile Design Guidelines
- Accessibility Standards

### C. Version History

- v1.0 - Initial simple todo app model

---

*This conceptual model captures the mental model for a simple, focused todo application.*
