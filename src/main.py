from fastapi import FastAPI
from auth.router import router as auth_router
from ads.router import router as ads_router
from common.database import engine, Base, create_database_if_not_exists

create_database_if_not_exists(engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(ads_router, prefix="/ads")