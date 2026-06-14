from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def matches():
    return {"status": "ok"}