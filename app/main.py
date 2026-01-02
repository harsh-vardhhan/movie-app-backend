from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from mangum import Mangum

from .database import engine, Base, get_db
from . import models, schemas

# Create tables if not exist (better to use migrations in prod, but fine here)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie App Backend")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie App API"}

@app.get("/movies/", response_model=List[schemas.MovieList])
def read_movies(
    genre: Optional[str] = None,
    actor_id: Optional[int] = None,
    director_id: Optional[int] = None,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(models.Movie)

    if genre:
        query = query.join(models.Movie.genres).filter(models.Genre.name == genre)
    if actor_id:
        query = query.join(models.Movie.actors).filter(models.Actor.id == actor_id)
    if director_id:
        query = query.filter(models.Movie.director_id == director_id)
    if search:
        query = query.filter(models.Movie.title.contains(search))

    movies = query.offset(skip).limit(limit).all()
    return movies

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.get("/actors/{actor_id}", response_model=schemas.ActorDetail)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = db.query(models.Actor).filter(models.Actor.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@app.get("/directors/{director_id}", response_model=schemas.DirectorDetail)
def read_director(director_id: int, db: Session = Depends(get_db)):
    director = db.query(models.Director).filter(models.Director.id == director_id).first()
    if director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@app.get("/genres/", response_model=List[schemas.Genre])
def read_genres(db: Session = Depends(get_db)):
    return db.query(models.Genre).all()

handler = Mangum(app)
