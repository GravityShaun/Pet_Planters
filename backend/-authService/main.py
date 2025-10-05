import sys
import asyncio
import select

# On macOS, the default asyncio event loop selector (kqueue) can be broken
# in certain Python versions/environments, causing an AttributeError for 'kevent'.
# This forces a fallback to the 'select' selector, which is more compatible.
if sys.platform == "darwin":
    if not hasattr(select, "kevent"):
        asyncio.set_event_loop_policy(asyncio.SelectorEventLoopPolicy(select.SelectSelector()))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api import login, signUp, health, users
from api.database_setup import create_database
from pathlib import Path

# Create the database and tables on startup
create_database()

app = FastAPI(title="Authentication Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if it doesn't exist
uploads_dir = Path("uploads")
uploads_dir.mkdir(exist_ok=True)

# Mount static files for serving uploaded avatars
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(login.router, prefix="/api/auth", tags=["authentication"])
app.include_router(signUp.router, prefix="/api/auth", tags=["user"])
app.include_router(users.router, prefix="/api/auth", tags=["users"])
app.include_router(health.router, prefix="/health", tags=["health"]) 