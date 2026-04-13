import anthropic
from debugger.state import DebugState
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

client = anthropic.Anthropic()
 
 
def build_prompt(state: DebugState) -> str:
    sections = [
        f"## Error\n**Type:** {state['error_type']}\n**Message:** {state['error_message']}",
        f"## Full Stacktrace\n```\n{state['raw_input']}\n```",
    ]
 
    if state["file_contents"]:
        file_sections = []
        for path, content in state["file_contents"].items():
            file_sections.append(f"### {path}\n```\n{content}\n```")
        sections.append("## Relevant File Contents\n" + "\n\n".join(file_sections))
 
    sections.append(
        "## Task\n"
        "Analyze this error and provide:\n"
        "1. **Root Cause** — what is actually going wrong and why\n"
        "2. **Fix** — concrete code changes or steps to resolve it\n"
        "3. **Explanation** — brief context so the developer understands the fix\n\n"
        "Be direct and specific. Show corrected code where applicable."
    )
 
    return "\n\n".join(sections)
 
 
def analyze(state: DebugState) -> DebugState:
    prompt = build_prompt(state)
 
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
 
    suggestions = message.content[0].text
    return {**state, "suggestions": suggestions}