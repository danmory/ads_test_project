from fastapi import FastAPI
from auth.router import router as auth_router
from ads.router import router as ads_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(ads_router, prefix="/ads")
