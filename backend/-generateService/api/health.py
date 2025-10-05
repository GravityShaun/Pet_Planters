from fastapi import APIRouter, HTTPException, Depends
from .database import ChatDatabaseManager
from .auth import auth_dependency, User
import sqlite3
import os

router = APIRouter()

@router.get("")
async def health_check(current_user: User = Depends(auth_dependency)):
    # Check SQLite database connection
    try:
        chat_db = ChatDatabaseManager()
        
        # Simple query to test database connection
        with sqlite3.connect(chat_db.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        return {
            'status': 'healthy',
            'database': 'up',
            'database_path': chat_db.db_path
        }
    except Exception as e:
        print(f"Database health check failed: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail={
                'status': 'unhealthy',
                'database': 'down',
                'error': str(e)
            }
        ) 