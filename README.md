# ShardSockyt
An agentic debugging tool built with LangGraph and Claude. Paste a stacktrace into the CLI and get a diagnosis + fix suggestion.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

## Usage

```bash
python -m debugger.main
```

Paste your stacktrace, then enter a blank line followed by `END`.

## How it works

The tool runs a 4-node LangGraph pipeline:

1. **parse_error** — extracts error type, message, and file references from the stacktrace
2. **read_files** — reads each referenced file, pulling ±10 lines of context around the error line
3. **analyze** — sends everything to Claude and gets back a root cause analysis + fix
4. **output** — renders the result in the terminal using Rich

## Project Structure

```
debugger/
├── main.py          # CLI entrypoint
├── graph.py         # LangGraph graph definition
├── state.py         # Shared state (TypedDict)
├── nodes/
│   ├── parse_error.py
│   ├── read_files.py
│   ├── analyze.py
│   └── output.py
├── requirements.txt
└── .env.example
```
