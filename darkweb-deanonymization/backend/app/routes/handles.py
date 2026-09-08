from fastapi import APIRouter, HTTPException
from app.crud import fetch_one, fetch_all

router = APIRouter(prefix="/handles", tags=["Handles"])


# 🔹 Get all handles
@router.get("/", summary="Get all handles")
def get_handles():
    handles = fetch_all("SELECT * FROM handles")
    return {"handles": handles}


# 🔹 Get handle by ID
@router.get("/{handle_id}", summary="Get handle by ID")
def get_handle(handle_id: int):
    handle = fetch_one(
        "SELECT handle_id, username, platform_id, actor_id FROM handles WHERE handle_id = %s",
        (handle_id,)
    )

    if not handle:
        raise HTTPException(status_code=404, detail="Handle not found")

    return {"handle": handle}


# 🔹 Get handles for an actor
@router.get("/actor/{actor_id}", summary="Get handles by actor")
def get_handles_by_actor(actor_id: int):
    handles = fetch_all(
        "SELECT handle_id, username, platform_id FROM handles WHERE actor_id = %s",
        (actor_id,)
    )

    return {"handles": handles}