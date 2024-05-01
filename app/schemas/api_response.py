from pydantic import BaseModel
from typing import Optional, TypeVar

from starlette.responses import JSONResponse

T = TypeVar("T")


class Response(BaseModel):
    code: str
    status: Optional[str]
    message: Optional[str]
    result: Optional[T]


def internal_server_error(message: str):
    error_detail = {"message": message}
    response = Response(code="500", status="Internal Server Error", message=message)
    return JSONResponse(status_code=500, content=response.dict())