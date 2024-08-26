from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app import models, schemas

from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@router.get("/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/", response_model=List[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = db.query(models.Article).offset(skip).limit(limit).all()
    return articles
