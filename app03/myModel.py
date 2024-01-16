from pydantic import BaseModel, EmailStr
# pip install 'pydantic[email]'
from typing import Union, List


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    fullname: Union[str | None] = None


class UserOut(BaseModel):
    username: str
    # password: str
    email: EmailStr
    fullname: Union[str | None] = None


class Items(BaseModel):
    name: str
    description: Union[str | None] = None
    price: float = 0.1
    tags: List[int] = []
