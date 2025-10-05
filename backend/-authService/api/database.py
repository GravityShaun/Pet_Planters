import sqlite3
import aiosqlite
import logging
from typing import Optional, Dict, Any
from datetime import datetime
import os
import uuid

DATABASE_PATH = os.getenv("DATABASE_PATH", "auth.db")

def generate_uuid():
    """Generate a new UUID string"""
    return str(uuid.uuid4())

class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create users table with UUID primary key
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id TEXT PRIMARY KEY,
                        email TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL,
                        first_name TEXT,
                        last_name TEXT,
                        phone_number TEXT,
                        avatar_url TEXT,
                        is_active BOOLEAN DEFAULT TRUE,
                        is_verified BOOLEAN DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create refresh_tokens table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS refresh_tokens (
                        token_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT NOT NULL,
                        token_hash TEXT NOT NULL,
                        expires_at TIMESTAMP NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                    )
                ''')
                
                # Create password_reset_tokens table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS password_reset_tokens (
                        token_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT NOT NULL,
                        token_hash TEXT NOT NULL,
                        expires_at TIMESTAMP NOT NULL,
                        used BOOLEAN DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                    )
                ''')
                
                conn.commit()
                logging.info("Database initialized successfully")
                
        except Exception as e:
            logging.error(f"Database initialization error: {str(e)}")
            raise
    
    async def create_user(self, email: str, password_hash: str, first_name: str = None, last_name: str = None) -> Optional[str]:
        """Create a new user and return user_id (UUID)"""
        try:
            user_id = generate_uuid()
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute(
                    """INSERT INTO users (user_id, email, password_hash, first_name, last_name) 
                       VALUES (?, ?, ?, ?, ?)""",
                    (user_id, email, password_hash, first_name, last_name)
                )
                await db.commit()
                return user_id
        except aiosqlite.IntegrityError:
            return None  # Email already exists
        except Exception as e:
            logging.error(f"Create user error: {str(e)}")
            raise
    
    async def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                cursor = await db.execute(
                    "SELECT * FROM users WHERE email = ? AND is_active = TRUE",
                    (email,)
                )
                row = await cursor.fetchone()
                return dict(row) if row else None
        except Exception as e:
            logging.error(f"Get user by email error: {str(e)}")
            raise
    
    async def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user by ID"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                cursor = await db.execute(
                    "SELECT * FROM users WHERE user_id = ? AND is_active = TRUE",
                    (user_id,)
                )
                row = await cursor.fetchone()
                return dict(row) if row else None
        except Exception as e:
            logging.error(f"Get user by ID error: {str(e)}")
            raise
    
    async def update_user_verification(self, user_id: str, is_verified: bool = True) -> bool:
        """Update user verification status"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "UPDATE users SET is_verified = ?, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?",
                    (is_verified, user_id)
                )
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Update user verification error: {str(e)}")
            return False
    
    async def store_refresh_token(self, user_id: str, token_hash: str, expires_at: datetime) -> bool:
        """Store refresh token"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "INSERT INTO refresh_tokens (user_id, token_hash, expires_at) VALUES (?, ?, ?)",
                    (user_id, token_hash, expires_at)
                )
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Store refresh token error: {str(e)}")
            return False
    
    async def verify_refresh_token(self, token_hash: str) -> Optional[str]:
        """Verify refresh token and return user_id if valid"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute(
                    """SELECT user_id FROM refresh_tokens 
                       WHERE token_hash = ? AND expires_at > CURRENT_TIMESTAMP""",
                    (token_hash,)
                )
                row = await cursor.fetchone()
                return row[0] if row else None
        except Exception as e:
            logging.error(f"Verify refresh token error: {str(e)}")
            return None
    
    async def delete_refresh_token(self, token_hash: str) -> bool:
        """Delete refresh token (logout)"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "DELETE FROM refresh_tokens WHERE token_hash = ?",
                    (token_hash,)
                )
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Delete refresh token error: {str(e)}")
            return False
    
    async def update_user_password(self, user_id: str, new_password_hash: str) -> bool:
        """Update user password"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "UPDATE users SET password_hash = ?, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?",
                    (new_password_hash, user_id)
                )
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Update user password error: {str(e)}")
            return False
    
    async def update_user_profile(self, user_id: str, update_fields: dict) -> bool:
        """Update user profile fields"""
        try:
            if not update_fields:
                return True
            
            # Build dynamic SET clause
            set_clause = ", ".join([f"{field} = ?" for field in update_fields.keys()])
            values = list(update_fields.values())
            values.append(user_id)  # Add user_id for WHERE clause
            
            query = f"UPDATE users SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?"
            
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(query, values)
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Update user profile error: {str(e)}")
            return False
    
    async def deactivate_user(self, user_id: str) -> bool:
        """Deactivate user account (soft delete)"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "UPDATE users SET is_active = FALSE, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?",
                    (user_id,)
                )
                # Also delete all refresh tokens for this user
                await db.execute(
                    "DELETE FROM refresh_tokens WHERE user_id = ?",
                    (user_id,)
                )
                await db.commit()
                return True
        except Exception as e:
            logging.error(f"Deactivate user error: {str(e)}")
            return False

    async def get_all_users(self, exclude_user_id: str = None) -> list[Dict[str, Any]]:
        """Get all active users, optionally excluding a specific user"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                if exclude_user_id:
                    cursor = await db.execute(
                        """SELECT user_id, email, first_name, last_name, phone_number, avatar_url, created_at 
                           FROM users WHERE is_active = TRUE AND user_id != ?
                           ORDER BY first_name, last_name""",
                        (exclude_user_id,)
                    )
                else:
                    cursor = await db.execute(
                        """SELECT user_id, email, first_name, last_name, phone_number, avatar_url, created_at 
                           FROM users WHERE is_active = TRUE
                           ORDER BY first_name, last_name"""
                    )
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            logging.error(f"Get all users error: {str(e)}")
            return []

# Global database instance
db_manager = DatabaseManager() 