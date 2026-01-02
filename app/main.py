from fastapi import FastAPI
from mangum import Mangum
from .database import engine
from . import models
from .routers import movies, actors, directors, genres

# Create tables if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie App Backend")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie App API"}

app.include_router(movies.router)
app.include_router(actors.router)
app.include_router(directors.router)
app.include_router(genres.router)

handler = Mangum(app)
