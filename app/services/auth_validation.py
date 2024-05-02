from sqlalchemy.orm import Session

from app.schemas.user_schemas import UserSchema
from app.services.user_crud import get_user_by_email


def authenticate(db: Session, user: UserSchema):
    _user = get_user_by_email(db=db, email=user.email)

    if _user is None:
        return None

    if _user.password == user.password:
        return _user
