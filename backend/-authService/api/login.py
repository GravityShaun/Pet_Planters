from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timezone, timedelta
import logging

from .auth import auth_service, auth_dependency, User
from .database import db_manager

router = APIRouter()
security = HTTPBearer()

# Request Models
class UserSignupRequest(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str

# Response Models
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class UserResponse(BaseModel):
    user_id: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_verified: bool

class LoginResponse(BaseModel):
    user: UserResponse
    tokens: TokenResponse

@router.post("/signup", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserSignupRequest):
    """Register a new user"""
    try:
        # Check if user already exists
        existing_user = await db_manager.get_user_by_email(user_data.email)
        if existing_user:
            print("User already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Hash password
        password_hash = auth_service.get_password_hash(user_data.password)
        
        # Create user
        user_id = await db_manager.create_user(
            email=user_data.email,
            password_hash=password_hash,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user"
            )
        
        # Generate tokens
        access_token = auth_service.create_access_token(data={"sub": str(user_id)})
        refresh_token = auth_service.create_refresh_token(data={"sub": str(user_id)})
        
        # Store refresh token
        refresh_token_hash = auth_service.hash_token(refresh_token)
        expires_at = datetime.now(timezone.utc) + timedelta(days=auth_service.refresh_token_expire_days)
        await db_manager.store_refresh_token(user_id, refresh_token_hash, expires_at)
        
        # Get user data for response
        user = await db_manager.get_user_by_id(user_id)
        
        return LoginResponse(
            user=UserResponse(
                user_id=user['user_id'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                is_verified=user['is_verified']
            ),
            tokens=TokenResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=auth_service.access_token_expire_minutes * 60
            )
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Signup error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )

@router.post("/login", response_model=LoginResponse)
async def login(login_data: UserLoginRequest):
    """Authenticate user and return tokens"""
    try:
        # Get user by email
        user = await db_manager.get_user_by_email(login_data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Verify password
        if not auth_service.verify_password(login_data.password, user['password_hash']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Generate tokens
        access_token = auth_service.create_access_token(data={"sub": str(user['user_id'])})
        refresh_token = auth_service.create_refresh_token(data={"sub": str(user['user_id'])})
        
        # Store refresh token
        refresh_token_hash = auth_service.hash_token(refresh_token)
        expires_at = datetime.now(timezone.utc) + timedelta(days=auth_service.refresh_token_expire_days)
        await db_manager.store_refresh_token(user['user_id'], refresh_token_hash, expires_at)
        
        return LoginResponse(
            user=UserResponse(
                user_id=user['user_id'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                is_verified=user['is_verified']
            ),
            tokens=TokenResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=auth_service.access_token_expire_minutes * 60
            )
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Login error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed"
        )

@router.post("/refresh", response_model=TokenResponse)
async def refresh_access_token(token_data: RefreshTokenRequest):
    """Refresh access token using refresh token"""
    try:
        # Verify refresh token
        payload = auth_service.verify_token(token_data.refresh_token)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        user_id = int(payload.get("sub"))
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        # Verify refresh token in database
        refresh_token_hash = auth_service.hash_token(token_data.refresh_token)
        stored_user_id = await db_manager.verify_refresh_token(refresh_token_hash)
        
        if not stored_user_id or stored_user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        # Generate new access token
        new_access_token = auth_service.create_access_token(data={"sub": str(user_id)})
        
        return TokenResponse(
            access_token=new_access_token,
            refresh_token=token_data.refresh_token,  # Keep the same refresh token
            expires_in=auth_service.access_token_expire_minutes * 60
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Token refresh error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token refresh failed"
        )

@router.post("/logout")
async def logout(
    token_data: RefreshTokenRequest,
    current_user: User = Depends(auth_dependency)
):
    """Logout user by invalidating refresh token"""
    try:
        refresh_token_hash = auth_service.hash_token(token_data.refresh_token)
        await db_manager.delete_refresh_token(refresh_token_hash)
        
        return {"message": "Successfully logged out"}
        
    except Exception as e:
        logging.error(f"Logout error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Logout failed"
        )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(auth_dependency)):
    """Get current user information"""
    return UserResponse(
        user_id=current_user.user_id,
        email=current_user.email,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        is_verified=current_user.is_verified
    )

@router.post("/change-password")
async def change_password(
    password_data: PasswordChangeRequest,
    current_user: User = Depends(auth_dependency)
):
    """Change user password"""
    try:
        # Get current user data
        user = await db_manager.get_user_by_id(current_user.user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Verify current password
        if not auth_service.verify_password(password_data.current_password, user['password_hash']):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is incorrect"
            )
        
        # Hash new password and update
        new_password_hash = auth_service.get_password_hash(password_data.new_password)
        
        # Update password in database (you'll need to add this method to DatabaseManager)
        # For now, let's assume it's added
        success = await db_manager.update_user_password(current_user.user_id, new_password_hash)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update password"
            )
        
        return {"message": "Password changed successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Change password error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Password change failed"
        )