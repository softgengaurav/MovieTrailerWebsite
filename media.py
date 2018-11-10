# Creating a class Movie, that serves as the blueprint


class Movie():
    # __init__ is the constructor and initializes the instance variables
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        '''self refers to pointing to the current instance'''
