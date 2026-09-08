from fastapi import APIRouter, HTTPException
from app.crud import fetch_all, fetch_one, execute_query

router = APIRouter()

@router.get("/posts/")
def get_posts():
    return fetch_all("SELECT * FROM posts")


@router.post("/posts/")
def create_post(data: dict):
    # ✅ validate handle exists
    handle = fetch_one(
        "SELECT * FROM handles WHERE handle_id = %s",
        (data.get("handle_id"),)
    )

    if not handle:
        raise HTTPException(status_code=400, detail="Invalid handle_id")

    # ✅ insert post
    execute_query(
        "INSERT INTO posts (handle_id, content) VALUES (%s, %s)",
        (data.get("handle_id"), data.get("content"))
    )

    return {"message": "Post created successfully"}