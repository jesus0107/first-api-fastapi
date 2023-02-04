from uuid import UUID
from datetime import date
from typing import Optional

# ------ Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    user_id: UUID = Field()
    email: EmailStr = Field()

class UserLogin(UserBase):
    password: str = Field(min_length=8)

class User(UserBase):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    birthday: Optional[date] = None 

class Tweet(BaseModel):
    pass