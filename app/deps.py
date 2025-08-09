from typing import Generator
from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from .db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_tenant(tenant_id: str = Header(...)) -> str:
    return tenant_id


def verify_token(x_token: str = Header(None)):
    if x_token != "fake-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
