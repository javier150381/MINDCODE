from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login():
    return {"access_token": "fake", "refresh_token": "fake"}


@router.post("/refresh")
def refresh():
    return {"access_token": "fake"}
