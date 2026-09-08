from fastapi import APIRouter, HTTPException
from app.crud import fetch_one, fetch_all

router = APIRouter(prefix="/actor", tags=["Profile"])

def calculate_risk(handles_count, wallets_count, posts_count, base=None):
    score = 0

    if base == 'High':
        score += 2
    elif base == 'Medium':
        score += 1

    if handles_count >= 3:
        score += 2
    elif handles_count == 2:
        score += 1

    if wallets_count >= 2:
        score += 2
    elif wallets_count == 1:
        score += 1

    if posts_count >= 20:
        score += 2
    elif posts_count >= 5:
        score += 1

    if score >= 5:
        return 'High'
    elif score >= 2:
        return 'Medium'
    return 'Low'


@router.get("/{actor_id}")
def get_profile(actor_id: int):
    actor = fetch_one("SELECT actor_id, name, risk_level FROM actors WHERE actor_id = %s", (actor_id,))
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")

    handles = fetch_all("SELECT handle_id FROM handles WHERE actor_id = %s", (actor_id,))
    wallets = fetch_all("SELECT wallet_id FROM wallets WHERE actor_id = %s", (actor_id,))
    posts = fetch_all(
        "SELECT p.post_id FROM posts p JOIN handles h ON p.handle_id = h.handle_id WHERE h.actor_id = %s",
        (actor_id,)
    )

    return {
        "actor": actor,
        "handles": handles,
        "wallets": wallets,
        "posts": posts,
        "calculated_risk": calculate_risk(len(handles), len(wallets), len(posts), actor.get('risk_level'))
    }