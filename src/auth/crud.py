from sqlalchemy.orm import Session

from . import schemas, lib, models


def get_user_by_id(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserRegister):
    hashed_password = lib.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, hashed_password=hashed_password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email)
    if db_user is None:
        return lib.construct_authentication_report(False, "User with given email does not exist", None)
    if not lib.verify_password(password, db_user.hashed_password):
        return lib.construct_authentication_report(False, "Incorrect password", None)
    return lib.construct_authentication_report(True, None, db_user)
