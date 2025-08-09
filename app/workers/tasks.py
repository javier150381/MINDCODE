from ..services import indexing, whatsapp


def index_document(tenant_id: str, workspace_id: str, path: str):
    indexing.index_document(tenant_id, workspace_id, path)


def handle_whatsapp_message(payload: dict):
    # stub for processing WhatsApp messages
    return payload
