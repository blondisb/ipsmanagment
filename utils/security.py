from jose import JWTError, jwt
from fastapi import HTTPException, status
from config import settings

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

def create_access_token(data: dict):
    from services.auth_service import AuthService
    return AuthService.create_access_token(data)