# Authentication Service

A FastAPI-based authentication service using SQLite database for user management.

## Features

- User registration and login
- JWT-based authentication with access and refresh tokens
- Password hashing with bcrypt
- SQLite database for user storage
- User profile management
- Account management (deactivation)
- Email verification placeholder endpoints

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Register a new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/refresh` - Refresh access token
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user info
- `POST /api/auth/change-password` - Change user password

### User Management
- `GET /api/user/profile` - Get detailed user profile
- `PUT /api/user/profile` - Update user profile
- `POST /api/user/verify-email` - Request email verification
- `POST /api/user/verify-email/{token}` - Verify email with token
- `DELETE /api/user/account` - Delete user account

### Health
- `GET /health` - Service health check

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy the environment file and configure:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Run the service:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

## Environment Variables

See `.env.example` for required environment variables.

**Important**: Change `JWT_SECRET_KEY` in production!

## Database

The service automatically creates an SQLite database with the following tables:
- `users` - User accounts
- `refresh_tokens` - JWT refresh tokens
- `password_reset_tokens` - Password reset tokens (for future use)

## Security Features

- Password hashing with bcrypt
- JWT tokens with expiration
- Refresh token rotation
- Input validation with Pydantic
- SQL injection protection with parameterized queries 