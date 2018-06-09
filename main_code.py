import media
import fresh_tomatoes

"""
    Instances consist of 4 arguments each that are passed into the module media.py and uses its
    class Movie
"""


#6 instances that calls __init__ method in the module media.py
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
                        "https://youtube.com/tv#/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","Blue people",
                     "http://www.madtomatoe.com/wp-content/uploads/2009/08/avatar_poster.jpg",
                     "https://youtube.com/tv#/watch?v=5PSNL1qE6VY")

transformers = media.Movie("The Transformers: The Movie(1986)",
                           "Autobots battle the Decepticons and Unicron",
                           "https://i.jeded.com/i/the-transformers-the-movie.31030.jpg",
                           "https://youtube.com/tv#/watch?v=VyGLiwGUjeM")

avengers = media.Movie("The Avengers",
                       "The Avengers battle Loki.",
                       "http://1.bp.blogspot.com/-p9FPICvPfqo/VdbMbDqbhDI/AAAAAAAAzrU/2BnrpuqkilQ/s1600/AvengersPoster4.jpg",
                       "https://youtube.com/tv#/watch?v=eOrNdBpGMv8")

wonder_woman = media.Movie("Wonder Woman",
                           "The Amazon searches the world for The God of War",
                           "https://hmssweblog.files.wordpress.com/2017/05/wonder-woman-poster.jpg",
                           "https://youtube.com/tv#/watch?v=VSB4wGIdDwo")

black_panther = media.Movie("The Black Panther",
                            "Wakanda stryggles to use their resources to help the world.",
                            "https://www.monkeysfightingrobots.com/wp-content/uploads/2017/10/Black-Panther-Poster.jpg",
                            "https://youtube.com/tv#/watch?v=xjDjIWPwcPU")

#Array placed in a variable
movies = [toy_story, avatar, transformers, avengers, wonder_woman, black_panther]

#Calls the method inside the module fresh_tomatoes and places an argument into it
fresh_tomatoes.open_movies_page(movies)



