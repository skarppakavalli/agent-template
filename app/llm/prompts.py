
from langchain_core.prompts import ChatPromptTemplate


# Basic chatbot prompt
CHAT_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful AI assistant.

        Instructions:
        - Give accurate answers.
        - Do not invent information.
        - If you do not know something, say so.
        - Keep answers structured and understandable.
        """
    ),
    ("human", "{question}")
])


# Example prompt for structured evaluation
EVALUATION_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an evaluator.

        Evaluate the user's answer based on:
        1. Correctness
        2. Completeness
        3. Clarity

        Explain your reasoning.
        """
    ),
    (
        "human",
        """
        Question: {question}

        Answer: {answer}
        """
    )
])
