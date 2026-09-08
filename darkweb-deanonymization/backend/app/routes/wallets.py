from fastapi import APIRouter, HTTPException
from app.crud import fetch_all, fetch_one, execute_query

router = APIRouter()

@router.get("/wallets/")
def get_wallets():
    return fetch_all("SELECT * FROM wallets")


@router.post("/wallets/")
def create_wallet(data: dict):
    # ✅ validate actor exists
    actor = fetch_one(
        "SELECT * FROM actors WHERE actor_id = %s",
        (data.get("actor_id"),)
    )

    if not actor:
        raise HTTPException(status_code=400, detail="Invalid actor_id")

    # ✅ insert wallet
    execute_query(
        "INSERT INTO wallets (actor_id, wallet_address) VALUES (%s, %s)",
        (data.get("actor_id"), data.get("wallet_address"))
    )

    return {"message": "Wallet created successfully"}