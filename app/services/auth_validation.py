from sqlalchemy.orm import Session

from app.models.user_model import UserModel
from app.schemas.user_schemas import UserSchema


def authenticate(db: Session, user: UserSchema):
    _user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if user == None:
        return False

    if _user.password == user.password:
        return _user
