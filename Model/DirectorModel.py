class DirectorModel:
    def __init__(self):
        self.director_id = None
        self.directorName = None
        self.otherFamousMovie = None

    def get_director_id(self):
        return self.director_id

    def get_directorName(self):
        return self.directorName

    def get_otherFamousMovie(self):
        return self.otherFamousMovie

    def set_director_id(self, director_id):
        self.director_id = director_id

    def set_directorName(self, directorName):
        self.directorName = directorName

    def set_otherFamousMovie(self, otherFamousMovie):
        self.otherFamousMovie = otherFamousMovie

    def _str_(self):
        return f"Director Details: {self.director_id}, {self.directorName}, {self.otherFamousMovie}"
