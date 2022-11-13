from connection_to_db import DBConnection


class MovieDetailsMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def insert_moviedetails(self, movieDetails):
        query = f'INSERT INTO movieDetail(title,movieIMDbRating,totalRatingCount,totalUserReviews,totalCriticReviews,datePublished,director_id,leadActor_id,description,duration) VALUES ("{movieDetails.get_title()}", "{movieDetails.get_movieIMDbRating()}", "{movieDetails.get_totalRatingCount()}", "{movieDetails.get_totalUserReviews()}", "{movieDetails.get_totalCriticReviews()}", "{movieDetails.get_datePublished()}","{movieDetails.get_director_id()}", "{movieDetails.get_leadActor_id()}", "{movieDetails.get_description()}", "{movieDetails.get_duration()}") ON CONFLICT (title) DO NOTHING'
        self.conn.execute_query(query)

    def create_moviedetails(self):
        query = f'CREATE TABLE if NOT EXISTS movieDetail (movieDetail_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR (20) UNIQUE, movieIMDbRating  DECIMAL (2, 1), totalRatingCount INTEGER, totalUserReviews VARCHAR (20), totalCriticReviews VARCHAR (20), director_id INTEGER REFERENCES director (director_id), datePublished DATE, leadActor_id INTEGER REFERENCES leadActor (leadActor_id), description TEXT, duration INTEGER)'
        print("Table Created Successfully")
        return self.conn.execute_query(query)

    # def select(self, dictionary={}):
    #     query = f'SELECT * FROM movieDetail WHERE '
    #     for key in dictionary:
    #         query += f'{key} = "{dictionary[key]}" AND '
    #     query = query[:-5]
    #     return self.conn.execute_query(query)

    def select(self):
        query = f'select * from movieDetail where movieIMDbRating > 8.5'
        result = self.conn.execute_query(query)
        print(result)
        # for data in result:
        #     print(data)
