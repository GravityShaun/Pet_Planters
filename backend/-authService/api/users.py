from fastapi import APIRouter, Depends, HTTPException, status, Header
from typing import List, Dict, Any, Optional
import logging
from .database import db_manager
from .auth import auth_dependency, User

router = APIRouter()

# Admin-only dependency
async def admin_only_dependency(x_admin_secret: Optional[str] = Header(None)):
    # In a real app, this should be a securely stored, complex secret
    ADMIN_SECRET = "SUPER_SECRET_ADMIN_KEY"
    if not x_admin_secret or x_admin_secret != ADMIN_SECRET:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Administrator access required")

@router.get("/admin/all_users", response_model=List[Dict[str, Any]], dependencies=[Depends(admin_only_dependency)])
async def get_all_users_for_admin():
    """
    Admin-only endpoint to get all users in the system, including inactive ones.
    """
    try:
        # A new DB method might be needed to get all users regardless of active status
        # For now, we'll reuse the existing one which gets active users.
        users = await db_manager.get_all_users()
        return [
            {
                "user_id": str(user['user_id']),
                "email": user['email'],
                "first_name": user.get('first_name'),
                "last_name": user.get('last_name'),
                "is_active": user.get('is_active', True), # Assuming default is active
                "is_verified": user.get('is_verified', False)
            } for user in users
        ]
    except Exception as e:
        logging.error(f"Admin get all users error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve all users for admin"
        )

@router.get("/users", response_model=List[Dict[str, Any]])
async def get_all_users(
    current_user: User = Depends(auth_dependency)
):
    """Get all users in the system (excluding current user)"""
    try:
        logging.info(f"=== USERS ENDPOINT START ===")
        logging.info(f"User: {current_user.user_id} ({current_user.email})")
        
        users = await db_manager.get_all_users(exclude_user_id=current_user.user_id)
        logging.info(f"Database returned {len(users)} users")
        
        # Format users for frontend consumption
        formatted_users = []
        for user in users:
            try:
                # Create display name from first_name and last_name
                display_name = ""
                if user.get('first_name') and user.get('last_name'):
                    display_name = f"{user['first_name']} {user['last_name']}"
                elif user.get('first_name'):
                    display_name = user['first_name']
                elif user.get('last_name'):
                    display_name = user['last_name']
                else:
                    display_name = user['email'].split('@')[0]  # Use email prefix as fallback
                
                formatted_user = {
                    "id": str(user['user_id']),
                    "user_id": user['user_id'],
                    "profile_id": str(user['user_id']),
                    "name": display_name,
                    "email": user['email'],
                    "first_name": user.get('first_name'),
                    "last_name": user.get('last_name'),
                    "phone_number": user.get('phone_number'),
                    "avatar_url": user.get('avatar_url'),
                    "initial": display_name[0].upper() if display_name else user['email'][0].upper(),
                    "created_at": user['created_at']
                }
                formatted_users.append(formatted_user)
                
            except Exception as e:
                logging.error(f"Error formatting user {user.get('user_id', 'unknown')}: {str(e)}")
                continue
        
        logging.info(f"Successfully formatted {len(formatted_users)} users")
        logging.info(f"=== USERS ENDPOINT SUCCESS ===")
        return formatted_users
        
    except HTTPException as e:
        logging.error(f"=== USERS ENDPOINT HTTP ERROR ===")
        logging.error(f"Status: {e.status_code}, Detail: {e.detail}")
        raise
    except Exception as e:
        logging.error(f"=== USERS ENDPOINT UNEXPECTED ERROR ===")
        logging.error(f"Error: {str(e)}")
        logging.error(f"Error type: {type(e)}")
        import traceback
        logging.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve users: {str(e)}"
        )

@router.get("/profile/{user_id}", response_model=Dict[str, Any])
async def get_user_profile(
    user_id: str,
    current_user: User = Depends(auth_dependency)
):
    """Get a user's profile by their user ID"""
    try:
        user = await db_manager.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        display_name = user.get('first_name', user['email'].split('@')[0])
        
        return {
            "id": str(user['user_id']),
            "user_id": user['user_id'],
            "name": display_name,
            "email": user['email'],
            "first_name": user.get('first_name'),
            "last_name": user.get('last_name'),
            "phone_number": user.get('phone_number'),
            "avatar_url": user.get('avatar_url'),
            "initial": display_name[0].upper(),
            "created_at": user['created_at'],
            "profile_id": user.get('profile_id') or str(user['user_id'])
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve user: {str(e)}"
        ) 