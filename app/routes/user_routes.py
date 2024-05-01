from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import get_db
from app.schemas.api_response import Response, internal_server_error
from app.schemas.user_schemas import UserSchema
from app.services import user_crud

router = APIRouter()


@router.get("/list")
async def list_users(db: Session = Depends(get_db)):
    return Response(
        code='Ok',
        status='200',
        message='List of users',
        result=user_crud.list_users(db)
    )


@router.post("/create")
async def create_user(request: UserSchema, db: Session = Depends(get_db)):
    try:
        user_crud.create_user(db, user=request)
        print(request)

        return Response(
            code='Ok',
            status='200',
            message='User created successfully',
            result=request.dict()
        )
    except Exception as e:
        return internal_server_error(str(e))