# Live API Documentation

![Deploy to AWS Lambda](https://github.com/harsh-vardhhan/movie-app-backend/actions/workflows/deploy.yml/badge.svg)

**Base URL**: `https://hxzoqzlhck.execute-api.ap-south-1.amazonaws.com/`

## API Endpoints

| Method | Path | Response Type | Description |
|---|---|---|---|
| **GET** | `/movies/` | `List[MovieList]` | Retrieve a paginated list of movies. Includes director and genre info. |
| **GET** | `/movies/{id}` | `Movie` | Retrieve detailed information about a specific movie, including its cast (actors). |
| **GET** | `/actors/{id}` | `ActorDetail` | Retrieve detailed information about an actor, including their filmography. |
| **GET** | `/directors/{id}` | `DirectorDetail` | Retrieve detailed information about a director, including their filmography. |
| **GET** | `/genres/` | `List[Genre]` | Retrieve a list of all available movie genres. |

## Data Models

### Movie
Detailed representation of a movie.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the movie. |
| `title` | `string` | Title of the movie. |
| `release_year` | `integer` | Year of release. |
| `director` | [Director](#director) | The director of the movie. |
| `genres` | List[[Genre](#genre)] | List of genres associated with the movie. |
| `actors` | List[[Actor](#actor)] | List of actors who starred in the movie. |

### MovieList
Simplified representation of a movie for list views.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the movie. |
| `title` | `string` | Title of the movie. |
| `release_year` | `integer` | Year of release. |
| `director` | [Director](#director) | The director of the movie. |
| `genres` | List[[Genre](#genre)] | List of genres associated with the movie. |

### ActorDetail
Detailed representation of an actor.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the actor. |
| `name` | `string` | Full name of the actor. |
| `movies` | List[[MovieList](#movielist)] | List of movies this actor has appeared in. |

### DirectorDetail
Detailed representation of a director.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the director. |
| `name` | `string` | Full name of the director. |
| `movies` | List[[MovieList](#movielist)] | List of movies directed by this person. |

### Actor
Basic actor information.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the actor. |
| `name` | `string` | Full name of the actor. |

### Director
Basic director information.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the director. |
| `name` | `string` | Full name of the director. |

### Genre
Movie genre information.
| Field | Type | Description |
|---|---|---|
| `id` | `integer` | Unique identifier for the genre. |
| `name` | `string` | Name of the genre (e.g., "Action", "Drama"). |