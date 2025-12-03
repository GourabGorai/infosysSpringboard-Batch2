# Backend Documentation

## Architecture
The backend is built using **FastAPI**, a modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints.

### Tech Stack
- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI server)
- **Database ORM**: SQLAlchemy
- **Database Driver**: `psycopg2-binary` (PostgreSQL) / `sqlite` (Development)
- **Authentication**:
    - `python-jose`: For JWT (JSON Web Token) encoding and decoding.
    - `passlib[bcrypt]`: For secure password hashing.
- **Validation**: Pydantic (Data validation and settings management using python type annotations).
- **Email Validation**: `email-validator`

## Application Structure
The backend is structured as a modular application:
- **`main.py`**: The entry point. Initializes the `FastAPI` app, configures CORS, creates database tables, and includes routers.
- **`database.py`**: Handles database connection (`create_engine`) and session management (`SessionLocal`).
- **`models.py`**: Defines the database schema using SQLAlchemy ORM classes.
- **`schemas.py`**: Defines Pydantic models for request/response validation.
- **`deps.py`**: Contains dependencies like `get_db` and `get_current_user`.
- **`routers/`**: Contains the API route definitions, split by domain (e.g., `auth.py`, `users.py`).

## Deep Dive: Key Components

### 1. Database Session Management
We use a dependency injection pattern for database sessions.
- **`get_db`**: A generator function that creates a new database session for each request and closes it after the request is completed.
- **Usage**: `def create_user(user: UserCreate, db: Session = Depends(get_db)): ...`

### 2. Authentication Flow
Authentication is stateless and JWT-based.
- **Login**:
    1. User sends `email` and `password`.
    2. Backend verifies password hash using `passlib`.
    3. If valid, creates a JWT containing the `sub` (subject/email) and expiration time.
    4. Returns `{ "access_token": "...", "token_type": "bearer" }`.
- **Protected Routes**:
    1. Client sends token in `Authorization: Bearer <token>` header.
    2. `get_current_user` dependency decodes the token.
    3. If valid, fetches the user from DB and attaches it to the request.
    4. If invalid/expired, raises `401 Unauthorized`.

### 3. Data Validation (Pydantic)
Pydantic models ensure that data entering and leaving the API is valid.
- **Request Models**: Validate incoming JSON bodies (e.g., `UserCreate` ensures email format and password length).
- **Response Models**: Filter data returned to the client (e.g., `UserOut` excludes the `password` field).

## Database Schema
The database schema is defined in `models.py` using SQLAlchemy.

### Models
- **User**:
    - `id`: Integer, Primary Key
    - `email`: String, Unique, Indexed
    - `role`: Enum (Employee, Admin)
    - Relationships: `shoutouts_sent`, `comments`, `reactions`, `reports_filed`
- **ShoutOut**:
    - `id`: Integer, Primary Key
    - `sender_id`: ForeignKey to Users
    - `message`: Text
    - Relationships: `sender`, `recipients`, `comments`, `reactions`
- **Reaction**:
    - `type`: Enum (Like, Clap, Star)
    - Links `User` and `ShoutOut`.

## API Endpoints
The API is organized into routers located in `app/routers`.

### Authentication (`/auth`)
- `POST /auth/login`: Authenticate user and return JWT token.
- `POST /auth/register`: Register a new user.
- `POST /auth/forgot-password`: Initiate password reset flow.
- `POST /auth/reset-password`: Complete password reset.

### Users (`/users`)
- `GET /users/me`: Get current authenticated user details.
- `PUT /users/me`: Update current user profile.

## Security Best Practices
- **Password Hashing**: Passwords are never stored in plain text. We use bcrypt.
- **CORS**: Configured to allow requests only from trusted origins (e.g., `http://localhost:5173`).
- **Dependency Injection**: Ensures clean testing and resource management.
