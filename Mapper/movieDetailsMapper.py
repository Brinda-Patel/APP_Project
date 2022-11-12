from connection_to_db import DBConnection


class MovieDetailsMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def insert_moviedetails(self, movieDetails):
        query = f'INSERT INTO (title,movieIMDbRating,totalRatingCount,totalUserReviews,totalCriticReviews,director_id,datePublished,leadActor_id,description) VALUES ("{movieDetails.get_title()}", "{movieDetails.get_movieIMDbRating()}", "{movieDetails.get_totalRatingCount()}", "{movieDetails.get_totalUserReviews()}", "{movieDetails.get_totalCriticReviews()}", "{movieDetails.get_director_id()}", "{movieDetails.get_datePublished()}", "{movieDetails.get_leadActor_id()}", "{movieDetails.get_description()}", "{movieDetails.get_duration()}")'
        return self.conn.execute_query(query)

    def create_moviedetails(self):
        query = f'CREATE TABLE if NOT EXISTS movieDetail (movieDetail_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR (20), movieIMDbRating  DECIMAL (2, 1), totalRatingCount INTEGER, totalUserReviews VARCHAR (20), totalCriticReviews VARCHAR (20), director_id INTEGER REFERENCES director (director_id), datePublished DATE, leadActor_id INTEGER REFERENCES leadActor (leadActor_id), description TEXT, duration INTEGER)'
        return self.conn.execute_query(query)
