from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth_routes, post_routes

app = FastAPI(title="FastAPI MVC App")

# Create database tables if they don’t exist
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(post_routes.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI MVC App"}
