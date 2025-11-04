# Changelog

All notable changes to the Conceptual Model Kit will be documented in this file.

## [1.0.0] - 2025-11-03

### Initial Release

#### Added
- Complete Conceptual Model Kit framework
- 7 custom commands for Claude Code
- 3 complete examples (Google Calendar, Todo App, E-Commerce)
- Template system for consistent documentation
- Interactive forms using AskUserQuestion
- ASCII art diagram generation
- PDF export support (requires pandoc)
- Comprehensive documentation (README, Quick Start, Commands Reference)

#### Commands
- `concept init <app-name>` - Initialize new conceptual model
- `concept add-object <name>` - Add objects to model
- `concept add-relationship <from> <to>` - Map relationships
- `concept add-action <name>` - Document workflows
- `concept review` - Review model completeness
- `concept generate` - Generate final document
- `concept status` - Quick progress overview

#### Examples
- **Google Calendar** (complex) - 25KB, comprehensive model
- **Todo App** (simple) - 10KB, beginner-friendly
- **E-Commerce** (medium) - 18KB, real-world patterns

#### Documentation
- `README.md` - Main documentation (12KB)
- `QUICK_START.md` - Step-by-step tutorial (8KB)
- `COMMANDS_REFERENCE.md` - Command reference (9KB)
- `PROJECT_STRUCTURE.md` - Architecture overview (7KB)

#### Templates
- `base-model.md` - Full document structure
- `object-card.md` - Object definition template
- `relationship-diagram.md` - Relationship template
- `workflow-steps.md` - Workflow template

---

## Command Naming

### Why `concept` instead of `model`?

The commands use the prefix `concept` (e.g., `concept init`) instead of `model` to:

1. **Avoid conflicts** with potential native Claude Code commands
2. **Be more specific** - we're creating conceptual models, not data models
3. **Be memorable** - shorter and distinct from technical "model" terminology

### Migration Note

If you have any documentation or scripts using the old `model` prefix, simply replace:
- `model init` → `concept init`
- `model add-object` → `concept add-object`
- `model add-relationship` → `concept add-relationship`
- `model add-action` → `concept add-action`
- `model review` → `concept review`
- `model generate` → `concept generate`
- `model status` → `concept status`

---

## Future Roadmap

### Planned Features

#### v1.1.0 (Next Release)
- [ ] `concept export <format>` - Export to different formats (HTML, Notion, Confluence)
- [ ] `concept validate` - Validate model against best practices
- [ ] `concept compare <v1> <v2>` - Compare different versions
- [ ] Section templates for all document sections
- [ ] More examples (SaaS, Mobile App, API)

#### v1.2.0
- [ ] `concept visualize` - Generate visual diagrams (Mermaid, PlantUML)
- [ ] `concept suggest` - AI-powered suggestions for improvements
- [ ] Interactive mode for guided model creation
- [ ] Integration with design tools (Figma, Sketch)

#### v1.3.0
- [ ] Team collaboration features
- [ ] Version control integration
- [ ] Model templates for common domains
- [ ] Analytics and insights

### Community Contributions Welcome

We welcome contributions for:
- New example domains
- Additional templates
- Language translations
- Tool integrations
- Bug fixes and improvements

See `CONTRIBUTING.md` (coming soon) for guidelines.

---

## Breaking Changes

### v1.0.0
- Initial release, no breaking changes

---

## Known Issues

### v1.0.0

#### PDF Generation
- **Issue:** PDF generation requires `pandoc` to be installed
- **Workaround:** Install pandoc (`brew install pandoc` on macOS) or skip PDF generation
- **Status:** Working as designed

#### Large Models
- **Issue:** Very large models (>50 objects) may be slow to generate
- **Workaround:** Break into multiple models or simplify
- **Status:** Investigating optimization

#### ASCII Diagrams
- **Issue:** Complex relationships may be hard to represent in ASCII
- **Workaround:** Use simpler notation or create external diagrams
- **Status:** Considering Mermaid support for v1.1.0

---

## Support

For issues, questions, or contributions:
- Read the documentation first (README, Quick Start, Commands Reference)
- Check existing issues on GitHub
- Create a new issue with:
  - Clear description
  - Steps to reproduce (if bug)
  - Expected vs actual behavior
  - Your environment (OS, Claude Code version)

---

## Credits

### Inspiration
- [GitHub Spec Kit](https://github.com/github/spec-kit) - Command structure and workflow
- Johnson & Henderson - Conceptual Models Framework (1991)
- Don Norman - "The Design of Everyday Things"

### Created By
- Conceptual Model Kit Team
- With assistance from Claude (Anthropic)

### License
MIT License - See LICENSE file for details

---

*Last updated: 2025-11-03*
