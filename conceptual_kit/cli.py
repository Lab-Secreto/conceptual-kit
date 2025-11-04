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


def get_templates_path() -> Path:
    """Get the path to the templates directory."""
    # When installed, templates are packaged with the module
    package_dir = Path(__file__).parent.parent
    templates_dir = package_dir / "templates"

    if templates_dir.exists():
        return templates_dir

    # Fallback to development location
    return Path.cwd() / "templates"


def get_examples_path() -> Path:
    """Get the path to the examples directory."""
    package_dir = Path(__file__).parent.parent
    examples_dir = package_dir / "examples"

    if examples_dir.exists():
        return examples_dir

    return Path.cwd() / "examples"


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
    templates_src = get_templates_path()
    templates_dst = target_dir / "templates"

    if templates_src.exists():
        if templates_dst.exists():
            shutil.rmtree(templates_dst)
        shutil.copytree(templates_src, templates_dst)
        console.print(f"✓ Copied templates to {templates_dst}")
    else:
        console.print("[yellow]Warning: Templates directory not found[/yellow]")

    # Copy examples
    examples_src = get_examples_path()
    examples_dst = target_dir / "examples"

    if examples_src.exists():
        if examples_dst.exists():
            shutil.rmtree(examples_dst)
        shutil.copytree(examples_src, examples_dst)
        console.print(f"✓ Copied examples to {examples_dst}")
    else:
        console.print("[yellow]Warning: Examples directory not found[/yellow]")

    # Create docs directory
    docs_dir = target_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    console.print(f"✓ Created docs directory")

    # Create .github directory and copilot instructions
    github_dir = target_dir / ".github"
    github_dir.mkdir(exist_ok=True)

    # Copy copilot instructions from source
    source_instructions = Path(__file__).parent.parent / ".github" / "copilot-instructions.md"
    if source_instructions.exists():
        shutil.copy(source_instructions, github_dir / "copilot-instructions.md")
        console.print(f"✓ Created AI assistant configuration for {ai}")

    # Create conceptual-modeling.md
    conceptual_modeling_src = Path(__file__).parent.parent / "conceptual-modeling.md"
    if conceptual_modeling_src.exists():
        shutil.copy(conceptual_modeling_src, target_dir / "conceptual-modeling.md")
        console.print(f"✓ Copied conceptual modeling guide")

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

### Create your first conceptual model

```bash
# Initialize a model
{ai if ai == 'claude' else 'your-ai'} "concept init {project_name}"

# Add objects
{ai if ai == 'claude' else 'your-ai'} "concept add-object User"
{ai if ai == 'claude' else 'your-ai'} "concept add-object Post"

# Map relationships
{ai if ai == 'claude' else 'your-ai'} "concept add-relationship User Post"

# Review your model
{ai if ai == 'claude' else 'your-ai'} "concept review"

# Generate final document
{ai if ai == 'claude' else 'your-ai'} "concept generate"
```

## Documentation

- See `conceptual-modeling.md` for the philosophy and principles
- Check `examples/` for reference models
- Review `templates/` for document structure

## Available Commands

- `concept init <name>` - Start a new conceptual model
- `concept add-object <name>` - Add an object to your model
- `concept add-relationship <from> <to>` - Map object relationships
- `concept add-action <name>` - Document user workflows
- `concept review` - Get feedback on your model
- `concept generate` - Create final formatted document
- `concept status` - Quick model overview

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
