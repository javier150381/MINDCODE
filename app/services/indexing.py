from pathlib import Path
import numpy as np
from redis import Redis
from rq import Queue

from ..config import settings
from . import vectorstore

redis_conn = Redis.from_url(settings.REDIS_URL)
queue = Queue("indexing", connection=redis_conn)


def chunk_text(text: str, size: int = 500):
    return [text[i : i + size] for i in range(0, len(text), size)]


def embed_text(text: str) -> np.ndarray:
    # simple stub returning random vectors
    return np.random.rand(768).astype("float32")


def index_chunks(tenant_id: str, workspace_id: str, chunks: list[str]):
    vectors = np.vstack([embed_text(c) for c in chunks])
    vectorstore.add_vectors(tenant_id, workspace_id, vectors)


def index_document(tenant_id: str, workspace_id: str, path: str):
    text = Path(path).read_text()
    chunks = chunk_text(text)
    index_chunks(tenant_id, workspace_id, chunks)


def enqueue_index_document(tenant_id: str, path: Path, workspace_id: str = "default"):
    queue.enqueue(index_document, tenant_id, workspace_id, str(path))


def search_index(tenant_id: str, workspace_id: str, query: str, k: int = 5):
    vec = embed_text(query)
    ids = vectorstore.search(tenant_id, workspace_id, vec, k)
    return ids
