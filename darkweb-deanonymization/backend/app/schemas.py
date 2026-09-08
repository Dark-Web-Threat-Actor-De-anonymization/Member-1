from pydantic import BaseModel

class ActorCreate(BaseModel):
    name: str
    risk_level: str


class HandleCreate(BaseModel):
    actor_id: int
    platform_id: int
    username: str


class WalletCreate(BaseModel):
    actor_id: int
    wallet_address: str


class PostCreate(BaseModel):
    handle_id: int
    content: str