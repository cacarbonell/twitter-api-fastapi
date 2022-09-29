#python
from uuid import UUID
#pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)