from classes.Review import Review


class Viewer:

    def __init__(self, username):
        self.username = username
    
    def get_username(self):
        return self._username
    def set_username(self, username):
        if isinstance(username, str) and (6 <= len(username) <= 16):
            self._username = username
    username = property(get_username, set_username)

    def reviews(self):
        pass

    def reviewed_movies(self):
        pass

    def movie_reviewed(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass
