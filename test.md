<!-- API_DOCS_START -->
## API Documentation

| Method | Path | Status | Response |
|---|---|---|---|
| GET | / | 200 | `<pre>{'message': 'Welcome to the Movie App API'}</pre>` |
| GET | /actors/{actor_id} | 200 | `<pre>{'name': 'Leonardo DiCaprio', 'id': 1, 'movies': [{'title': 'Inception', 'release_year': 2010, 'id': 1, 'director': {'name': 'Christopher Nolan', 'id': 1}, 'genres': [{'name': 'Action', 'id': 1}, {'na... (truncated)</pre>` |
| GET | /directors/{director_id} | 200 | `<pre>{'name': 'Christopher Nolan', 'id': 1, 'movies': [{'title': 'Inception', 'release_year': 2010, 'id': 1, 'director': {'name': 'Christopher Nolan', 'id': 1}, 'genres': [{'name': 'Action', 'id': 1}, {'na... (truncated)</pre>` |
| GET | /genres/ | 200 | `<pre>[{'name': 'Action', 'id': 1}, {'name': 'Sci-Fi', 'id': 2}, {'name': 'Drama', 'id': 3}, {'name': 'Crime', 'id': 4}]</pre>` |
| GET | /movies/ | 200 | `<pre>[{'title': 'Inception', 'release_year': 2010, 'id': 1, 'director': {'name': 'Christopher Nolan', 'id': 1}, 'genres': [{'name': 'Action', 'id': 1}, {'name': 'Sci-Fi', 'id': 2}]}, {'title': 'The Dark Kn... (truncated)</pre>` |
| GET | /movies/{movie_id} | 200 | `<pre>{'title': 'Inception', 'release_year': 2010, 'id': 1, 'director': {'name': 'Christopher Nolan', 'id': 1}, 'genres': [{'name': 'Action', 'id': 1}, {'name': 'Sci-Fi', 'id': 2}], 'actors': [{'name': 'Leo... (truncated)</pre>` |

<!-- API_DOCS_END -->