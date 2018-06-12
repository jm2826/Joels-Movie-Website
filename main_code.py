import media
import fresh_tomatoes

""" Instances consist of 4 arguments each that are passed into the
    module media.py and uses its class Movie """


# 6 instances that calls __init__ method in the module media.py
star_wars = media.Movie(
    "Star Wars",
    "A story of a boy a girl and the universe",
    # NOQA - URL breaks PEP8 Standards but cant break line to fix
    "https://tse2.mm.bing.net/th?id=OIP.W3-_kiSuMQ35EpfQmpCQoAHaKX&pid=15.1&P=0&w=300&h=300",
    "https://youtube.com/tv#/watch?v=XHk5kCIiGoM")

the_sound_of_music = media.Movie(
    "The Sound of Music",
    # NOQA - URL breaks PEP8 Standards but cant break line to fix
    "A Nun, Maria, becomes a Governess and much more for the Von Trapps.",
    "https://tse1.mm.bing.net/th?id=OIP.OGX0qNsyvHh3O7j4JBvJYgHaLD&pid=15.1&P=0&w=300&h=300",
    "https://youtube.com/tv#/watch?v=UY6uw3WpPzY")

transformers = media.Movie(
    "The Transformers: The Movie(1986)",
    "Autobots battle the Decepticons and Unicron",
    "https://i.jeded.com/i/the-transformers-the-movie.31030.jpg",
    "https://youtube.com/tv#/watch?v=VyGLiwGUjeM")

avengers = media.Movie(
    "The Avengers",
    "The Avengers battle Loki.",
    # NOQA - URL breaks PEP8 Standards but cant break line to fix
    "http://1.bp.blogspot.com/-p9FPICvPfqo/VdbMbDqbhDI/AAAAAAAAzrU/2BnrpuqkilQ/s1600/AvengersPoster4.jpg",
    "https://youtube.com/tv#/watch?v=eOrNdBpGMv8")

wonder_woman = media.Movie(
    "Wonder Woman",
    "The Amazon searches the world for The God of War",
    "https://hmssweblog.files.wordpress.com/2017/05/wonder-woman-poster.jpg",
    "https://youtube.com/tv#/watch?v=VSB4wGIdDwo")

black_panther = media.Movie(
    "The Black Panther",
    "Wakanda stryggles to use their resources to help the world.",
    # NOQA - URL breaks PEP8 Standards but cant break line to fix
    "https://www.monkeysfightingrobots.com/wp-content/uploads/2017/10/Black-Panther-Poster.jpg",
    "https://youtube.com/tv#/watch?v=xjDjIWPwcPU")

# Array placed in a variable
movies = [
    star_wars,
    the_sound_of_music,
    transformers,
    avengers,
    wonder_woman,
    black_panther]

# Calls the method inside the module fresh_tomatoes and places an argument
# into it
fresh_tomatoes.open_movies_page(movies)
