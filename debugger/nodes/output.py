from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from debugger.state import DebugState
 
console = Console()
 
 
def output(state: DebugState) -> DebugState:
    # Header
    console.print()
    console.print(Panel(
        Text(f"{state['error_type']}: {state['error_message']}", style="bold red"),
        title="[bold]Error Detected[/bold]",
        border_style="red",
    ))
 
    # Files read
    if state["file_references"]:
        console.print("\n[bold yellow]Files Analyzed:[/bold yellow]")
        for ref in state["file_references"]:
            console.print(f"  • {ref['path']} (line {ref['line_number']})")
 
    # Suggestions
    console.print("\n[bold green]Analysis & Fix:[/bold green]\n")
    console.print(Markdown(state["suggestions"]))
    console.print()
 
    return state
 