from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

from app.common.config import settings
from .models import User
from .schemas import UserBase

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: UserBase):
    to_encode = data.dict()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt, expire


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, [ALGORITHM])


def construct_authentication_report(result: bool, detail: str | None, user: User | None):
    return {
        "result": result,
        "detail": detail,
        "user": user,
    }


def construct_token_response(access_token: str, expire: datetime):
    return {"access_token": access_token, "token_type": "Bearer", "expire": expire}
