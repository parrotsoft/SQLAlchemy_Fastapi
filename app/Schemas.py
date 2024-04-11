from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

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

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]