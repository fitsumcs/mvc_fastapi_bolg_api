# FastAPI MVC Web Application

This is a FastAPI-based web application that follows the **MVC pattern**. It includes:

- **Authentication** (Signup/Login with JWT)
- **CRUD operations for posts**
- **SQLAlchemy ORM**
- **Pydantic request validation**
- **Dependency Injection**
- **Caching (Redis/FastAPI Cache)**

## 🛠️ Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/your-repo/fastapi_mvc_app.git
cd fastapi_mvc_app
```

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Configure Environment Variables

DATABASE_URL="mysql+pymysql://user:password@localhost:3306/mydatabase"
SECRET_KEY="your_secret_key_here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 4️⃣ Run the Application

uvicorn main:app --reload

By default, the app will run at:
🔗 Swagger UI: http://127.0.0.1:8000/docs
🔗 Redoc UI: http://127.0.0.1:8000/redoc

🛠️ API Endpoints
Authentication
Method Endpoint Description
POST /auth/signup Register a new user
POST /auth/login Authenticate user & get token
Posts
Method Endpoint Description
POST /posts/ Create a new post (requires authentication)
GET /posts/ Retrieve all posts (requires authentication)
DELETE /posts/{post_id} Delete a post (requires authentication)
