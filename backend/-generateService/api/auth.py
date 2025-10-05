from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
import os
from typing import Optional
from .getEnv import JWT_SECRET, JWT_ALGORITHM

# Development mode flag
DEV_MODE = os.getenv("DEV_MODE", "false").lower() == "true" or True  # Enable for development


class User:
    def __init__(self, user_id: str):
        self.user_id = user_id

class JWTAuth:
    def __init__(self):
        self.secret_key = JWT_SECRET
        self.algorithm = JWT_ALGORITHM
        self.security = HTTPBearer()

    async def __call__(
        self,
        credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())
    ) -> Optional[User]:
        try:
            token = credentials.credentials
            
            # Development mode: allow dummy tokens
            if DEV_MODE and (token == "dummy-token-for-testing" or token.startswith("test-")):
                return User(user_id="test-user-uuid")  # Default test user
            
            decoded_token = jwt.decode(
                token, 
                self.secret_key, 
                algorithms=[self.algorithm]
            )
            # Auth service uses "sub" field for user_id
            user_id_str = decoded_token.get('sub')
            
            if not user_id_str:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token: missing user ID"
                )
            
            # Use the user_id as a string (UUID from auth service)
            return User(user_id_str)
            
        except jwt.ExpiredSignatureError:
            # In development mode, allow expired tokens
            if DEV_MODE:
                return User(user_id="test-user-uuid")
            raise HTTPException(
                status_code=401,
                detail="Token has expired"
            )
        except jwt.InvalidTokenError:
            # In development mode, allow invalid tokens
            if DEV_MODE:
                return User(user_id="test-user-uuid")
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

auth_dependency = JWTAuth()