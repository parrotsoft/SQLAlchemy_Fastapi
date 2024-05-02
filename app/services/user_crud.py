from sqlalchemy.orm import Session

from app.models.user_model import UserModel
from app.schemas.user_schemas import UserSchema


def list_users(db: Session):
    return db.query(UserModel).all()


def create_user(db: Session, user: UserSchema):
    _user = UserModel(
        email=user.email,
        password=user.password
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def delete_user(db: Session, user_id: int):
    _user = get_user(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()
    return _user


def update_user(db: Session, user_id: int, user: UserSchema):
    _user = get_user(db=db, user_id=user_id)
    _user.name = user.email
    _user.password = user.email
    db.commit()
    db.refresh(_user)
    return _user