from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post_schema import PostCreate
from cachetools import TTLCache
import time

# Cache that stores up to 100 users' posts for 5 minutes (300 seconds)
post_cache = TTLCache(maxsize=100, ttl=300)


def create_post(db: Session, text: str, user):
    new_post = Post(text=text, user_id=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # Update cache for this user
    if user.id in post_cache:
        post_cache[user.id].append(new_post)
    else:
        post_cache[user.id] = [new_post]

    print("🆕 Post added and cache updated")

    return new_post


def get_posts(db: Session, user):
    # Check if posts are in cache
    if user.id in post_cache:
        print("✅ Returning cached posts")
        return post_cache[user.id]

    # Otherwise, fetch from DB
    posts = db.query(Post).filter(Post.user_id == user.id).all()

    # Store result in cache
    post_cache[user.id] = posts
    print("🆕 Fetched from DB and cached")

    return posts


def delete_post(db: Session, post_id: int, user):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()

    # Remove post from cache if it exists
    if user.id in post_cache:
        post_cache[user.id] = [p for p in post_cache[user.id] if p.id != post_id]

    print("❌ Post deleted and cache updated")

    return {"message": "Post deleted successfully"}



