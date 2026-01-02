from pydantic import BaseModel
from typing import List, Optional

class GenreBase(BaseModel):
    name: str

class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True

class ActorBase(BaseModel):
    name: str

class Actor(ActorBase):
    id: int

    class Config:
        from_attributes = True

class DirectorBase(BaseModel):
    name: str

class Director(DirectorBase):
    id: int

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    release_year: int

class MovieCreate(MovieBase):
    director_id: int
    genre_ids: List[int] = []
    actor_ids: List[int] = []

class Movie(MovieBase):
    id: int
    director: Optional[Director] = None
    genres: List[Genre] = []
    actors: List[Actor] = []

    class Config:
        from_attributes = True

class MovieList(MovieBase):
    id: int
    director: Optional[Director] = None
    genres: List[Genre] = []
    
    class Config:
        from_attributes = True

class ActorDetail(Actor):
    movies: List[MovieList] = []

class DirectorDetail(Director):
    movies: List[MovieList] = []
