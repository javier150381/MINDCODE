from datetime import datetime
from sqlalchemy.orm import Session

from ..db import models


def increment(db: Session, tenant_id: str, metric: str, value: int = 1):
    usage = models.Usage(
        tenant_id=tenant_id,
        metric=metric,
        value=value,
        period_start=datetime.utcnow(),
        period_end=datetime.utcnow(),
    )
    db.add(usage)
    db.commit()
    db.refresh(usage)
    return usage
