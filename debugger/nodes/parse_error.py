import re
from debugger.state import DebugState


# Common patterns for file references in stacktraces
FILE_PATTERNS = [
    # Python: File "path/to/file.py", line 42
    r'File "([^"]+\.py)",\s*line\s*(\d+)',
    # Node.js/JS: at Object.<anonymous> (path/to/file.js:42:10)
    r'at .+?\(([^\)]+\.[jt]sx?):(\d+):\d+\)',
    # Generic: path/to/file.ext:line_number
    r'([^\s\(\)"\']+\.[a-zA-Z]+):(\d+)',
]


ERROR_PATTERNS = [
    # Python exceptions
    r'(\w+Error|\w+Exception):\s*(.+)',
    # JS errors
    r'(TypeError|ReferenceError|SyntaxError|Error):\s*(.+)',
]


def parse_error(state: DebugState) -> DebugState:
    raw = state["raw_input"]

    # Extract error type and message
    error_type = "UnknownError"
    error_message = "Could not parse error message."
    for pattern in ERROR_PATTERNS:
        match = re.search(pattern, raw)
        if match:
            error_type = match.group(1)
            error_message = match.group(2)
            break

    
    # Extract file references
    seen_paths = set()
    file_references = []
    for pattern in FILE_PATTERNS:
        for match in re.finditer(pattern, raw):
            path = match.group(1)
            line_number = int(match.group(2))
            if path not in seen_paths:
                seen_paths.add(path)
                file_references.append({"path": path, "line_number": line_number})
 
    # Return the updated state
    return {
        **state,
        "error_type": error_type,
        "error_message": error_message,
        "file_references": file_references,
    }