import webbrowser


class Movie:

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, movie_post_image, movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_post_image
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)