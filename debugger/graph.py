from langgraph.graph import StateGraph, END
from debugger.state import DebugState
from debugger.nodes.parse_error import parse_error
from debugger.nodes.read_files import read_files
from debugger.nodes.analyze import analyze
from debugger.nodes.output import output
 
 
def build_graph():
    graph = StateGraph(DebugState)
 
    graph.add_node("parse_error", parse_error)
    graph.add_node("read_files", read_files)
    graph.add_node("analyze", analyze)
    graph.add_node("output", output)
 
    graph.set_entry_point("parse_error")
    graph.add_edge("parse_error", "read_files")
    graph.add_edge("read_files", "analyze")
    graph.add_edge("analyze", "output")
    graph.add_edge("output", END)
 
    return graph.compile()