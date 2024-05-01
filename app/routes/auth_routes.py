from fastapi import APIRouter
from pydantic import BaseModel
from jose import jwt

SECRET_KEY = '5m)-3#w%p(@=h-esz()fnrmfzh$#yp2irsdef0322^+t70t+=9'
ALGORITHM = 'HS256'

router = APIRouter()


class LoginCredential(BaseModel):
    email: str | None = None
    password: str | None = None


@router.post("/login")
async def login(request: LoginCredential):
    token = jwt.encode(
        {
            'email': request.email,
            'password': request.password
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
