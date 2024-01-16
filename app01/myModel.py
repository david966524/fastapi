from pydantic import BaseModel ,Field
from typing import List
from datetime import date
class Item(BaseModel):
    name : str
    age : int
    sex : str

class User(BaseModel):
    name: str = "root" # default value
    age: int = Field(default=0,gt=0,lt=100) # 0-100范围
    birthday: date
    friend: List[str]
