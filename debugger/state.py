from typing import TypedDict
 
 
class DebugState(TypedDict):
    raw_input: str
    error_type: str
    error_message: str
    file_references: list[dict]  # [{path, line_number}]
    file_contents: dict[str, str]  # {path: content_with_context}
    suggestions: str