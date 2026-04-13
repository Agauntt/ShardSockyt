import sys
from rich.console import Console
from rich.prompt import Prompt
from debugger.graph import build_graph

console = Console()

console.print("[bold green]Welcome to the ShardSockyt Debugger![/bold green]")

def get_user_input():
    """Collect multi-line input from the user."""
    console.print("\n[bold cyan]AI Debugger[/bold cyan] — Paste your error or stacktrace below.")
    console.print("[dim]When done, enter a blank line followed by END on its own line.[/dim]\n")
    lines = []
    while True:
        try:
            line = Prompt.ask("[bold blue]>[/bold blue]")
            if line == "END":
                break
            lines.append(line)
        except EOFError:
            break

    return "\n".join(lines)

def main():
    raw_input = get_user_input()

    if not raw_input:
        console.print("[bold red]No input provided. Exiting.[/bold red]")
        sys.exit(1)

    console.print("\n[dim]Analyzing...[/dim]\n")

    graph = build_graph()
    graph.invoke({
        "raw_input": raw_input,
        "error_type": "",
        "error_message": "",
        "file_references": [],
        "file_contents": {},
        "suggestions": "",
    })


if __name__ == "__main__":
    main()