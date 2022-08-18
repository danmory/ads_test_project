from pydantic import BaseModel, HttpUrl


class AdBase(BaseModel):
    title: str
    description: str
    image_url: HttpUrl


class AdResponse(AdBase):
    id: int

    class Config:
        orm_mode = True


class Ad(AdBase):
    id: int
    author_id: int
