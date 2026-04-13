from debugger.state import DebugState
 
CONTEXT_LINES = 10  # lines of context to show around the error line
 
 
def read_files(state: DebugState) -> DebugState:
    file_contents = {}
 
    for ref in state["file_references"]:
        path = ref["path"]
        line_number = ref["line_number"]
 
        try:
            with open(path, "r") as f:
                lines = f.readlines()
 
            start = max(0, line_number - CONTEXT_LINES - 1)
            end = min(len(lines), line_number + CONTEXT_LINES)
            context = lines[start:end]
 
            # Annotate lines with numbers, mark the error line
            annotated = []
            for i, line in enumerate(context, start=start + 1):
                marker = ">>>" if i == line_number else "   "
                annotated.append(f"{marker} {i:4d} | {line.rstrip()}")
 
            file_contents[path] = "\n".join(annotated)
 
        except FileNotFoundError:
            file_contents[path] = f"[File not found: {path}]"
        except Exception as e:
            file_contents[path] = f"[Could not read file: {e}]"
 
    return {**state, "file_contents": file_contents}