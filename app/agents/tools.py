from langchain_core.tools import tool


@tool
def count_words(text: str) -> int:
    """
    Count the number of words in the provided text.
    Use this when the user asks for a word count.
    """

    return len(text.split())


# Add more tools here when the problem requires them.
tools = [count_words]
