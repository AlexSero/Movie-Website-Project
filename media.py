#defines the Movie class that contains the details of a movie
import webbrowser

class Movie():
    
    """This class provides a way to store movie related information
    Attributes:
        title, storyline, poster image, trailer, release date, and valid ratings"""
    
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube,valid_ratings,movie_release_date):
        #Initializes Movie class instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.valid_ratings = valid_ratings
        self.release_date = movie_release_date
        
    VALID_RATINGS = ("G", "PG", "PG-13", "R")
    
    def show_trailer(self):
        #Plays the movie trailer in the web browser
        webbrowser.open(self.trailer_youtube_url)
