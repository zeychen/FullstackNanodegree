import webbrowser

"""
#######################################
#   Udacity Fullstack Nanodegree      #
#   Project 1 Movie Trailer Website   #
#                                     #
#   Zeyuan (Zee) Chen                 #
#   November 8, 2016                  #
#                                     #
#   Movie Class                       #
#######################################
"""

class Movie():
    """ contains:
            title
            story line
            poster image
            youtube trailer
    """

    # initates movie class with input parameters
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
