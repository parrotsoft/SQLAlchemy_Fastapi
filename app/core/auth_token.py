from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from fastapi import Request, HTTPException

from app.core.config import get_db, SessionLocal
from app.models.user_model import UserModel

SECRET_KEY = '5m)-3#w%p(@=h-esz()fnrmfzh$#yp2irsdef0322^+t70t+=9'
ALGORITHM = 'HS256'


def create_token(email):
    token = jwt.encode({
        'email': email,
    }, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_token(token):
    isTokenValid: bool = False
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        session = SessionLocal()
        record = session.query(UserModel).filter(UserModel.email == payload['email']).first()

        if not record:
            isTokenValid = False
    except Exception as e:
        print(str(e))
        payload = None
    if payload:
        isTokenValid = True

    return isTokenValid


class MyHTTPBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(MyHTTPBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(MyHTTPBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not verify_token(token=credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
