from connection_to_db import DBConnection

class DirectorMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def create_directorDetails(self):
        query = f'CREATE TABLE IF NOT EXISTS Director(director_id INTEGER PRIMARY KEY AUTOINCREMENT, directorName varchar(20), otherFamousMovie varchar(20))'
        return self.conn.execute_query(query)

    def insert_directorDetails(self, directorDetails):
        query = f'INSERT INTO Director (directorName, otherFamousMovie) VALUES("{directorDetails.get_directorName()}", "{directorDetails.get_otherFamousMovie()}")'
        return self.conn.execute_query(query)
