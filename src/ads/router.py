from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from common.dependencies import get_db, has_access
from . import schemas, crud, lib
from auth.crud import get_user_by_email


router = APIRouter()


@router.get("/all", response_model=list[schemas.AdResponse])
def read_all_ads(db: Session = Depends(get_db),
                 skip: int = Query(default=0),
                 limit: int = Query(default=100)
                 ):
    return crud.get_all_ads(db, skip, limit)


@router.get("/{ad_id}", response_model=schemas.AdResponse)
def read_ad_by_id(ad_id: int, db: Session = Depends(get_db)):
    return crud.get_ad_by_id(db, ad_id)


@router.post("/create", response_model=schemas.AdResponse)
def create_ad(ad: schemas.AdBase, access=Depends(has_access), db: Session = Depends(get_db)):
    user = get_user_by_email(db, access["email"])
    lib.raise_exc_if_none(user, 404, "Failed to load user")
    return crud.create_ad(db, ad, user.id)  # type: ignore


@router.delete("/delete")
def delete_ad(ad_id: int = Query(), access=Depends(has_access), db: Session = Depends(get_db)):
    user = get_user_by_email(db, access["email"])
    lib.raise_exc_if_none(user, 404, "Failed to load user")
    ad_to_del = crud.get_ad_by_id(db, ad_id)
    lib.raise_exc_if_none(ad_to_del, 404, "Failed to load ad")
    if not lib.is_delete_permitted(ad_to_del, user):  # type: ignore
        raise HTTPException(status_code=401, detail="No permission to delete")
    crud.delete_ad(db, ad_id)
