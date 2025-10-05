from fastapi import APIRouter, HTTPException, Depends, status, File, UploadFile
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
import logging
import os
import uuid
import shutil
from pathlib import Path

from .auth import auth_dependency, User
from .database import db_manager

router = APIRouter()

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads/avatars")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Request Models
class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    Avatar_url: Optional[str] = None
    email: Optional[str] = None

class EmailVerificationRequest(BaseModel):
    email: EmailStr

# Response Models
class ProfileResponse(BaseModel):
    user_id: str
    email: str
    name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    Avatar_url: Optional[str]
    is_verified: bool
    created_at: str

@router.get("/profile", response_model=ProfileResponse)
async def get_user_profile(current_user: User = Depends(auth_dependency)):
    """Get detailed user profile"""
    try:
        user_data = await db_manager.get_user_by_id(current_user.user_id)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return ProfileResponse(
            user_id=str(user_data['user_id']),
            email=user_data['email'],
            name=user_data.get('first_name'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            phone_number=user_data.get('phone_number'),
            Avatar_url=user_data.get('avatar_url'),
            is_verified=user_data['is_verified'],
            created_at=user_data['created_at']
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Get profile error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch profile"
        )

@router.put("/profile")
async def update_user_profile(
    profile_data: UpdateProfileRequest,
    current_user: User = Depends(auth_dependency)
):
    """Update user profile information"""
    try:
        # Prepare update data
        update_fields = {}
        if profile_data.name is not None:
            update_fields['first_name'] = profile_data.name
        if profile_data.phone_number is not None:
            update_fields['phone_number'] = profile_data.phone_number
        if profile_data.Avatar_url is not None:
            update_fields['avatar_url'] = profile_data.Avatar_url
        
        if not update_fields:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No fields to update"
            )
        
        # Update user profile
        success = await db_manager.update_user_profile(current_user.user_id, update_fields)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update profile"
            )
        
        # Get updated user data
        user = await db_manager.get_user_by_id(current_user.user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return {
            "message": "Profile updated successfully",
            "user": {
                "user_id": str(user['user_id']),
                "email": user['email'],
                "name": user.get('first_name'),
                "phone_number": user.get('phone_number'),
                "Avatar_url": user.get('avatar_url'),
                "is_verified": user['is_verified']
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Update profile error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Profile update failed"
        )

@router.post("/profile/{user_id}/avatar", status_code=status.HTTP_200_OK)
async def upload_avatar(
    user_id: str,
    file: UploadFile = File(...),
    current_user: User = Depends(auth_dependency)
):
    """Upload user avatar"""
    try:
        # Ensure user can only upload their own avatar
        if current_user.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
        
        # Validate file type
        if not file.content_type or not file.content_type.startswith('image/'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File must be an image"
            )
        
        # Generate unique filename
        file_extension = file.filename.split('.')[-1] if '.' in file.filename else 'jpg'
        unique_filename = f"{user_id}_{uuid.uuid4().hex}.{file_extension}"
        file_path = UPLOAD_DIR / unique_filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Update user's avatar URL in database
        avatar_url = f"/uploads/avatars/{unique_filename}"
        success = await db_manager.update_user_profile(user_id, {"avatar_url": avatar_url})
        
        if not success:
            # Clean up uploaded file if database update fails
            if file_path.exists():
                file_path.unlink()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update avatar"
            )
        
        return {
            "message": "Avatar uploaded successfully",
            "avatar_url": avatar_url
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Upload avatar error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload avatar"
        )

@router.delete("/account")
async def delete_user_account(current_user: User = Depends(auth_dependency)):
    """Delete user account (soft delete)"""
    try:
        success = await db_manager.deactivate_user(current_user.user_id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete account"
            )
        
        return {"message": "Account deleted successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Delete account error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Account deletion failed"
        )
