#python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional
#models
from models.user import User
#pydantic
from pydantic import BaseModel
from pydantic import Field


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
