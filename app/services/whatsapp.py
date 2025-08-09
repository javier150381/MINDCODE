import httpx

from ..config import settings


async def send_text(to: str, message: str):
    headers = {"Authorization": f"Bearer {settings.META_WA_TOKEN}"}
    async with httpx.AsyncClient() as client:
        await client.post("https://graph.facebook.com/messages", json={"to": to, "text": message}, headers=headers)


def verify_token(token: str) -> bool:
    return token == settings.META_WA_VERIFY_TOKEN
