from sqlalchemy.orm import Session
from . import models

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def get_movies(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    genre: str = None,
    actor_id: int = None,
    director_id: int = None,
    search: str = None
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

    return query.offset(skip).limit(limit).all()

def get_actor(db: Session, actor_id: int):
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()

def get_director(db: Session, director_id: int):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

def get_genres(db: Session):
    return db.query(models.Genre).all()
