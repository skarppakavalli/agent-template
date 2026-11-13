from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from app.agents.state import AgentState
from app.agents.nodes import assistant_node
from app.agents.tools import tools


# Create the graph
graph_builder = StateGraph(AgentState)

# Register nodes
graph_builder.add_node("assistant", assistant_node)
graph_builder.add_node("tools", ToolNode(tools))

# Starting point
graph_builder.add_edge(START, "assistant")

# If LLM requests a tool, execute it.
# Otherwise, finish the workflow.
graph_builder.add_conditional_edges(
    "assistant",
    tools_condition
)

# After tool execution, return to the assistant.
graph_builder.add_edge("tools", "assistant")

# Compile graph into an executable workflow
agent = graph_builder.compile()
