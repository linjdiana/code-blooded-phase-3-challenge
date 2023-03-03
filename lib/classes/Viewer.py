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
        return [review for review in Review.all if review.viewer == self]
  
    def reviewed_movies(self):
        all_movies = []
        from classes.Movie import Movie
        for review in self.reviews():
            if isinstance(review.movie, Movie):
                all_movies.append(review.movie)
        return all_movies

    def movie_reviewed(self, movie):
        if movie in self.reviewed_movies():
            return True
        else:
            return False

    def rate_movie(self, movie, rating):
        Review(self, movie,rating)
