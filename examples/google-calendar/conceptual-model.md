# Conceptual Model & Object Mapping

## Google Calendar

Based on Johnson & Henderson's Conceptual Models Framework

---

## 1. Executive Summary

**Purpose:** Define the conceptual model users form when interacting with Google Calendar.

Following Johnson & Henderson's principles, this document focuses on:

- **Objects:** Events, calendars, reminders, and time slots users manipulate
- **Attributes:** Time, duration, participants, locations, and colors
- **Actions:** Creating, scheduling, inviting, rescheduling, and viewing
- **Relationships:** How events relate to calendars, people, and time
- **Mental Models:** Calendar as a "time map" and "coordination space"

**Key Stakeholders:**

- Design Team
- Product Management
- Engineering
- Google Workspace Teams

---

## 2. Core Conceptual Model

### 2.1 The Central Metaphor

**"Your Time, Visualized and Coordinated"**

Users think of Google Calendar as a visual map of their time where they can:

- See their life laid out in time blocks
- Coordinate with others by overlaying schedules
- Claim time for activities like claiming physical space
- Navigate through time like navigating through a landscape

### 2.2 Mental Model Hierarchy

```
Calendar System (Time Container)
├── My Calendars (Time Layers)
│   ├── Personal Calendar
│   ├── Work Calendar
│   └── Shared Calendars
├── Time Views (Time Windows)
│   ├── Day View (Detailed)
│   ├── Week View (Balanced)
│   ├── Month View (Overview)
│   └── Agenda View (List)
├── Events (Time Claims)
│   ├── Meetings (Coordinated Time)
│   ├── Appointments (Reserved Time)
│   ├── Reminders (Time Markers)
│   └── All-day Events (Date Markers)
└── People (Time Coordinators)
    ├── Attendees
    ├── Guests
    └── Calendar Subscribers
```

### 2.3 Key Conceptual Principles

1. **Time as Space:** Users think of time slots as spaces they can fill
2. **Layered Visibility:** Multiple calendars overlay like transparent sheets
3. **Collaborative Ownership:** Events can be owned but shared
4. **Time Navigation:** Moving through time like scrolling through a map
5. **Visual Priority:** Color, size, and position indicate importance

---

## 3. Object Model

### 3.1 Primary Objects

#### EVENT (The Time Block)

**What users think it is:** "A chunk of my time dedicated to something"

**Attributes visible to users:**

- Title (what's happening)
- Time (when it starts/ends)
- Date (which day)
- Location (where to be)
- Color (which calendar/category)
- Participants (who's involved)
- Description (details/agenda)
- Attachments (related files)
- Status (tentative/confirmed/busy/free)

**Actions users can perform:**

- Create event
- Edit details
- Delete event
- Duplicate event
- Move/reschedule (drag)
- Resize (change duration)
- Invite others
- RSVP (yes/no/maybe)
- Set reminders
- Add to different calendar

**System attributes (hidden from users):**

- Event ID
- Calendar ID
- Sync status
- Creation timestamp
- Last modified
- Organizer permissions
- Recurrence rules

**User-visible structure:**

```
┌─────────────────────┐
│ 📅 Team Standup     │
│ 9:00 - 9:30 AM      │
│ 👥 8 guests         │
│ 📍 Zoom link        │
│ [Join] [Maybe] [No] │
└─────────────────────┘
```

---

#### CALENDAR (The Time Layer)

**What users think it is:** "A category or view of my events"

**Attributes visible to users:**

- Name (e.g., "Work", "Personal")
- Color (visual identifier)
- Visibility (shown/hidden)
- Access level (owner/editor/viewer)
- Description
- Time zone
- Sharing status

**Actions users can perform:**

- Create calendar
- Rename calendar
- Change color
- Show/hide calendar
- Share calendar
- Subscribe to calendar
- Import/export events
- Delete calendar
- Set notifications defaults

**System attributes (hidden from users):**

- Calendar ID
- Sync tokens
- Permission sets
- Integration keys

---

### 3.2 Object Types & Categories

#### MEETING (Coordinated Event)

**Mental model:** "Time when multiple people need to be together"

**User-visible structure:**

```
┌─────────────────────┐
│ 📅 Team Standup     │
│ 9:00 - 9:30 AM      │
│ 👥 8 guests         │
│ 📍 Zoom link        │
│ [Join] [Maybe] [No] │
└─────────────────────┘
```

**Attributes shown:**

- Meeting title
- Time slot
- Guest list/count
- Meeting location/link
- RSVP status
- Organizer
- Video call link

---

#### REMINDER (Time Marker)

**Mental model:** "A post-it note at a specific time"

**User-visible structure:**

```
┌─────────────────────┐
│ 🔔 Call dentist     │
│ 2:00 PM             │
│ [Mark done] [Edit]  │
└─────────────────────┘
```

**Attributes shown:**

- Reminder text
- Time
- Completion status
- Recurrence

---

#### ALL-DAY EVENT (Date Marker)

**Mental model:** "Something that marks an entire day"

**User-visible structure:**

```
┌─────────────────────┐
│ 🎂 Sarah's Birthday │
│ All day             │
└─────────────────────┘
```

---

### 3.3 Layout/Structure System

**Mental model:** "A grid where time flows vertically/horizontally"

**Visual representation:**

```
Week View:
  Mon  Tue  Wed  Thu  Fri
8am  ┌─┐  ───  ┌─┐  ───  ┌─┐
9am  │M│  ───  │M│  ───  │M│ ← Recurring
10am └─┘  ┌─┐  └─┘  ───  └─┘
11am ───  │A│  ───  ┌──────┐
12pm ───  └─┘  ───  │Lunch │ ← Different calendar (color)
1pm  ───  ───  ───  └──────┘
```

**Attributes:**

- Time increments (15/30/60 min)
- Day boundaries
- Current time indicator
- Weekend distinction
- Calendar layer colors

---

## 4. Relationships & Rules

### 4.1 Object Relationships

```
User (1) ───── owns ─────→ Calendars (n)
Calendar (1) ─ contains ──→ Events (0..n)
Event (1) ──── has ───────→ Attendees (0..n)
Event (1) ──── belongs to ─→ Calendar (1)
Event (1) ──── may repeat ─→ Recurrence Pattern (0..1)
User (1) ───── subscribes to ─→ Calendars (0..n)
Event (1) ──── links to ──→ Video Call (0..1)
```

### 4.2 Conceptual Rules (User's Understanding)

1. **No Time Travel:** "I can't create events in the past" (with exceptions)
2. **One Place at a Time:** "Conflicting events show as overlapping"
3. **Color = Category:** "Each calendar has its own color"
4. **Invitation = Notification:** "When I invite someone, they get notified"
5. **Tentative Until Confirmed:** "Grayed out means not confirmed"
6. **Private by Choice:** "I control who sees my calendar details"

### 4.3 System Constraints (Learned Through Use)

- Maximum event title: ~255 characters
- Guest limit: 200 per event (free accounts)
- Calendar limit: 25 calendars per account
- Notification limit: 5 per event
- Attachment size: 25MB via Google Drive
- Recurring event limit: 730 occurrences
- Time zones: All events convert to viewer's zone

---

## 5. User Actions & Workflows

### 5.1 Primary Action Flows

#### Creating an Event (Claiming Time Flow)

**Mental model:** "Blocking out time for something"

**Flow:**

1. Click time slot → "I want this time"
2. Type event name → "This is what it's for"
3. Adjust duration → "It'll take this long"
4. Add location → "It happens here"
5. Invite people → "These people should know/come"
6. Save → "Lock it in"

**Objects involved:**

- Event
- Calendar
- Time slot

---

#### Finding a Meeting Time (Coordination Flow)

**Mental model:** "Finding when everyone is free"

**Flow:**

1. Create event → "I need to schedule something"
2. Add guests → "With these people"
3. Check availability → "When are we all free?"
4. See conflicts → "Oh, Jim is busy then"
5. Adjust time → "Let's try this slot instead"
6. Send invites → "Does this work for everyone?"

**Objects involved:**

- Event
- Users
- Calendars (overlaid)

---

#### Weekly Planning (Overview Flow)

**Mental model:** "Seeing my week at a glance"

**Flow:**

1. Switch to week view → "Show me the whole week"
2. Scan for gaps → "Where do I have free time?"
3. Check meeting density → "Is Thursday too packed?"
4. Drag events → "Move this to a better time"
5. Add buffer time → "Block time between meetings"

**Objects involved:**

- Week view
- Events
- Time blocks

---

## 6. Information Architecture

### 6.1 Conceptual Hierarchy (User's View)

```
My Google Calendar
├── My Time
│   ├── Today's Schedule
│   ├── This Week
│   ├── This Month
│   └── Upcoming Events
├── My Calendars
│   ├── Personal
│   ├── Work
│   ├── Family
│   └── Subscriptions
├── My Events
│   ├── Meetings I Own
│   ├── Invitations
│   ├── Recurring Events
│   └── Reminders
└── My People
    ├── Frequent Attendees
    ├── Shared Calendars
    └── Guest Permissions
```

### 6.2 Visual Hierarchy Principles

- **Size = Duration:** Longer events appear taller/wider
- **Color = Calendar:** Each calendar has distinct color
- **Opacity = Tentative:** Unconfirmed events are semi-transparent
- **Position = Time:** Vertical/horizontal position indicates when
- **Bold = Current:** Today/current time is highlighted
- **Strikethrough = Cancelled:** Cancelled events show struck through

---

## 7. State Model

### 7.1 Event States (User Perception)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ TENTATIVE   │ ──→│ CONFIRMED   │ ──→│ COMPLETED   │
│"Penciled in"│    │"It's        │    │"It happened"│
│             │    │ happening"  │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
      ↓                   ↓
┌─────────────┐    ┌─────────────┐
│ CANCELLED   │    │ RESCHEDULED │
│"Not         │    │"New time"   │
│ happening"  │    │             │
└─────────────┘    └─────────────┘
```

### 7.2 Calendar States (User Perception)

- **Visible:** "I can see these events"
- **Hidden:** "Temporarily turned off"
- **Syncing:** "Updating from source"
- **Error:** "Can't connect right now"
- **Read-only:** "I can see but not edit"

---

## 8. Error & Exception Handling

### 8.1 Conceptual Error Messages

| System Error | User Sees | User Thinks |
|-------------|-----------|-------------|
| Network timeout | "Offline - changes saved locally" | "It'll sync when I'm back online" |
| Permission denied | "You need permission to edit" | "I can only view this" |
| Conflict detected | "This time has conflicts" | "I'm double-booked" |
| Invalid date | "Please enter a valid date" | "I typed it wrong" |
| Sync failure | "Having trouble syncing" | "The server is having issues" |
| Guest limit exceeded | "Too many guests (max 200)" | "I need to use a different tool" |

### 8.2 Graceful Degradation

When services fail, the conceptual model remains intact:

- No network → Local changes queue for sync
- Can't send invites → Save event, notify manually
- Video link fails → Show phone number backup
- Can't load calendar → Show cached version
- Permissions revoked → Switch to read-only view

---

## 9. Metaphorical Consistency

### 9.1 Metaphors Throughout

| System Concept | Metaphor | User Language |
|---------------|----------|---------------|
| Calendar database | "Calendar layer" | "My work calendar" |
| Event object | "Time block" | "My 2pm meeting" |
| Recurring rule | "Repeat pattern" | "Every Tuesday" |
| Permission system | "Sharing" | "Let them see/edit" |
| Notification system | "Reminders" | "Alert me before" |
| Synchronization | "Staying updated" | "It syncs" |
| Time zone conversion | "Local time" | "In my time zone" |

### 9.2 Language & Terminology

**Use ✅**

- Event, meeting, appointment
- Calendar, schedule
- Invite, guest, attendee
- Reminder, notification
- Busy, free, available
- Repeat, recurring

**Avoid ❌**

- Database record (too technical)
- Instance, object (too abstract)
- Sync token (implementation detail)
- API, webhook (developer-focused)
- Entity, model (too abstract)

---

## 10. Progressive Disclosure Model

### 10.1 Complexity Layers

**Layer 1: Novice (First Week)**

- **Sees:** Basic month view, create simple events
- **Thinks:** "It's like a paper calendar but digital"
- **Can do:** Add events, see calendar, set basic reminders

**Layer 2: Regular (First Month)**

- **Sees:** Multiple calendars, guest invites, recurring events
- **Thinks:** "I can coordinate with others and organize my life"
- **Can do:** Manage multiple calendars, schedule meetings, find time slots

**Layer 3: Power User (3+ Months)**

- **Sees:** Appointment slots, working locations, calendar analytics
- **Thinks:** "This is my complete time management system"
- **Can do:** Complex scheduling, automated booking, integration with other tools

### 10.2 Feature Discovery Path

```
Basic Use          Coordination        Advanced Control
    │                  │                     │
    ├─ Add events      ├─ Invite others     ├─ Appointment slots
    ├─ Set reminders   ├─ Find meeting      ├─ Working locations
    ├─ View calendar   │   times             ├─ Custom
    └─ Color coding    ├─ Share calendar    │   notifications
                       └─ Check             └─ Keyboard
                           availability         shortcuts
```

---

## 11. Platform-Specific Adaptations

### 11.1 Mental Model Shifts

- **Desktop:** "Command center for time management - see everything, plan ahead"
- **Mobile:** "Quick checker and capture device - what's next, add on the go"
- **Tablet:** "Portable planner - review and adjust my schedule"

### 11.2 Interaction Patterns

| Gesture/Input | Desktop Action | Mobile Action | User Expects |
|--------------|---------------|---------------|--------------|
| Click/Tap | Select time slot | View event | "Show details" |
| Drag | Move event | Scroll view | "Reschedule/Navigate" |
| Long press | Right-click menu | Event options | "More options" |
| Pinch | - | Zoom timeline | "Change time scale" |
| Swipe | - | Change date | "Move through time" |
| Double-click | Create event | - | "Quick create" |

---

## 12. Design Principles from Model

### 12.1 Core Principles

1. **Time is Visual:** Show time spatially, not just as numbers
2. **Direct Manipulation:** Drag to reschedule, resize to change duration
3. **Contextual Clarity:** Always show when and where user is in time
4. **Glanceable Status:** Color and visual weight convey information instantly
5. **Incremental Disclosure:** Start simple, reveal complexity as needed
6. **Social Coordination:** Make scheduling with others frictionless

### 12.2 Key Design Decisions

Based on the conceptual model:

- **Grid-based layout:** Time is spatial, events are blocks in space
- **Color-per-calendar:** Visual separation without cognitive load
- **Current time indicator:** Always oriented in the present
- **Overlay conflicts:** Physical impossibility of being two places
- **Inline editing:** Direct manipulation reduces abstraction
- **Smart defaults:** Most events are 1 hour, start on hour/half-hour

---

## 13. Implementation Notes for Designers

### 13.1 Visual Cues for Object Types

- **Regular events:** Solid color blocks with clear edges
- **All-day events:** Banner style at top of day
- **Tentative events:** Diagonal stripes or reduced opacity
- **Recurring events:** Small repeat icon in corner
- **Conflicts:** Red border or overlap indicator
- **Past events:** Slightly grayed out
- **Current time:** Red line across view
- **Free time:** No visual marking (negative space)

### 13.2 Maintaining Conceptual Integrity

Critical rules to never break:

- Time always flows in consistent direction (top-bottom or left-right)
- Color coding remains consistent across all views
- Current moment is always findable
- User's own calendar is visually primary
- Conflicts are always visible, never hidden
- Direct manipulation is preferred over dialogs

---

## 14. Validation & Testing

### 14.1 Conceptual Model Validation Tests

1. **First-use test:** Can users create an event without instructions?
2. **Mental model interview:** How do users describe the calendar to others?
3. **Conflict resolution:** Do users understand overlapping events?
4. **Sharing comprehension:** Do users understand visibility settings?
5. **Time zone test:** Do users grasp events in different zones?

### 14.2 Success Metrics

- Time to create first event < 30 seconds
- Successful meeting scheduling > 90% first attempt
- Finding free time < 10 seconds
- Understanding of sharing model > 85%
- Successful conflict resolution > 95%
- Mobile quick-add usage > 60% of mobile events

---

## Summary

**Core Metaphor:** Google Calendar is a visual map of time where users claim slots, coordinate with others, and navigate through their schedule.

**Key Principles:**

- Time is spatial and visual
- Direct manipulation reduces abstraction
- Colors and layers organize complexity
- Social coordination is built-in
- Past, present, and future are always accessible

**Critical Success Factors:**

- Users can see their time at a glance
- Creating events is faster than paper calendars
- Coordination with others feels natural
- The system prevents double-booking
- Works seamlessly across devices

---

## Appendices

### A. Glossary of Terms

- **Event:** A block of time dedicated to an activity
- **Calendar:** A collection/layer of related events
- **Guest:** Someone invited to an event
- **Recurring:** Events that repeat on a pattern
- **Reminder:** A notification before an event
- **Busy/Free:** Availability status for time slots

### B. Related Documents

- Material Design System Guidelines
- Google Workspace Integration Specs
- Calendar API Documentation

### C. Version History

- v1.0 - Initial draft based on current Google Calendar
- v1.1 - Added mobile interaction patterns

---

*This conceptual model captures how users think about Google Calendar, focusing on the mental models that make the product intuitive and successful.*
