from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "email": "<EMAIL>",
                "password": "<PASSWORD>"
            }
        }
