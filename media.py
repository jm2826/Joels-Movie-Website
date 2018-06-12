import webbrowser
"""This module was created to make my class Movie for every instance
   used in the file main_code.py. It also utilizes the module webbrowser
    to open the movie trailer URL's I found for each instance"""


class Movie():
    """This class allows me to call two methods, __init__ and show_trailer
        in the module main_code.py"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open Web Browser and play movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

