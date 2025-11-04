# Conceptual Model-Driven Development

A framework for designing software from the user's mental model first.

## What is Conceptual Model-Driven Development?

**Conceptual Model-Driven Development** is a design philosophy that starts with understanding **how users think** about your application, rather than jumping straight to features, UI mockups, or implementation architecture.

Based on Johnson & Henderson's foundational research on conceptual models, this approach ensures that:

- **Users understand your product intuitively** because it matches their mental model
- **Teams align** around user thinking, not just technical architecture
- **Features feel cohesive** because they all fit the same conceptual framework
- **Design decisions have rationale** rooted in user cognition

---

## Why Start with Conceptual Models?

### The Problem with Traditional Development

Most software development follows one of these paths:

**Path 1: Implementation-First**
```
Technical Architecture → Database Schema → API Design → UI
```
*Result:* Technical concepts leak into the user experience

**Path 2: UI-First**
```
Wireframes → Visual Design → Features → Implementation
```
*Result:* Beautiful interface to functionality users don't understand

**Path 3: Feature-First**
```
Requirements List → User Stories → Implementation → UI
```
*Result:* Collection of features with no coherent mental model

### The Conceptual Model-Driven Path

```
User Tasks → Conceptual Model → UI Design → Implementation
     ↑              ↓
     └──── Validation ────┘
```

**Result:** A product users understand because it maps to how they naturally think about their work.

---

## Core Principles

### 1. **Task-Centered Design**

Start with the **task domain**, not the solution domain.

❌ **Wrong:** "We need a database with users, posts, and comments tables"
✅ **Right:** "People want to share thoughts and have conversations about them"

The conceptual model describes the essential concepts users need to accomplish their tasks.

### 2. **Simplicity First**

**Every concept has a cognitive cost.**

- Each object users learn
- Each relationship between objects
- Each special case or exception

The conceptual model should be **as simple as the task allows**, no simpler.

❌ **Wrong:** Adding features because they're easy to implement
✅ **Right:** Adding concepts only when they're essential to the task

### 3. **Structure Before Presentation**

Get the "bone structure" right first, then flesh it out.

**Order of design:**
1. **Conceptual Model** - What are the core objects and relationships?
2. **UI Design** - How do we present these concepts clearly?
3. **Implementation** - How do we build this reliably?

Starting with wireframes or code diverts attention from the fundamental design problem: **What should users think this is?**

### 4. **Explicit Intentional Design**

Conceptual models don't emerge accidentally - they must be **deliberately designed**.

Without explicit design:
- Developers add features that don't fit the model
- UI reveals implementation details
- Users form conflicting mental models
- Product feels incoherent

**Solution:** Document the conceptual model explicitly and make it the **source of truth** for all design decisions.

### 5. **User Understanding as Foundation**

The conceptual model defines the **ideal mental model** users should develop.

When the conceptual model is clear:
- Users can **predict** what will happen
- Users can **generalize** their knowledge to new features
- Users can **explain** the app to others
- Users feel **confident** using the product

---

## What Makes a Good Conceptual Model?

### Essential Components

A complete conceptual model includes:

#### 1. **Purpose & Scope**
- What does this application fundamentally do?
- What task domain does it address?
- Who are the users?

#### 2. **Objects (Concepts)**
- What "things" do users create and manipulate?
- What do users call these things?
- What do users think each thing is?

#### 3. **Attributes**
- What properties do objects have?
- Which attributes are visible to users?
- Which attributes matter for tasks?

#### 4. **Operations (Actions)**
- What can users do with each object?
- How do users think about these actions?
- What's the mental model for each operation?

#### 5. **Relationships**
- How do objects connect to each other?
- What's the user's mental model of these connections?
- Are relationships hierarchical, containment, or associative?

#### 6. **Task Mapping**
- How do task-domain concepts map to application concepts?
- Can all user tasks be expressed in terms of the model?
- Does the model match how users naturally think about their work?

---

## Validation Criteria

### ✅ Completeness Checks

- [ ] All user-facing concepts enumerated
- [ ] Relationships between concepts documented
- [ ] All task-relevant operations included
- [ ] Edge cases and error scenarios covered
- [ ] Concept names match user vocabulary

### ✅ Clarity & Coherence

- [ ] Model is simple enough to explain in one page
- [ ] No contradictory or confusing concepts
- [ ] Relationships are logical and predictable
- [ ] Similar objects treated consistently
- [ ] Concept granularity is appropriate

### ✅ Task Alignment

- [ ] Every concept supports actual user tasks
- [ ] No unnecessary technical concepts exposed
- [ ] Task scenarios work naturally with the model
- [ ] Common tasks are straightforward
- [ ] Complex tasks are possible

### ✅ Growth Capacity

- [ ] Model can evolve without breaking user understanding
- [ ] Extension points identified
- [ ] Migration paths for concept changes planned
- [ ] Version compatibility strategy defined

---

## Anti-Patterns to Avoid

### ❌ Implementation Leakage

**Problem:** Technical architecture drives user-facing concepts

**Example:**
- Exposing "sessions" or "tokens" to users
- Making users understand database relationships
- Using technical terms in the UI

**Solution:** Separate the conceptual model (user view) from implementation model (technical view)

---

### ❌ Metaphor Confusion

**Problem:** Treating design metaphors as the conceptual model

**Example:**
- "It's like a filing cabinet" becomes the entire model
- Physical world constraints applied to digital concepts
- Metaphor breaks down as features grow

**Solution:** Use metaphors to **explain** the model, not to **define** it

---

### ❌ Feature Accumulation

**Problem:** Adding features without considering conceptual coherence

**Example:**
- Calendar app adds tasks, notes, email, files, contacts...
- Each feature makes sense alone but together they're incoherent
- Users can't explain what the app "is"

**Solution:** Every new feature must fit the conceptual model, or the model must evolve deliberately

---

### ❌ Incoherent Object Identity

**Problem:** Unclear whether objects are shared or copied

**Example:**
- Does editing this item edit it everywhere?
- Is this a copy or a reference?
- What happens when the original changes?

**Solution:** Define clear rules for object identity and sharing in the conceptual model

---

### ❌ Missing Error Recovery

**Problem:** Conceptual model doesn't account for mistakes or changes

**Example:**
- No undo mechanism
- Can't recover from accidental deletion
- Changes are immediately permanent

**Solution:** Include undo/redo, versioning, or recovery mechanisms in the conceptual model

---

## The Conceptual Modeling Process

### Phase 1: Understand the Task Domain

**Before designing anything:**

1. **Study the work** - How do people accomplish these tasks today?
2. **Identify task objects** - What "things" do people work with?
3. **Map current procedures** - What's the current workflow?
4. **Question assumptions** - Could this work be done differently?

**Output:** Task analysis documenting current state

---

### Phase 2: Design the Conceptual Model

**Core design decisions:**

1. **Enumerate objects** - What are the primary concepts?
2. **Define attributes** - What properties do objects have?
3. **Specify operations** - What actions can users perform?
4. **Map relationships** - How do objects connect?
5. **Define the central metaphor** - What's the organizing principle?
6. **Document vocabulary** - What do users call each concept?

**Output:** Conceptual model document

---

### Phase 3: Validate with Users

**Test the model:**

1. **Explain the model** to target users
2. **Walk through task scenarios** using model concepts
3. **Ask users to predict** what would happen
4. **Identify confusion points**
5. **Refine the model** based on feedback

**Output:** Validated conceptual model

---

### Phase 4: Design UI & Implementation

**Only after the model is validated:**

1. **UI Design** - How do we present these concepts clearly?
2. **Visual Language** - How do we make objects recognizable?
3. **Interaction Patterns** - How do users perform operations?
4. **Implementation** - How do we build this reliably?

**Output:** Implemented product that matches the conceptual model

---

### Phase 5: Maintain Model Integrity

**Throughout development:**

1. **Guard the model** - Reject features that don't fit
2. **Evolve deliberately** - When concepts must change, do it consciously
3. **Document decisions** - Why did we design it this way?
4. **Onboard new team members** - Teach the conceptual model first

**Output:** Coherent product that users understand

---

## Examples of Good Conceptual Models

### Google Calendar

**Central Metaphor:** "My time, organized"

**Core Objects:**
- **Event** - "A chunk of my time dedicated to something"
- **Calendar** - "A category of events in my life" (work, personal, etc.)
- **Reminder** - "A prompt so I don't forget"

**Key Relationships:**
- Events belong to Calendars
- Events can be recurring (repeating pattern)
- Events can have Guests (shared time)

**Why it works:**
- Matches how people think about time
- Simple core concept (events as time blocks)
- Natural grouping (calendars for life areas)
- Handles sharing intuitively (invite guests to your time)

---

### Todo App

**Central Metaphor:** "My digital checklist"

**Core Objects:**
- **Task** - "Something I need to do"
- **List** - "A group of related tasks"

**Key Relationships:**
- Tasks belong to Lists
- Tasks have status (done/not done)

**Why it works:**
- Familiar checklist metaphor
- Minimal concepts (just tasks and lists)
- Binary completion state matches mental model
- Straightforward organization

---

### E-Commerce

**Central Metaphor:** "Shopping like in a store"

**Core Objects:**
- **Product** - "Something I can buy"
- **Cart** - "Things I'm planning to buy"
- **Order** - "My purchase"

**Key Relationships:**
- Products go into Cart
- Cart becomes Order when you checkout

**Why it works:**
- Maps to physical shopping experience
- Clear progression (browse → add to cart → checkout)
- Familiar vocabulary
- Predictable behavior

---

## Implementing Conceptual Models in Practice

### For Product Managers

**Use conceptual models to:**
- Evaluate feature requests ("Does this fit our model?")
- Write requirements in user concepts
- Align stakeholders around user thinking
- Make roadmap decisions based on conceptual coherence

### For Designers

**Use conceptual models to:**
- Design UI that reveals the model clearly
- Choose appropriate visual metaphors
- Create consistent interaction patterns
- Validate that designs match user mental models

### For Developers

**Use conceptual models to:**
- Structure code around user concepts
- Name classes and methods using user vocabulary
- Validate that implementation preserves conceptual integrity
- Make technical decisions that don't leak into UX

### For QA/Testing

**Use conceptual models to:**
- Write test scenarios in user language
- Validate that product behavior matches conceptual model
- Identify edge cases where model breaks down
- Ensure error messages use conceptual vocabulary

---

## Tools & Techniques

### Object/Operations Analysis

**Structure for documenting each concept:**

```markdown
### [Object Name]

**What users think it is:** [Mental model description]

**Attributes visible to users:**
- [Attribute 1]
- [Attribute 2]

**Actions users can perform:**
- [Action 1]
- [Action 2]

**Relationships:**
- [How this connects to other objects]
```

### Task Scenario Mapping

**Write task scenarios using conceptual model vocabulary:**

```markdown
#### [Task Name]

**User goal:** [What they want to accomplish]

**Mental model:** "[How user thinks about this task]"

**Flow:**
1. [Step 1] → "User thinks: [mental model]"
2. [Step 2] → "User thinks: [mental model]"
3. [Step 3] → "User thinks: [mental model]"

**Objects involved:** [List concepts used]
```

### Relationship Diagrams

**Map how concepts connect:**

```
User (Account Owner)
├── Calendars (Collections)
│   ├── Work Calendar
│   └── Personal Calendar
└── Events (Time Blocks)
    ├── Meetings (Shared Events)
    └── Reminders (Personal Events)
```

---

## Common Questions

### When should I create a conceptual model?

**Create a conceptual model when:**
- Starting a new product
- Redesigning an existing product
- Users report confusion about how things work
- Team members have conflicting ideas about how it should work
- Adding major new features

### How detailed should it be?

**Aim for 60-80% completeness:**
- All major objects documented
- Key relationships mapped
- Primary user workflows covered
- Central metaphor defined

Don't try to document every detail - perfect is the enemy of good.

### Can I use this for APIs?

**Yes!** API conceptual models focus on:
- **Resources** (objects) - What entities exist?
- **Endpoints** (operations) - What actions can you perform?
- **Request/response flow** (workflows) - How do operations work?
- **Developer mental model** - How should API consumers think about this?

### How do I keep it up to date?

**Maintenance strategies:**
- Review quarterly or after major features
- Make conceptual model review part of design process
- Version the model document
- Assign ownership to someone who guards conceptual integrity

---

## Further Reading

### Foundational Research

- **Johnson & Henderson (1991)** - "Conceptual Models: Begin by Designing What to Design"
- **Don Norman** - "The Design of Everyday Things"
- **Jakob Nielsen** - Mental Models in User Experience

### Related Frameworks

- **Domain-Driven Design** - Similar focus on domain concepts
- **Object-Oriented Design** - Objects, attributes, operations
- **Task Analysis** - Understanding user work

### Tools & Resources

- **Conceptual Model Kit** - This framework and templates
- **GitHub Spec Kit** - Specification-driven development
- **C4 Model** - Software architecture diagrams

---

## Summary: The Conceptual Model Advantage

When you design with conceptual models:

✅ **Users understand** your product intuitively
✅ **Teams align** around how users think
✅ **Features cohere** into a unified whole
✅ **Decisions have rationale** rooted in cognition
✅ **Products scale** without becoming incoherent
✅ **Onboarding is faster** with clear mental models
✅ **Support is easier** when everyone speaks the same language

---

**Start your next project with the question:**

> "What should users think this is?"

**Not:**

> "What features should this have?"
> "What should this look like?"
> "How should we build this?"

The conceptual model is the foundation. Get it right, and everything else follows.

---

*This document is part of the [Conceptual Model Kit](https://github.com/Lab-Secreto/conceptual-kit) - A framework for designing software from the user's mental model first.*
