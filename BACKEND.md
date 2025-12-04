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

## Security & Data Protection

### Account Creation & Management
- **Unique Constraints**: The database enforces unique email addresses to prevent duplicate accounts.
- **Input Validation**: Pydantic schemas (`schemas.py`) strictly validate all inputs during account creation:
    - **Email**: Must be a valid email format (validated via `email-validator`).
    - **Password**: Minimum length requirements are enforced.
    - **Role**: Restricted to valid Enum values (`employee`, `admin`).

### Password Storage
We strictly follow industry standards for password storage. **Passwords are NEVER stored in plain text.**
- **Algorithm**: `bcrypt`
- **Implementation**: We use `passlib.context.CryptContext` with `schemes=["bcrypt"]`.
- **Why Bcrypt?**:
    - **Salting**: Automatically handles salting to protect against rainbow table attacks.
    - **Work Factor**: It is a slow hashing algorithm, making brute-force attacks computationally expensive.
- **Verification**: When a user logs in, the provided password is hashed and compared against the stored hash using `verify_password()`.

### Token Management (JWT)
- **Stateless Authentication**: We use JSON Web Tokens (JWT) to manage sessions without server-side state.
- **Algorithm**: `HS256` (HMAC with SHA-256) for signing tokens.
- **Payload**:
    - `sub`: The subject (user's email).
    - `exp`: Expiration time (set to a short duration, e.g., 30 minutes) to minimize the window of opportunity if a token is compromised.
- **Security**: The secret key used to sign tokens is kept secure on the server. Any modification to the token payload invalidates the signature.

### Data Integrity
- **SQL Injection Protection**: By using SQLAlchemy ORM, all database queries are parameterized, automatically protecting against SQL injection attacks.
- **Over-posting Protection**: Pydantic response models (`UserOut`) explicitly define which fields are sent back to the client, ensuring sensitive data like password hashes or internal flags are never leaked.

## Database Schema
The database schema is defined in `models.py` using SQLAlchemy.

### Models
- **User**:
    - `id`: Integer, Primary Key
    - `email`: String, Unique, Indexed
    - `password`: String (Hashed)
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
