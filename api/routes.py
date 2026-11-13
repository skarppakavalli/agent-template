
from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage

from app.schemas.request import ChatRequest, ChatResponse
from app.agents.workflow import agent

from app.core.logging_config import logger


router = APIRouter()


@router.get("/health")
def health_check():

    return {"status": "healthy"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        # Start a new agent conversation for this request
        result = agent.invoke({
            "messages": [
                HumanMessage(content=request.question)
            ]
        })

        # Get the final message
        answer = result["messages"][-1].content

        return ChatResponse(answer=answer)

    except Exception:

        logger.exception("Agent execution failed")

        raise HTTPException(
            status_code=500,
            detail="Unable to process request"
        )
