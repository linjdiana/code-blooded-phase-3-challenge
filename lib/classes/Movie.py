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
        pass

    def reviewers(self):
        pass

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
