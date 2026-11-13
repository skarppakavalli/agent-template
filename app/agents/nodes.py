
from langchain_core.messages import SystemMessage

from app.llm.client import get_llm
from app.agents.tools import tools


# Initialise the model with tool-calling capabilities
llm_with_tools = get_llm().bind_tools(tools)


def assistant_node(state):

    system_message = SystemMessage(
        content="""
        You are a helpful AI agent.

        Use available tools when they are useful.
        Do not call tools unnecessarily.
        Explain the result clearly.
        """
    )

    # Send the system instructions and conversation history
    response = llm_with_tools.invoke(
        [system_message] + state["messages"]
    )

    # Return new message to update graph state
    return {
        "messages": [response]
    }
