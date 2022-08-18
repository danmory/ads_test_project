from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserRegister(UserBase):
    name: str
    password: str


class UserInfo(UserBase):
    name: str


class UserLogin(UserBase):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
