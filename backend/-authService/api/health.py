from fastapi import APIRouter, HTTPException, Depends
from .database import db_manager
from .auth import auth_dependency, User
import sqlite3
import os

router = APIRouter()

@router.get("")
async def health_check():
    """Public health check endpoint"""
    try:
        # Check database connection
        database_status = await check_database_health()
        
        return {
            'status': 'healthy',
            'database': database_status,
            'service': 'authentication-service'
        }
    except Exception as e:
        print(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail={
                'status': 'unhealthy',
                'database': 'down',
                'error': str(e)
            }
        )

@router.get("/detailed")
async def detailed_health_check(current_user: User = Depends(auth_dependency)):
    """Detailed health check endpoint (requires authentication)"""
    try:
        # Check database connection
        database_status = await check_database_health()
        
        # Check database file size
        db_size = get_database_size()
        
        # Count users (example health metric)
        user_count = await get_user_count()
        
        return {
            'status': 'healthy',
            'database': {
                'status': database_status,
                'size_bytes': db_size,
                'user_count': user_count
            },
            'service': 'authentication-service',
            'authenticated_user': current_user.email
        }
    except Exception as e:
        print(f"Detailed health check failed: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail={
                'status': 'unhealthy',
                'error': str(e)
            }
        )

async def check_database_health():
    """Check if database is accessible"""
    try:
        # Test database connection by fetching a user count
        user = await db_manager.get_user_by_id(1)  # This will work even if user doesn't exist
        return 'up'
    except Exception as e:
        print(f"Database health check failed: {str(e)}")
        return 'down'

def get_database_size():
    """Get database file size in bytes"""
    try:
        if os.path.exists(db_manager.db_path):
            return os.path.getsize(db_manager.db_path)
        return 0
    except Exception:
        return 0

async def get_user_count():
    """Get total number of active users"""
    try:
        import aiosqlite
        async with aiosqlite.connect(db_manager.db_path) as db:
            cursor = await db.execute("SELECT COUNT(*) FROM users WHERE is_active = TRUE")
            row = await cursor.fetchone()
            return row[0] if row else 0
    except Exception:
        return 0 