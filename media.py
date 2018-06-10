import webbrowser


class Movie():
    """Is this module and its methods consider very short or obvious to have a
    docstring?"""
        
    #Create space in memory for these attributes for each instance created
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Open web browser and play movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
