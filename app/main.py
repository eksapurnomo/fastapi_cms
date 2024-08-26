from fastapi import FastAPI
from app.routes import articles, users
from app.database import engine
from app import models

app = FastAPI()

# Buat tabel-tabel database
models.Base.metadata.create_all(bind=engine)

app.include_router(articles.router)
app.include_router(users.router)
