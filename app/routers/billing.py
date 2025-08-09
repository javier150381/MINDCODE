from fastapi import APIRouter, Request, HTTPException

from ..config import settings

router = APIRouter(prefix="/webhook/stripe", tags=["billing"])


@router.post("")
async def stripe_webhook(request: Request):
    signature = request.headers.get("stripe-signature")
    if signature != settings.STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=400, detail="Invalid signature")
    payload = await request.json()
    # handle events here
    return {"received": True}
