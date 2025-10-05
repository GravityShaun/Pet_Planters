import os
from dotenv import load_dotenv
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(env_path)

# Get environment variables for auth service
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
DATABASE_PATH = os.getenv("DATABASE_PATH", "auth.db")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Optional email configuration (for future email verification feature)
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT", "587")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")

print("Environment variables loaded:")
print(f"JWT_SECRET_KEY: {'Set' if JWT_SECRET_KEY != 'your-secret-key-change-in-production' else 'Using default (not recommended for production)'}")
print(f"DATABASE_PATH: {DATABASE_PATH}")
print(f"ENVIRONMENT: {ENVIRONMENT}")
print(f"SMTP_SERVER: {'Set' if SMTP_SERVER else 'Not Set'}")
print(f"FROM_EMAIL: {'Set' if FROM_EMAIL else 'Not Set'}")

# Validate critical environment variables in production
if ENVIRONMENT == "production":
    if JWT_SECRET_KEY == "your-secret-key-change-in-production":
        raise ValueError("JWT_SECRET_KEY must be set to a secure value in production")
    
    logger.info("Production environment detected - all critical variables validated")
else:
    logger.info(f"Running in {ENVIRONMENT} environment")

# Export commonly used variables
__all__ = [
    'JWT_SECRET_KEY',
    'DATABASE_PATH', 
    'ENVIRONMENT',
    'SMTP_SERVER',
    'SMTP_PORT',
    'SMTP_USERNAME',
    'SMTP_PASSWORD',
    'FROM_EMAIL'
]

