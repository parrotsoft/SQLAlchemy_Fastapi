from sqlalchemy import Column, Integer, String
from app.core.config import Base


class BookModel(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
