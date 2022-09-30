from models.user import User
#pydantic
from pydantic import Field

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
