from pathlib import Path
import numpy as np

DATA_DIR = Path("data/faiss")


def _index_path(tenant_id: str, workspace_id: str) -> Path:
    return DATA_DIR / tenant_id / f"{workspace_id}.index"


def load_index(tenant_id: str, workspace_id: str, dim: int):
    import faiss  # imported lazily
    path = _index_path(tenant_id, workspace_id)
    if path.exists():
        return faiss.read_index(str(path))
    return faiss.IndexFlatL2(dim)


def save_index(tenant_id: str, workspace_id: str, index) -> None:
    import faiss
    path = _index_path(tenant_id, workspace_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(path))


def search(tenant_id: str, workspace_id: str, query_vec, k: int = 5):
    import faiss
    index = load_index(tenant_id, workspace_id, len(query_vec))
    D, I = index.search(np.array([query_vec]).astype("float32"), k)
    return I[0].tolist()


def add_vectors(tenant_id: str, workspace_id: str, vectors: np.ndarray):
    index = load_index(tenant_id, workspace_id, vectors.shape[1])
    index.add(vectors)
    save_index(tenant_id, workspace_id, index)
