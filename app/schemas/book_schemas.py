from typing import Optional
from pydantic import BaseModel


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "title": "Book 1",
                "description": "Book description"
            }
        }
