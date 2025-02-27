from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post_schema import PostCreate

def create_post(db: Session, text: str, user):
    new_post = Post(text=text, user_id=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_posts(db: Session, user):
    return db.query(Post).filter(Post.user_id == user.id).all()

def delete_post(db: Session, post_id: int, user):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

