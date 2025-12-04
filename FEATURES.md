# Features Documentation

## Overview
BragBoard is a platform for employees to recognize and celebrate each other's achievements through shoutouts. It fosters a positive work culture by enabling peer-to-peer recognition.

## User Authentication & Management
### Features
- **Registration**: New users can sign up with their name, email, password, department, and role (Employee/Admin).
- **Login**: Secure login using email and password.
- **Forgot Password**: Users can request a password reset via email verification.
- **Reset Password**: Securely reset the password after email verification.
- **User Roles**:
    - **Employee**: Standard user who can send/receive shoutouts and manage their profile.
    - **Admin**: Privileged user with access to administrative logs and potentially user management.

### Security Features
- **Secure by Design**: All user passwords are encrypted before storage. We never see your actual password.
- **Session Security**: Your login session is protected by secure tokens that expire automatically to keep your account safe.
- **Data Privacy**: Your personal information is protected and only accessible to you and authorized administrators.

### Technical Implementation
- **Frontend**:
    - `LoginRegister.jsx` handles the UI for all auth flows, switching modes (`login`, `register`, `forgot`, `reset`) based on user interaction.
    - Uses `fetch` to communicate with the backend auth endpoints.
    - Stores the returned JWT `access_token` in `localStorage` for session persistence.
- **Backend**:
    - **Router**: `app/routers/auth.py`
    - **Libraries**: `python-jose` for JWT generation/decoding, `passlib` for bcrypt password hashing.
    - **Flow**:
        1. User submits credentials.
        2. Backend verifies hash against DB.
        3. If valid, generates a JWT token with an expiration time.
        4. Token is returned to client.

## Profile Management
### Features
- **View Profile**: Users can view their own profile details.
- **Edit Profile**: Users can update their personal information.

### Technical Implementation
- **Frontend**:
    - `Profile.jsx` fetches user data from `/users/me` using the stored JWT token.
    - `EditProfile.jsx` provides a form to update fields, sending a `PUT` request to `/users/me`.
- **Backend**:
    - **Router**: `app/routers/users.py`
    - **Dependency**: `get_current_user` dependency ensures only authenticated requests can access these endpoints.
    - **Model**: Updates the `User` SQLAlchemy model in the database.

## Shoutouts (Core Feature)
### Features
- **Send Shoutouts**: Users can send shoutouts to colleagues to recognize their work.
- **Feed**: A central feed displaying shoutouts from across the organization.
- **Recipients**: Shoutouts can be directed to specific users.

### Technical Implementation
- **Data Model**:
    - `ShoutOut` table stores the message, sender, and timestamp.
    - `ShoutOutRecipient` association table links shoutouts to multiple `User` recipients (Many-to-Many relationship).
- **API**:
    - `POST /shoutouts`: Creates a new record.
    - `GET /shoutouts`: Fetches records with joined sender and recipient data for the feed.

## Social Interactions
### Features
- **Comments**: Users can comment on shoutouts to add their congratulations or thoughts.
- **Reactions**: Users can react to shoutouts with different emojis (Like, Clap, Star).

### Technical Implementation
- **Data Model**:
    - `Comment` table linked to `ShoutOut` and `User`.
    - `Reaction` table with an `Enum` for reaction types (`like`, `clap`, `star`).
- **Real-time Updates** (Planned): Currently implemented via polling or page refresh, but designed to support WebSocket integration in the future.

## Moderation & Compliance
### Features
- **Reporting**: Users can report inappropriate shoutouts for review.
- **Admin Logs**: The system tracks administrative actions for auditing purposes.

### Technical Implementation
- **Data Model**:
    - `Report` table links a `ShoutOut` to a `User` (reporter) and includes a reason.
    - `AdminLog` table records actions taken by admins.
- **Access Control**: Admin-only endpoints are protected by checking `current_user.role == UserRole.ADMIN`.
