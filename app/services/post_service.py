from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post_schema import PostCreate

def create_post(db: Session, text: str, user_id: int):
    new_post = Post(text=text, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
