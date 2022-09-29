#models
from models.user_base import UserBase
#pydantic
from pydantic import BaseModel
from pydantic import Field


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
