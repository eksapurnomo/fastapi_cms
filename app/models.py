from sqlalchemy import Column, Integer, String
from app.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(String(1000))
