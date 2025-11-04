# Architecture Fix: Claude Code Integration

## Problem Summary

The Conceptual Kit was not functioning as intended because it lacked proper Claude Code integration. The framework was inspired by GitHub Spec Kit but was missing the critical `.claude/` directory structure that enables slash commands.

## Issues Identified

### 1. **Missing Claude Code Slash Commands**
- ❌ No `.claude/commands/` directory
- ❌ Commands were documented in `.github/copilot-instructions.md` (wrong location for Claude Code)
- ❌ Users couldn't execute `/concept.*` commands inside Claude Code

### 2. **Incorrect Architecture**
The project had:
```
conceptual_kit/cli.py              → CLI Python tool (conceptual init)
.github/copilot-instructions.md    → GitHub Copilot instructions (not Claude Code)
```

But was missing:
```
.claude/commands/                  → Slash commands for Claude Code
```

### 3. **Misleading Documentation**
- README showed examples like `claude-code "concept init MyApp"`
- This syntax doesn't work because:
  - Claude Code doesn't recognize "concept" as a command
  - No slash commands were configured
  - `.github/copilot-instructions.md` is not read by Claude Code

## Solution Implemented

### 1. **Created .claude Directory Structure**

```
.claude/
├── commands/
│   ├── concept-init.md              # /concept.init
│   ├── concept-add-object.md        # /concept.add-object
│   ├── concept-add-relationship.md  # /concept.add-relationship
│   ├── concept-add-action.md        # /concept.add-action
│   ├── concept-review.md            # /concept.review
│   ├── concept-generate.md          # /concept.generate
│   └── concept-status.md            # /concept.status
└── steering/
    └── conceptual-modeling-guide.md
```

### 2. **Updated CLI to Install Slash Commands**

Modified `conceptual_kit/cli.py` to copy `.claude/` directory during `conceptual init`:

```python
# Copy .claude directory (Claude Code slash commands)
claude_src = Path(__file__).parent.parent / ".claude"
claude_dst = target_dir / ".claude"

if claude_src.exists():
    if claude_dst.exists():
        shutil.rmtree(claude_dst)
    shutil.copytree(claude_src, claude_dst)
    console.print(f"✓ Installed Claude Code slash commands (.claude/)")

    # Count commands
    commands_dir = claude_dst / "commands"
    if commands_dir.exists():
        command_files = list(commands_dir.glob("*.md"))
        console.print(f"  → {len(command_files)} slash commands available")
```

### 3. **Updated Package Configuration**

Modified `pyproject.toml` to include `.claude/` in distribution:

```toml
[tool.hatch.build.targets.sdist]
include = [
    "/conceptual_kit",
    "/templates",
    "/examples",
    "/.claude",      # ← ADDED
    "/.github",
    "/README.md",
    "/LICENSE",
    "/conceptual-modeling.md",
]
```

### 4. **Created Comprehensive Slash Command Files**

Each command file includes:
- **Purpose**: Clear explanation of what the command does
- **Usage**: Syntax and parameters
- **Workflow**: Step-by-step execution instructions
- **Examples**: Concrete usage scenarios
- **Error Handling**: How to handle edge cases
- **Best Practices**: Guidelines for quality

Example structure:
```markdown
# /concept.init

## Purpose
Initialize a new conceptual model for an application.

## Usage
/concept.init <app-name>

## Workflow
1. Gather Initial Information (using AskUserQuestion)
2. Create Conceptual Model File
3. Fill Executive Summary
4. Initialize Core Sections
5. Confirm Creation

[... detailed instructions ...]
```

### 5. **Updated Documentation**

**README.md changes:**
- ✅ Clear distinction between CLI tool (`conceptual init`) and slash commands (`/concept.init`)
- ✅ Correct usage examples showing slash commands inside Claude Code
- ✅ Visual project structure showing `.claude/` directory
- ✅ Updated all command examples from `claude-code "concept ..."` to `/concept.*`

**Generated project README:**
- ✅ Lists all available slash commands
- ✅ Shows correct workflow using slash commands
- ✅ References `.claude/` directory structure

## How It Works Now

### Installation Flow

1. **Install CLI Tool** (one time):
   ```bash
   uv tool install conceptual-kit --from git+https://github.com/Lab-Secreto/conceptual-kit.git
   ```

2. **Initialize Project**:
   ```bash
   conceptual init my-project
   cd my-project
   ```

3. **What Gets Installed**:
   ```
   my-project/
   ├── .claude/
   │   ├── commands/              # 7 slash commands
   │   └── steering/              # Guide
   ├── .github/
   │   └── copilot-instructions.md  # For Copilot (optional)
   ├── docs/
   ├── examples/
   └── templates/
   ```

4. **Open Claude Code**:
   ```bash
   claude
   ```

5. **Use Slash Commands** (inside Claude Code):
   ```
   /concept.init MyApp
   /concept.add-object User
   /concept.add-relationship User Post
   /concept.review
   /concept.generate
   ```

### Command Recognition

Claude Code automatically:
1. Scans `.claude/commands/` directory on startup
2. Registers each `.md` file as a slash command
3. Makes commands available via autocomplete
4. Executes command instructions when invoked

## Comparison: Before vs After

| Aspect | Before ❌ | After ✅ |
|--------|----------|---------|
| **Claude Code Integration** | None | Full slash command support |
| **Command Location** | `.github/copilot-instructions.md` | `.claude/commands/*.md` |
| **Commands Available** | 0 | 7 slash commands |
| **Usage** | `claude-code "concept init"` (doesn't work) | `/concept.init` (works) |
| **Auto-complete** | No | Yes |
| **Documentation** | Misleading | Accurate |
| **User Experience** | Broken | Seamless |

## GitHub Spec Kit Alignment

Now properly aligned with GitHub Spec Kit architecture:

| Feature | GitHub Spec Kit | Conceptual Kit |
|---------|----------------|----------------|
| CLI Tool | `specify` | `conceptual` |
| Project Init | `specify init` | `conceptual init` |
| Slash Commands Location | `.claude/commands/` | `.claude/commands/` ✅ |
| Slash Commands | `/speckit.*` | `/concept.*` ✅ |
| Steering Docs | `.claude/steering/` | `.claude/steering/` ✅ |
| Auto-recognition | Yes | Yes ✅ |

## Testing Results

Tested successfully:

```bash
# 1. Install package
✅ uv tool install conceptual-kit --from git+...

# 2. Initialize project
✅ conceptual init /tmp/test-project --ai claude --no-git

# 3. Verify structure
✅ ls .claude/commands/ → 7 files found
✅ cat .claude/commands/concept-init.md → Valid slash command

# 4. Verify installation output
✅ "Installed Claude Code slash commands (.claude/)"
✅ "→ 7 slash commands available"

# 5. Verify README
✅ Shows correct slash command usage
✅ Documents .claude/ directory structure
```

## Files Modified

1. **Created:**
   - `.claude/commands/concept-init.md`
   - `.claude/commands/concept-add-object.md`
   - `.claude/commands/concept-add-relationship.md`
   - `.claude/commands/concept-add-action.md`
   - `.claude/commands/concept-review.md`
   - `.claude/commands/concept-generate.md`
   - `.claude/commands/concept-status.md`
   - `.claude/steering/conceptual-modeling-guide.md`

2. **Modified:**
   - `conceptual_kit/cli.py` (added .claude directory copy logic)
   - `pyproject.toml` (included .claude in distribution)
   - `README.md` (corrected usage examples and documentation)

## Breaking Changes

⚠️ **User Impact:**

**Old (incorrect) usage:**
```bash
claude-code "concept init MyApp"  # Doesn't work
```

**New (correct) usage:**
```bash
# Inside Claude Code:
/concept.init MyApp  # Works!
```

Users following old documentation would have been confused because commands didn't work. Now they work correctly.

## Future Improvements

Potential enhancements:
1. Add more slash commands for advanced workflows
2. Create subagents for complex operations
3. Add validation and linting commands
4. Integration with other AI assistants (Cursor, Windsurf)
5. Interactive command builder

## Conclusion

The Conceptual Kit now works as originally intended, matching the architecture and user experience of GitHub Spec Kit. Users can seamlessly create conceptual models using intuitive slash commands within Claude Code.

**Key Takeaway:** The CLI tool (`conceptual`) bootstraps the project, and the slash commands (`/concept.*`) drive the workflow.
