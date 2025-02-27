from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.post_service import create_post, get_posts, delete_post
from app.schemas.post_schema import PostCreate, PostResponse
from app.services.auth_service import verify_token

router = APIRouter()

@router.post("/")
def add_post(post_data: PostCreate, token: str, db: Session = Depends(get_db)):
    user = verify_token(token, db)
    return create_post(db, post_data.text, user) 

@router.get("/")
def list_posts(token: str, db: Session = Depends(get_db)):
    user = verify_token(token, db)
    return get_posts(db, user)  


@router.delete("/{post_id}")
def remove_post(post_id: int, token: str, db: Session = Depends(get_db)):
    user = verify_token(token, db)
    return delete_post(db, post_id, user)  # ✅ user.id is now used inside delete_post()

