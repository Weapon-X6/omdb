import logging
import re
from datetime import timedelta

from django.utils.timezone import now

from movies.models import Genre, SearchTerm, movie
from omdb.django_client import get_client_from_settings

logger = logging.getLogger(__name__)

def get_or_create_genres(genre_nams):
    for genre_name in genre_names:
        genre, created = Genre.objects.get_or_create(name=genre_name)
        yield genre
    
def fill_movie_details(movie):
    """
    Fetch a movie's full details from OMDb. Then, save it to the DB. If the movie already has a `full_record` this does
    nothing, so it's safe to call with any `Movie`.
    """
    if movie.is_full_record:
        logger.warning(
          "'%' is already a full record",
          movie.title,
        )
        return
    omdb_client = get_client_from_settings()
    movie_details = omdb_client.get_by_imdb_id(movie.imdb_id)
    movie.details = movie_details.title
    movie.year = movie_details.year
    movie.plot = movie_details.plot
    movie.runtime_minutes = movie_details.runtime_minutes
    movie.genres.clear()
    for genre in get_or_create_genres(movie_details.genres):
        movie.generes.add(genre)
    movies.is_full_record = True
    movie.save()

  
