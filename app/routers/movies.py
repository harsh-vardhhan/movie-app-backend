from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud, models
from ..database import get_db

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.MovieList])
def read_movies(
    genre: Optional[str] = None,
    actor_id: Optional[int] = None,
    director_id: Optional[int] = None,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_movies(
        db, 
        skip=skip, 
        limit=limit, 
        genre=genre, 
        actor_id=actor_id, 
        director_id=director_id, 
        search=search
    )

@router.get("/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
