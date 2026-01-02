from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Movie, Actor, Director, Genre

def seed_data():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    # Check if data exists
    if db.query(Movie).first():
        print("Data already exists.")
        db.close()
        return

    # Genres
    action = Genre(name="Action")
    scifi = Genre(name="Sci-Fi")
    drama = Genre(name="Drama")
    crime = Genre(name="Crime")
    
    db.add_all([action, scifi, drama, crime])
    db.commit()

    # Directors
    nolan = Director(name="Christopher Nolan")
    tarantino = Director(name="Quentin Tarantino")
    villeneuve = Director(name="Denis Villeneuve")

    db.add_all([nolan, tarantino, villeneuve])
    db.commit()

    # Actors
    leo = Actor(name="Leonardo DiCaprio")
    murphy = Actor(name="Cillian Murphy")
    bale = Actor(name="Christian Bale")
    chalamet = Actor(name="Timothée Chalamet")
    jackson = Actor(name="Samuel L. Jackson")
    travolta = Actor(name="John Travolta")

    db.add_all([leo, murphy, bale, chalamet, jackson, travolta])
    db.commit()

    # Movies
    inception = Movie(title="Inception", release_year=2010, director=nolan)
    inception.genres = [action, scifi]
    inception.actors = [leo, murphy]

    dark_knight = Movie(title="The Dark Knight", release_year=2008, director=nolan)
    dark_knight.genres = [action, crime, drama]
    dark_knight.actors = [bale, murphy]

    pulp_fiction = Movie(title="Pulp Fiction", release_year=1994, director=tarantino)
    pulp_fiction.genres = [crime, drama]
    pulp_fiction.actors = [jackson, travolta]

    dune = Movie(title="Dune", release_year=2021, director=villeneuve)
    dune.genres = [scifi, action]
    dune.actors = [chalamet]

    db.add_all([inception, dark_knight, pulp_fiction, dune])
    db.commit()
    db.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
