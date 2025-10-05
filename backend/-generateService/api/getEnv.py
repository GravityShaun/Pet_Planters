import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from datetime import datetime, timezone

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
# Load environment variables
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(env_path)

# Database configuration
CHAT_DATABASE_PATH = os.getenv("CHAT_DATABASE_PATH", "chat.db")

# JWT settings - use same secret as auth service
JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
JWT_ALGORITHM = "HS256"

print("Environment variables loaded:")
print(f"CHAT_DATABASE_PATH: {CHAT_DATABASE_PATH}")
print(f"JWT_SECRET: {'Set' if JWT_SECRET else 'Not Set'}")

logging.info("Chat service configuration loaded successfully")

