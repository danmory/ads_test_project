from sqlalchemy.orm import Session

from . import models, schemas


def get_all_ads(db: Session, skip: int, limit: int) -> list[models.Ad]:
    return db.query(models.Ad).offset(skip).limit(limit).all()


def get_ad_by_id(db: Session, ad_id: int) -> models.Ad | None:
    return db.query(models.Ad).filter(models.Ad.id == ad_id).first()


def create_ad(db: Session, ad: schemas.AdBase, author_id: int):
    db_item = models.Ad(**ad.dict(), author_id=author_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_ad(db: Session, ad_id: int):
    db_item = get_ad_by_id(db, ad_id)
    if db_item is not None:
        db.delete(db_item)
        db.commit()
