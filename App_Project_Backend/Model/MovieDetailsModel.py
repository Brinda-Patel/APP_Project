class MovieDetailsModel:

    def __init__(self):
        self.movieDetail_id = None
        self.title = None
        self.movieIMDbRating = None
        self.totalRatingCount = None
        self.totalUserReviews = None
        self.totalCriticReviews = None
        self.director_id = None
        self.datePublished = None
        self.leadActor_id = None
        self.description = None
        self.duration = None

    def get_movieDetail_id(self):
        return self.movieDetail_id

    def get_title(self):
        return self.title

    def get_movieIMDbRating(self):
        return self.movieIMDbRating

    def get_totalRatingCount(self):
        return self.totalRatingCount

    def get_totalUserReviews(self):
        return self.totalUserReviews

    def get_totalCriticReviews(self):
        return self.totalCriticReviews

    def get_director_id(self):
        return self.director_id

    def get_datePublished(self):
        return self.datePublished

    def get_leadActor_id(self):
        return self.leadActor_id

    def get_description(self):
        return self.description

    def get_duration(self):
        return self.duration

    def set_movieDetail_id(self, movieDetail_id):
        self.movieDetail_id = movieDetail_id

    def set_title(self, title):
        self.title = title

    def set_movieIMDbRating(self, movieIMDbRating):
        self.movieIMDbRating = movieIMDbRating

    def set_totalRatingCount(self, totalRatingCount):
        self.totalRatingCount = totalRatingCount

    def set_totalUserReviews(self, totalUserReviews):
        self.totalUserReviews = totalUserReviews

    def set_totalCriticReviews(self, totalCriticReviews):
        self.totalCriticReviews = totalCriticReviews

    def set_director_id(self, director_id):
        self.director_id = director_id

    def set_datePublished(self, datePublished):
        self.datePublished = datePublished

    def set_leadActor_id(self, leadActor_id):
        self.leadActor_id = leadActor_id

    def set_description(self, description):
        self.description = description

    def set_duration(self, duration):
        self.duration = duration

    def __str__(self):
        return f"Movie Details: {self.movieDetail_id}, {self.title}, {self.movieIMDbRating}, {self.totalRatingCount}, {self.totalUserReviews}, {self.totalCriticReviews}, {self.director_id}, {self.datePublished}, {self.leadActor_id}, {self.description}, {self.duration}"
