from auth.lib import decode_access_token
from .database import SessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose.exceptions import JOSEError

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        decode_access_token(token)
    except JOSEError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e))
