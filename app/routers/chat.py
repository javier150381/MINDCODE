from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ..services.llm import LLMClient

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    tenant_id: str
    workspace_id: str
    messages: list[ChatMessage]
    api_key: str | None = None


@router.post("")
async def chat(req: ChatRequest):
    client = LLMClient()

    async def event_generator():
        async for chunk in client.stream([m.dict() for m in req.messages], api_key=req.api_key):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

# For WebSocket implementation, replace the above with a WebSocket endpoint using websockets.
