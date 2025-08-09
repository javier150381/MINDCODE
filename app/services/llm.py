import asyncio
from typing import AsyncGenerator, List, Dict, Any
import httpx

from ..config import settings


class LLMClient:
    def __init__(self):
        self.base_url = settings.DEEPSEEK_API_BASE or "https://api.deepseek.com"

    async def stream(
        self, messages: List[Dict[str, str]], api_key: str | None = None, model: str = "deepseek-chat"
    ) -> AsyncGenerator[str, None]:
        key = api_key or settings.DEEPSEEK_API_KEY
        if not key:
            # fallback stub
            for msg in messages:
                yield msg.get("content", "")
            yield "[DONE]"
            return

        headers = {"Authorization": f"Bearer {key}"}
        async with httpx.AsyncClient() as client:
            # This is a simplified example; real implementation would call the API with streaming
            resp = await client.post(
                f"{self.base_url}/chat/completions",
                json={"model": model, "messages": messages},
                headers=headers,
            )
            data = resp.json()
            yield data.get("choices", [{}])[0].get("message", {}).get("content", "")
            yield "[DONE]"
