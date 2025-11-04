#!/usr/bin/env python3
"""
Conceptual Kit CLI - Command-line interface for conceptual modeling.
"""

import os
import sys
import shutil
from pathlib import Path
from typing import Optional
import click
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich import box

console = Console()


def get_data_path(subdir: str, debug: bool = False) -> Path:
    """Get the path to a data directory (templates, examples, .claude, etc)."""
    # Try multiple locations in order of preference
    import sys

    # 1. Development mode: relative to package
    package_dir = Path(__file__).parent.parent
    dev_path = package_dir / subdir
    if debug:
        console.print(f"[dim]Checking dev path: {dev_path} (exists: {dev_path.exists()})[/dim]")
    if dev_path.exists():
        return dev_path

    # 2. Installed via wheel: in share directory
    if sys.prefix != sys.base_prefix:  # In a virtual environment
        share_path = Path(sys.prefix) / "share" / "conceptual_kit" / subdir
        if debug:
            console.print(f"[dim]Checking venv share path: {share_path} (exists: {share_path.exists()})[/dim]")
        if share_path.exists():
            return share_path

    # 3. Global installation
    share_path = Path(sys.prefix) / "share" / "conceptual_kit" / subdir
    if debug:
        console.print(f"[dim]Checking global share path: {share_path} (exists: {share_path.exists()})[/dim]")
    if share_path.exists():
        return share_path

    # 4. Fallback to return the dev path even if it doesn't exist (for error messages)
    if debug:
        console.print(f"[dim]Fallback to: {dev_path}[/dim]")
    return dev_path


def get_templates_path() -> Path:
    """Get the path to the templates directory."""
    return get_data_path("templates")


def get_examples_path() -> Path:
    """Get the path to the examples directory."""
    return get_data_path("examples")


def get_claude_path() -> Path:
    """Get the path to the .claude directory."""
    return get_data_path(".claude")


def get_github_path() -> Path:
    """Get the path to the .github directory."""
    return get_data_path(".github")


def get_conceptual_modeling_path(debug: bool = False) -> Path:
    """Get the path to the conceptual-modeling.md file."""
    # Try multiple locations
    package_dir = Path(__file__).parent.parent
    import sys

    # 1. Development mode
    dev_path = package_dir / "conceptual-modeling.md"
    if debug:
        console.print(f"[dim]Checking conceptual-modeling.md at: {dev_path} (exists: {dev_path.exists()})[/dim]")
    if dev_path.exists():
        return dev_path

    # 2. Installed via wheel
    if sys.prefix != sys.base_prefix:
        share_path = Path(sys.prefix) / "share" / "conceptual_kit" / "conceptual-modeling.md"
        if debug:
            console.print(f"[dim]Checking venv share path: {share_path} (exists: {share_path.exists()})[/dim]")
        if share_path.exists():
            return share_path

    # 3. Global installation
    share_path = Path(sys.prefix) / "share" / "conceptual_kit" / "conceptual-modeling.md"
    if debug:
        console.print(f"[dim]Checking global share path: {share_path} (exists: {share_path.exists()})[/dim]")
    if share_path.exists():
        return share_path

    return dev_path


@click.group()
@click.version_option(version="0.1.0", prog_name="conceptual")
def main() -> None:
    """
    Conceptual Kit - Create comprehensive conceptual models for your applications.

    Based on Johnson & Henderson's Conceptual Models Framework.
    """
    pass


@main.command()
@click.argument("project_name", required=False)
@click.option("--ai", type=click.Choice(["claude", "copilot", "cursor-agent", "windsurf", "amp", "gemini"]),
              default="claude", help="AI assistant to configure for")
@click.option("--script", type=click.Choice(["sh", "ps"]), default="sh",
              help="Script type (sh for bash, ps for PowerShell)")
@click.option("--here", is_flag=True, help="Initialize in current directory")
@click.option("--force", is_flag=True, help="Force initialization in non-empty directory")
@click.option("--no-git", is_flag=True, help="Skip git initialization")
@click.option("--debug", is_flag=True, help="Enable debug output")
@click.option("--github-token", help="GitHub token for API requests")
def init(
    project_name: Optional[str],
    ai: str,
    script: str,
    here: bool,
    force: bool,
    no_git: bool,
    debug: bool,
    github_token: Optional[str]
) -> None:
    """
    Initialize a new conceptual modeling project.

    Examples:

        # Basic project initialization
        conceptual init my-project

        # Initialize with specific AI assistant
        conceptual init my-project --ai claude

        # Initialize in current directory
        conceptual init . --ai copilot
        # or use the --here flag
        conceptual init --here --ai copilot

        # Force initialization in non-empty directory
        conceptual init . --force --ai copilot

        # Skip git initialization
        conceptual init my-project --ai gemini --no-git
    """
    if debug:
        console.print("[dim]Debug mode enabled[/dim]")

    # Determine target directory
    if here or project_name == ".":
        target_dir = Path.cwd()
        project_name = target_dir.name
    elif project_name:
        target_dir = Path.cwd() / project_name
    else:
        console.print("[red]Error: Project name required (or use --here)[/red]")
        sys.exit(1)

    # Check if directory exists and is not empty
    if target_dir.exists() and any(target_dir.iterdir()) and not force:
        console.print(f"[red]Error: Directory {target_dir} is not empty. Use --force to override.[/red]")
        sys.exit(1)

    # Create directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    console.print(Panel.fit(
        f"[bold green]Initializing Conceptual Model Kit[/bold green]\n"
        f"Project: {project_name}\n"
        f"AI Assistant: {ai}\n"
        f"Location: {target_dir}",
        border_style="green"
    ))

    # Copy templates
    templates_src = get_data_path("templates", debug)
    templates_dst = target_dir / "templates"

    if templates_src.exists():
        if templates_dst.exists():
            shutil.rmtree(templates_dst)
        shutil.copytree(templates_src, templates_dst)
        console.print(f"✓ Copied templates to {templates_dst}")
    else:
        console.print("[yellow]Warning: Templates directory not found[/yellow]")
        if debug:
            console.print(f"[dim]Searched at: {templates_src}[/dim]")

    # Copy examples
    examples_src = get_data_path("examples", debug)
    examples_dst = target_dir / "examples"

    if examples_src.exists():
        if examples_dst.exists():
            shutil.rmtree(examples_dst)
        shutil.copytree(examples_src, examples_dst)
        console.print(f"✓ Copied examples to {examples_dst}")
    else:
        console.print("[yellow]Warning: Examples directory not found[/yellow]")
        if debug:
            console.print(f"[dim]Searched at: {examples_src}[/dim]")

    # Create docs directory
    docs_dir = target_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    console.print(f"✓ Created docs directory")

    # Copy .claude directory (Claude Code slash commands)
    claude_src = get_data_path(".claude", debug)
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
    else:
        console.print("[yellow]Warning: .claude directory not found[/yellow]")
        if debug:
            console.print(f"[dim]Searched at: {claude_src}[/dim]")

    # Create .github directory and copilot instructions (for GitHub Copilot compatibility)
    github_src = get_data_path(".github", debug)
    github_dst = target_dir / ".github"
    github_dst.mkdir(exist_ok=True)

    # Copy copilot instructions from source
    copilot_instructions = github_src / "copilot-instructions.md"
    if copilot_instructions.exists():
        shutil.copy(copilot_instructions, github_dst / "copilot-instructions.md")
        console.print(f"✓ Created GitHub Copilot configuration (.github/)")
    else:
        if debug:
            console.print(f"[dim]Copilot instructions not found at: {copilot_instructions}[/dim]")

    # Copy conceptual-modeling.md to project root
    conceptual_modeling_src = get_conceptual_modeling_path(debug)
    if conceptual_modeling_src.exists():
        shutil.copy(conceptual_modeling_src, target_dir / "conceptual-modeling.md")
        console.print(f"✓ Copied conceptual modeling guide")
    else:
        if debug:
            console.print(f"[dim]Conceptual modeling guide not found at: {conceptual_modeling_src}[/dim]")

    # Initialize git if requested
    if not no_git:
        try:
            import subprocess
            subprocess.run(["git", "init"], cwd=target_dir, check=True, capture_output=True)
            console.print("✓ Initialized git repository")

            # Create .gitignore
            gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Generated files
*.pdf
*-final.md
"""
            (target_dir / ".gitignore").write_text(gitignore_content)
            console.print("✓ Created .gitignore")

        except (subprocess.CalledProcessError, FileNotFoundError):
            console.print("[yellow]Warning: Could not initialize git repository[/yellow]")

    # Create README
    readme_content = f"""# {project_name}

Conceptual Model Kit Project

## Getting Started

This project has been configured with **Claude Code slash commands** for creating conceptual models.

### Available Slash Commands

When using Claude Code in this project, you have access to these commands:

- `/concept.init <name>` - Start a new conceptual model
- `/concept.add-object <name>` - Add an object to your model
- `/concept.add-relationship <from> <to>` - Map object relationships
- `/concept.add-action <name>` - Document user workflows
- `/concept.review` - Get comprehensive feedback on your model
- `/concept.generate` - Create final formatted document
- `/concept.status` - Quick model overview

### Create Your First Conceptual Model

```bash
# 1. Open Claude Code in this directory
claude

# 2. Inside Claude Code, use slash commands:
/concept.init {project_name}

# 3. Add your core objects
/concept.add-object User
/concept.add-object Post
/concept.add-object Comment

# 4. Map relationships
/concept.add-relationship User Post
/concept.add-relationship Post Comment

# 5. Add user workflows
/concept.add-action create-post
/concept.add-action add-comment

# 6. Review your model
/concept.review

# 7. Generate final document
/concept.generate
```

## Documentation

- See `.claude/steering/conceptual-modeling-guide.md` for the philosophy and principles
- Check `examples/` for reference models at different complexity levels
- Review `templates/` for document structure
- See `.claude/commands/` for detailed command documentation

## Command Details

Each slash command in `.claude/commands/` provides:
- Detailed workflow instructions
- Interactive forms for gathering information
- Best practices and examples
- Error handling guidance

## Project Structure

```
{project_name}/
├── .claude/
│   ├── commands/          # Slash commands for Claude Code
│   └── steering/          # Conceptual modeling guide
├── docs/                  # Your conceptual models go here
├── examples/              # Reference models
│   ├── todo-app/         # Simple example
│   ├── e-commerce/       # Medium complexity
│   └── google-calendar/  # Complex example
└── templates/            # Document templates

## Resources

- [Johnson & Henderson - Conceptual Models](https://www.sciencedirect.com/science/article/abs/pii/S0953543805800340)
- [The Design of Everyday Things - Don Norman](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things)

---

Generated with Conceptual Kit
"""
    (target_dir / "README.md").write_text(readme_content)
    console.print("✓ Created README.md")

    # Success message
    console.print()
    console.print(Panel.fit(
        "[bold green]✓ Project initialized successfully![/bold green]\n\n"
        f"[bold]Next steps:[/bold]\n"
        f"1. cd {project_name if not here else '.'}\n"
        f"2. Read conceptual-modeling.md to understand the approach\n"
        f"3. Check examples/ for reference models\n"
        f"4. Start modeling: {ai if ai == 'claude' else 'your-ai'} 'concept init MyApp'\n\n"
        f"[dim]Happy modeling! 🎨🧠[/dim]",
        border_style="green",
        title="Success"
    ))


@main.command()
def check() -> None:
    """Check system requirements and configuration."""
    console.print(Panel.fit("[bold]Conceptual Kit - System Check[/bold]", border_style="blue"))

    table = Table(title="System Requirements", box=box.ROUNDED)
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Notes")

    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    python_ok = sys.version_info >= (3, 8)
    table.add_row(
        "Python",
        "✓" if python_ok else "✗",
        f"Version {python_version} {'(OK)' if python_ok else '(Need 3.8+)'}"
    )

    # Check for pandoc (optional)
    pandoc_available = shutil.which("pandoc") is not None
    table.add_row(
        "Pandoc (PDF generation)",
        "✓" if pandoc_available else "○",
        "Installed" if pandoc_available else "Optional - install for PDF export"
    )

    # Check for git
    git_available = shutil.which("git") is not None
    table.add_row(
        "Git",
        "✓" if git_available else "○",
        "Installed" if git_available else "Optional - for version control"
    )

    # Check templates availability
    templates_path = get_templates_path()
    templates_ok = templates_path.exists()
    table.add_row(
        "Templates",
        "✓" if templates_ok else "✗",
        f"Found at {templates_path}" if templates_ok else "Not found"
    )

    # Check examples availability
    examples_path = get_examples_path()
    examples_ok = examples_path.exists()
    table.add_row(
        "Examples",
        "✓" if examples_ok else "✗",
        f"Found at {examples_path}" if examples_ok else "Not found"
    )

    # Check .claude directory availability
    claude_path = get_claude_path()
    claude_ok = claude_path.exists()
    table.add_row(
        "Claude Commands",
        "✓" if claude_ok else "✗",
        f"Found at {claude_path}" if claude_ok else "Not found"
    )

    console.print(table)
    console.print()

    if not python_ok:
        console.print("[red]Error: Python 3.8 or higher is required[/red]")
        sys.exit(1)

    if not templates_ok or not examples_ok:
        console.print("[yellow]Warning: Some resources are missing. Try reinstalling the package.[/yellow]")

    console.print("[green]✓ System check complete[/green]")


@main.command()
def version() -> None:
    """Show version information."""
    from conceptual_kit import __version__
    console.print(f"[bold]Conceptual Kit[/bold] version [cyan]{__version__}[/cyan]")


if __name__ == "__main__":
    main()
