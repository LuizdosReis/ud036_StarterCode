import webbrowser


class Movie:
    """ This class create the objects of movies """

    VALID_RATINGS = ['G',
                     'PG',
                     'PG-13',
                     'R',
                     ]

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_post_image,
                 movie_trailer_youtube_url,
                 ):
        """ This constructor initializes all attributes of class """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_post_image
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self,
                     ):
        """ This method open browser in the trailer of movie"""
        webbrowser.open(self.trailer_youtube_url)
