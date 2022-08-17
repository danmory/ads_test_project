from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from . import crud, lib
from common.dependencies import get_db, has_access
from .schemas import Token, UserBase, UserLogin, UserRegister

router = APIRouter()


@router.post("/register", response_model=Token)
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = crud.create_user(db, user)
    access_token = lib.create_access_token(UserBase.from_orm(db_user))
    return lib.construct_token_response(access_token)


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth_result = crud.authenticate_user(db, user.email, user.password)
    if not auth_result["result"]:
        raise HTTPException(status_code=401, detail=auth_result["detail"])
    access_token = lib.create_access_token(
        UserBase.from_orm(auth_result["user"]))
    return lib.construct_token_response(access_token)


@router.post("/check", dependencies=[Depends(has_access)])
def check():
    return "Authorized"
