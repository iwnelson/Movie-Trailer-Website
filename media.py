import webbrowser

class Movie():

    """This class provides a way to store information about movies."""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_synopsis, poster_image, trailer_youtube):
        self.title = movie_title
        self.synopsis = movie_synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #this procedure initializes all of the required movie data fields

    def show_trailer(self):  #displays the movie trailer from youtube in the browser
        webbrowser.open(self.trailer_youtube_url)
        
