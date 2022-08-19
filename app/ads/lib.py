from fastapi import HTTPException

from . import models
from app.auth.models import User


def is_delete_permitted(ad_to_del: models.Ad, user: User):
    return user.id == ad_to_del.author_id


def raise_exc_if_none(obj: object, status_code, message: str):
    if obj is None:
        raise HTTPException(status_code=status_code, detail=message)
