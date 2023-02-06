from uuid import UUID, uuid4
from datetime import date, datetime
from typing import Optional

# ------ Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    email: EmailStr = Field()

class UserLogin(UserBase):
    password: str = Field(min_length=8, max_length=64)

class User(UserBase):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    birth_date: Optional[date] = None 

class UserRegister(User, UserLogin):
    pass

class Tweet(BaseModel):
    tweet_id: UUID = Field()
    content: str = Field(min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field()