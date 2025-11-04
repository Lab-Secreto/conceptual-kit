# Project Structure

## Directory Layout

```
conceptual-kit/
├── .github/
│   └── copilot-instructions.md    # Custom commands definition
│
├── templates/
│   ├── base-model.md              # Main document template
│   ├── components/
│   │   ├── object-card.md         # Template for object definitions
│   │   ├── relationship-diagram.md # Template for relationships
│   │   └── workflow-steps.md      # Template for workflows
│   └── sections/
│       └── (reserved for future section templates)
│
├── examples/
│   ├── google-calendar/
│   │   └── conceptual-model.md    # Complex example
│   ├── todo-app/
│   │   └── conceptual-model.md    # Simple example
│   └── e-commerce/
│       └── conceptual-model.md    # Medium complexity example
│
├── README.md                      # Main documentation
├── QUICK_START.md                 # Step-by-step tutorial
├── COMMANDS_REFERENCE.md          # Command reference
└── conceptual-model-example-google-calendar.pdf  # Original reference
```

## File Descriptions

### Core Files

#### `.github/copilot-instructions.md`
Custom commands that Claude Code recognizes:
- `concept init` - Initialize new model
- `concept add-object` - Add objects
- `concept add-relationship` - Map relationships
- `concept add-action` - Define workflows
- `concept review` - Review completeness
- `concept generate` - Generate final document
- `concept status` - Quick overview

**Size:** ~15KB  
**Purpose:** Command definitions and guidelines

---

#### `README.md`
Main documentation covering:
- What the kit is
- Why use it
- Quick start
- All commands
- Examples overview
- Best practices
- FAQ

**Size:** ~12KB  
**Purpose:** Primary user documentation

---

#### `QUICK_START.md`
Complete walkthrough creating a RecipeApp model:
- Step-by-step commands
- Sample form responses
- Expected outputs
- Tips specific to the example

**Size:** ~8KB  
**Purpose:** Hands-on tutorial

---

#### `COMMANDS_REFERENCE.md`
Quick reference for all commands:
- Command syntax
- Form fields
- Examples
- Common patterns
- Troubleshooting

**Size:** ~9KB  
**Purpose:** Quick lookup reference

---

### Templates

#### `templates/base-model.md`
Full document structure with placeholders:
- 15 main sections
- All required headings
- Placeholder variables ({{VAR_NAME}})
- Complete table of contents

**Size:** ~5KB  
**Purpose:** Document scaffolding

---

#### `templates/components/object-card.md`
Template for individual object definitions:
- Mental model
- Attributes
- Actions
- System attributes
- Visual representation

**Size:** ~0.5KB  
**Purpose:** Consistent object documentation

---

#### `templates/components/relationship-diagram.md`
Template for relationship documentation:
- Cardinality
- User mental model
- ASCII diagram
- Example usage

**Size:** ~0.3KB  
**Purpose:** Consistent relationship documentation

---

#### `templates/components/workflow-steps.md`
Template for user workflows:
- Mental model
- Sequential steps
- User thoughts
- Objects involved

**Size:** ~0.4KB  
**Purpose:** Consistent workflow documentation

---

### Examples

#### `examples/google-calendar/conceptual-model.md`
**Complexity:** High  
**Objects:** 4+ (Event, Calendar, Reminder, Meeting, etc.)  
**Relationships:** 7+  
**Workflows:** 3+  
**Size:** ~25KB  

**Best for:**
- Learning comprehensive modeling
- Complex applications
- Feature-rich products
- Reference for all sections

**Key features:**
- Multiple object types
- Platform adaptations
- State models
- Error handling
- Progressive disclosure

---

#### `examples/todo-app/conceptual-model.md`
**Complexity:** Low  
**Objects:** 2 (Task, List)  
**Relationships:** 2  
**Workflows:** 3  
**Size:** ~10KB  

**Best for:**
- Getting started
- Simple applications
- Understanding basics
- Quick reference

**Key features:**
- Simple structure
- Clear mental models
- Focused workflows
- Easy to understand

---

#### `examples/e-commerce/conceptual-model.md`
**Complexity:** Medium  
**Objects:** 4 (Product, Cart, Order, Review)  
**Relationships:** 5  
**Workflows:** 5  
**Size:** ~18KB  

**Best for:**
- Most real-world apps
- Balanced complexity
- E-commerce inspiration
- Standard patterns

**Key features:**
- Multiple workflows
- State transitions
- Error scenarios
- Common patterns

---

## Usage Flow

### 1. First Time Setup
```
User reads:
1. README.md (overview)
2. QUICK_START.md (tutorial)
3. Tries: model init MyApp
```

### 2. Building Model
```
User interacts with:
1. .github/copilot-instructions.md (via commands)
2. templates/ (automatically used)
3. examples/ (for reference)
```

### 3. Reference
```
User consults:
1. COMMANDS_REFERENCE.md (command lookup)
2. examples/ (inspiration)
3. README.md (best practices)
```

---

## Generated Files

When users run commands, files are created in their project:

```
your-project/
└── docs/
    ├── conceptual-model-<name>.md        # Working file
    ├── conceptual-model-<name>-final.md  # Generated final
    └── conceptual-model-<name>.pdf       # PDF (if pandoc)
```

**Note:** These files are created in the USER's project, not in the kit itself.

---

## Customization Points

### For Your Organization

1. **Modify commands:**
   - Edit `.github/copilot-instructions.md`
   - Add custom commands
   - Adjust form fields

2. **Customize templates:**
   - Edit `templates/base-model.md`
   - Add/remove sections
   - Change structure

3. **Add examples:**
   - Create `examples/your-domain/`
   - Follow existing structure
   - Document domain-specific patterns

4. **Update docs:**
   - Modify `README.md` with your branding
   - Add company-specific guidelines
   - Include internal links

---

## File Size Summary

```
Total kit size: ~100KB (excluding PDF example)

Breakdown:
- Documentation: ~35KB (README, guides)
- Commands: ~15KB (copilot-instructions.md)
- Templates: ~7KB (base + components)
- Examples: ~55KB (3 complete models)
```

Lightweight and fast to clone/use!

---

## Dependencies

### Required
- None! Pure markdown and text files

### Optional
- **pandoc** - For PDF generation (`concept generate`)
- **Claude Code** or **GitHub Copilot** - To use custom commands

### Recommended
- **Git** - For version control
- **VS Code** - For markdown editing with preview

---

## Version Control

Recommended `.gitignore` for your project:

```
# Ignore working files
docs/conceptual-model-*-working.md

# Ignore generated PDFs (optional - your choice)
docs/*.pdf

# Keep final documents
!docs/*-final.md
```

Recommended to commit:
- Working model: `conceptual-model-<name>.md`
- Final model: `conceptual-model-<name>-final.md`
- (Optional) PDFs for distribution

---

## Updates & Maintenance

To update the kit:

1. **Pull latest version:**
   ```bash
   git pull origin main
   ```

2. **Merge custom changes:**
   - Keep your customized `.github/copilot-instructions.md`
   - Keep your domain-specific examples
   - Update documentation as needed

3. **Version your changes:**
   ```bash
   # In your fork
   git tag v1.0.0
   git push --tags
   ```

---

## Contributing

To contribute improvements:

1. Fork the repository
2. Add your enhancement
3. Test with real examples
4. Submit PR with:
   - Description of change
   - Example usage
   - Updated docs if needed

Common contributions:
- New example domains
- Additional templates
- Command improvements
- Documentation clarity
- Bug fixes

---

## Support

For help:
1. Check `README.md`
2. Try `QUICK_START.md` tutorial
3. Reference `COMMANDS_REFERENCE.md`
4. Review `examples/` for patterns
5. Open issue on GitHub

---

*This structure is designed to be simple, extensible, and easy to customize for your specific needs.*
