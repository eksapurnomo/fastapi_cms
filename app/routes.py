from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models
from .schemas import Article, ArticleCreate
from .dependencies import get_db

router = APIRouter()

@router.post("/articles/", response_model=Article)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db, title=article.title, content=article.content)

@router.get("/articles/", response_model=list[Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_articles(db, skip=skip, limit=limit)

@router.get("/articles/{article_id}", response_model=Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@router.delete("/articles/{article_id}", response_model=dict)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    if crud.delete_article(db, article_id):
        return {"detail": "Article deleted"}
    raise HTTPException(status_code=404, detail="Article not found")
