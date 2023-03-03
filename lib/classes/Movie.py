from classes.Review import Review

class Movie:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self._title
    def set_title(self, title):
        if isinstance(title, str) and (len(title) > 0) and not hasattr(self, "_title"):
            self._title = title
    title = property(get_title, set_title)
    
    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        all_reviewers = []
        for review in self.reviews():
            all_reviewers.append(review.viewer)
        return all_reviewers

    def average_rating(self):
        reviews = self.reviews()
        ratings = [review.rating for review in reviews]
        sum_ratings = sum(ratings)
        num_ratings = len(ratings)
        return sum_ratings / num_ratings
    
    @classmethod
    def highest_rated(cls):
        pass
