from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth_token import create_token
from app.core.config import get_db
from app.schemas.api_response import Response
from app.schemas.user_schemas import UserSchema
from app.services.auth_validation import authenticate

router = APIRouter()


@router.post("/login")
async def login(request: UserSchema, db: Session = Depends(get_db)):

    _authentication = authenticate(db=db, user=request)

    if _authentication is not None:
        token = create_token(_authentication.email)

        return Response(
            code='Ok',
            status='200',
            message='Login Successful',
            result={'access_token': token, 'token_type': 'bearer'}
        )

    return Response(
        code='Error',
        statu='401',
        message="Incorrect credentials"
    )
