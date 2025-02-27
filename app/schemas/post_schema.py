from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str
    user_id: int

    class Config:
        from_attributes = True
