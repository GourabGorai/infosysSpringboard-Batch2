# Backend Documentation

## Architecture
The backend is built using **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

### Tech Stack
- **Framework**: FastAPI
- **Database ORM**: SQLAlchemy
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Authentication**: JWT (JSON Web Tokens) with `python-jose` and `passlib`
- **Validation**: Pydantic

## Database Schema
The database schema is defined in `models.py` using SQLAlchemy.

### Models
- **User**: Stores user information (name, email, password hash, department, role).
- **ShoutOut**: Represents a recognition message sent from one user to another.
- **ShoutOutRecipient**: Association table linking ShoutOuts to multiple recipients.
- **Comment**: Comments on shoutouts.
- **Reaction**: Emoji reactions (Like, Clap, Star) on shoutouts.
- **Report**: Reports filed against inappropriate shoutouts.
- **AdminLog**: Logs of administrative actions.

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
- (Additional user management endpoints implied)

### Shoutouts (Planned/Implied)
- `POST /shoutouts`: Create a new shoutout.
- `GET /shoutouts`: Retrieve feed of shoutouts.
- `POST /shoutouts/{id}/comments`: Add a comment.
- `POST /shoutouts/{id}/react`: Add a reaction.

## Security
- **Password Hashing**: Passwords are hashed using bcrypt before storage.
- **JWT**: Stateless authentication using JSON Web Tokens.
- **CORS**: Configured to allow requests from the frontend application.
