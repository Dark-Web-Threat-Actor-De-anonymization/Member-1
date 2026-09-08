from fastapi import APIRouter, HTTPException
from app.crud import fetch_one, fetch_all

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.get("/", summary="Get all actors")
def get_actors():
    return {"actors": fetch_all("SELECT * FROM actors")}

@router.get("/{actor_id}", summary="Get actor by ID")
def get_actor(actor_id: int):
    actor = fetch_one(
        "SELECT actor_id, name, risk_level FROM actors WHERE actor_id = %s",
        (actor_id,)
    )
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {"actor": actor}

@router.get("/{actor_id}/details", summary="Actor with handles and wallets")
def get_actor_details(actor_id: int):
    actor = fetch_one(
        "SELECT actor_id, name, risk_level FROM actors WHERE actor_id = %s",
        (actor_id,)
    )
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")

    handles = fetch_all(
        "SELECT handle_id, username, platform_id FROM handles WHERE actor_id = %s",
        (actor_id,)
    )
    wallets = fetch_all(
        "SELECT wallet_id, wallet_address FROM wallets WHERE actor_id = %s",
        (actor_id,)
    )

    return {"actor": actor, "handles": handles, "wallets": wallets}