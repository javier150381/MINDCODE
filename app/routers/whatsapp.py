from fastapi import APIRouter, HTTPException, Request, Response
from redis import Redis
from rq import Queue

from ..config import settings
from ..workers import tasks

router = APIRouter(prefix="/webhook/whatsapp", tags=["whatsapp"])

redis_conn = Redis.from_url(settings.REDIS_URL)
queue = Queue("default", connection=redis_conn)


@router.get("")
def verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    if mode == "subscribe" and token == settings.META_WA_VERIFY_TOKEN:
        return Response(content=challenge)
    raise HTTPException(status_code=400, detail="Invalid token")


@router.post("")
async def webhook(payload: dict):
    queue.enqueue(tasks.handle_whatsapp_message, payload)
    return {"status": "queued"}
