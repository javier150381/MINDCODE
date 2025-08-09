from sqlalchemy.orm import Session

from . import models


def get_user_by_email(db: Session, tenant_id: str, email: str):
    return db.query(models.User).filter_by(tenant_id=tenant_id, email=email).first()


def save(db: Session, instance):
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
