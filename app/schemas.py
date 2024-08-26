from pydantic import BaseModel

# Definisikan semua skema dalam file ini tanpa circular import
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class ArticleCreate(BaseModel):  # Definisikan ArticleCreate di sini, jika belum ada
    title: str
    content: str

class Article(BaseModel):
    title: str
    content: str
