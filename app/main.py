from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import health, auth, chat, rag, whatsapp, billing

app = FastAPI(title="MindChat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(rag.router)
app.include_router(whatsapp.router)
app.include_router(billing.router)


@app.get("/")
def root():
    return {"name": "MindChat", "version": "0.1.0"}


# Run with: uvicorn app.main:app --reload
