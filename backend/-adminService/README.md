# backend/-adminService/README.md
# Admin Service

This service acts as a secure Backend-for-Frontend (BFF) for the Admin Dashboard. It provides a single, authenticated entry point for the dashboard to gather data from the various backend microservices.

## Features

- **CORS Configuration**: Properly configured to allow requests from the admin dashboard (http://localhost:5173)
- **Authentication**: Simple token-based authentication for admin access
- **Proxy Endpoints**: Aggregates data from multiple backend services
- **Health Monitoring**: Provides system metrics and health status

## Prerequisites

- Python 3.9+
- pip (Python package manager)

## Quick Start

1. **Use the startup script (recommended)**:
   ```bash
   ./start.sh
   ```

2. **Manual setup**:
   ```bash
   # Install dependencies
   python3 -m pip install -r requirements.txt
   
   # Start the server
   python3 -m uvicorn main:app --host 0.0.0.0 --port 8005 --reload
   ```

## Service Information

- **Port**: 8005
- **Admin Dashboard**: http://localhost:5173
- **API Base URL**: http://localhost:8005/api
- **Health Check**: GET /api/metrics

## Authentication

The service uses a simple token-based authentication system:
- Frontend token: `SECRET_ADMIN_TOKEN`
- API calls must include header: `X-Auth-Token: Bearer SECRET_ADMIN_TOKEN`

## API Endpoints

- `GET /api/metrics` - System metrics and health status
- `GET /api/users` - List all users (requires auth service)
- `POST /api/users/{user_id}/deactivate` - Deactivate user
- `GET /api/channels` - List channels (requires chat service)
- `GET /api/channels/{channel_id}/messages` - Get channel messages
- `DELETE /api/messages/{message_id}` - Delete message

## Configuration

Environment variables (optional):
- `AUTH_SERVICE_URL` - Default: http://localhost:8000/api/auth
- `CHAT_SERVICE_URL` - Default: http://localhost:8007/api/chat
- `ADMIN_SECRET_TOKEN` - Default: SUPER_SECRET_ADMIN_KEY

## Important Note

For this dashboard to function properly, ensure the following backend services are running:
- Auth Service on port 8000
- Chat Service on port 8007
- WebRTC Service on ports 8002/8005

## Troubleshooting

If you encounter CORS errors:
1. Ensure the admin service is running on port 8005
2. Check that the dashboard is running on port 5173
3. Verify the CORS configuration allows the dashboard origin
