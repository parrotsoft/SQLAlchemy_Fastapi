from sqlalchemy.orm import Session

from app.models.book_models import BookModel
from app.schemas.book_schemas import BookSchema


def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookModel).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    _book = BookModel(
        title=book.title,
        description=book.description
    )

    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()
    return _book


def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book
