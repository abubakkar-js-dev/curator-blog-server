# Curator Blogs System - Backend

A scalable, high-performance blog backend API.

## 🚀 Tech Stack

-   **Web Framework**: [FastAPI](https://fastapi.tiangolo.com/) for high-concurrency API routing.
-   **Database**: PostgreSQL fully optimized for asynchronous execution using `asyncpg`.
-   **ORM**: SQLAlchemy 2.0+ 
-   **DB Migrations**: Alembic (Configured for async engines)
-   **Validation & Config**: Pydantic / Pydantic Settings

## 🛠️ Local Setup

### 1. Environment Variables
Create a `.env` file at the root of the project with the following required configuration:
```env
DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>/<dbname>?ssl=require
SECRET_KEY=your-super-secret-key-here
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DEBUG=True
APP_ENV=development
```

### 2. Installations
Activate your Python virtual environment and install the dependencies.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
# Alternatively, if syncing from pyproject.toml: pip install -e .
```

### 3. Database Migrations
Since this project uses a strict schema driven by Alembic, initialize your database tables by upgrading to the most recent migration state:
```bash
alembic upgrade head
```

### 4. Running the App
Spin up the local Uvicorn ASGI server with live reload:
```bash
uvicorn app.main:app --reload
```
You can then visit `http://127.0.0.1:8000/docs` to view the auto-generated Swagger UI!

## 📂 Architecture Overview

This backend is designed with a production-ready **Layered Architecture**.
*   **`app/api/`**: The Controller Layer containing your FastAPI routers and dependencies (e.g., `get_db`).
*   **`app/schemas/`**: The Validation Layer storing all Pydantic DTOs for strict type-checking on HTTP requests/responses.
*   **`app/services/`**: The Business Logic Layer handling the core application features independent of HTTP or DB routing. 
*   **`app/repositories/`**: The Data Access Layer centralizing all SQLAlchemy database queries safely.
*   **`app/models/`**: The Data Layer housing your SQLAlchemy table classes.
*   **`app/core/`**: Security (`jwt`, `hashing`), Custom exceptions, and Global Configurations.
*   **`app/db/`**: Connection logic, asynchronous engines, and `Base` metadata.
