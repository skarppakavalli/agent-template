
from app.llm.client import get_llm
from app.llm.prompts import CHAT_PROMPT

from app.core.logging_config import logger


def ask_llm(question: str) -> str:

    try:
        llm = get_llm()

        # Combine prompt and model into a runnable chain
        chain = CHAT_PROMPT | llm

        # Invoke the chain with input variables
        response = chain.invoke({
            "question": question
        })

        return response.content

    except Exception:
        logger.exception("LLM invocation failed")
        raise
