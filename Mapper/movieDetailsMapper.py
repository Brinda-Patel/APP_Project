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

    def select_all(self):
        query = f'select m.title, m.movieIMDbRating, m.totalRatingCount, m.totalUserReviews, m.totalCriticReviews, d.directorName, m.datePublished, a.actorName, m.description, m.duration from movieDetail m inner join Director d on m.director_id=d.director_id inner join Actor a on m.leadActor_id=a.leadActor_id'
        result = self.conn.execute_query(query)
        column_name = ["title", "movieIMDbRating", "totalRatingCount", "totalUserReviews", "totalCriticReviews", "directorName", "datePublished", "actorName", "description", "duration"]
        final_result = []
        for i in result:
            fin_res = dict(zip(column_name, i))
            final_result.append(fin_res)
        return final_result

    def select_specific(self,data: dict):
        parameter = "Where "
        if list(data.keys())[0] == "movieIMDbRating":
            for key, value in data.items():
                p= f"{key} > '{value}' AND"
                parameter+=p
            query = f'select m.title,m.movieIMDbRating,m.totalRatingCount,m.totalUserReviews,m.totalCriticReviews,d.directorName, m.datePublished, a.actorName, m.description,m.duration from movieDetail m inner join Director d on m.director_id=d.director_id inner join Actor a on m.leadActor_id=a.leadActor_id {parameter[:-4]}'
            print(query)
            result=self.conn.execute_query(query)

            column_name = ["title", "movieIMDbRating", "totalRatingCount", "totalUserReviews", "totalCriticReviews", "directorName", "datePublished", "actorName", "description", "duration"]
            final_result = []
            for i in result:
                fin_res = dict(zip(column_name, i))
                final_result.append(fin_res)
            return final_result
        else:
            for key, value in data.items():
                p= f"{key} = '{value}' AND"
                parameter+=p
            query = f'select m.title,m.movieIMDbRating,m.totalRatingCount,m.totalUserReviews,m.totalCriticReviews,d.directorName, m.datePublished, a.actorName, m.description,m.duration from movieDetail m inner join Director d on m.director_id=d.director_id inner join Actor a on m.leadActor_id=a.leadActor_id {parameter[:-4]}'
            print(query)
            result=self.conn.execute_query(query)

            column_name = ["title", "movieIMDbRating", "totalRatingCount", "totalUserReviews", "totalCriticReviews", "directorName", "datePublished", "actorName", "description", "duration"]
            final_result = []
            for i in result:
                fin_res = dict(zip(column_name, i))
                final_result.append(fin_res)
            return final_result