from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Depends
from pydantic import BaseModel

from ..deps import get_tenant
from ..services.indexing import enqueue_index_document, search_index

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/upload")
async def upload(file: UploadFile = File(...), tenant_id: str = Depends(get_tenant)):
    path = Path("data") / file.filename
    path.write_bytes(await file.read())
    enqueue_index_document(tenant_id, path)
    return {"filename": file.filename}


class SearchRequest(BaseModel):
    tenant_id: str
    workspace_id: str
    query: str
    k: int = 5


@router.post("/search")
async def search(req: SearchRequest):
    results = search_index(req.tenant_id, req.workspace_id, req.query, req.k)
    return {"results": results}
