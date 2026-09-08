from fastapi import APIRouter

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(q: str = ""):
    return {"query": q}