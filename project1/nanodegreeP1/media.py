import webbrowser


# Generates movie object with required assets
class Movie():
    """Takes movie details as input - returns an object with those details"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
