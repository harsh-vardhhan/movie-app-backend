from sqlalchemy.orm import Session
from faker import Faker
import random
from .database import SessionLocal, engine, Base
from .models import Movie, Actor, Director, Genre

fake = Faker()

def seed_data():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    # genres = ["Action", "Sci-Fi", "Drama", "Crime", "Comedy", "Adventure", "Romance", "Thriller", "Horror", "Fantasy"]
    # Existing check can be removed to allow adding more data, or kept. 
    # Let's check for a threshold.
    if db.query(Movie).count() > 50:
        print("Database already has significant data. Skipping large seed.")
        db.close()
        return

    print("Seeding large dataset...")

    # Create Genres
    genre_names = ["Action", "Sci-Fi", "Drama", "Crime", "Comedy", "Adventure", "Romance", "Thriller", "Horror", "Fantasy", "Mystery", "Animation", "Documentary"]
    genres = []
    for name in genre_names:
        g = db.query(Genre).filter_by(name=name).first()
        if not g:
            g = Genre(name=name)
            db.add(g)
        genres.append(g)
    db.commit()

    # Create Directors (20)
    directors = []
    for _ in range(20):
        d = Director(name=fake.name())
        db.add(d)
        directors.append(d)
    db.commit()

    # Create Actors (50)
    actors = []
    for _ in range(50):
        a = Actor(name=fake.name())
        db.add(a)
        actors.append(a)
    db.commit()

    # Create Movies (100)
    for _ in range(100):
        title = fake.sentence(nb_words=3).replace(".", "")
        year = random.randint(1990, 2025)
        director = random.choice(directors)
        
        movie = Movie(title=title, release_year=year, director=director)
        
        # Random genres (1-3)
        movie_genres = random.sample(genres, k=random.randint(1, 3))
        movie.genres = movie_genres
        
        # Random actors (2-5)
        movie_actors = random.sample(actors, k=random.randint(2, 5))
        movie.actors = movie_actors
        
        db.add(movie)
    
    db.commit()
    db.close()
    print("Database seeded with 100 movies, 50 actors, 20 directors, and ~13 genres.")

if __name__ == "__main__":
    seed_data()
