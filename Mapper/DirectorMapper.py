from connection_to_db import DBConnection

class DirectorMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def create_directorDetails(self):
        query = f'CREATE TABLE IF NOT EXISTS Director(director_id INTEGER PRIMARY KEY AUTOINCREMENT, directorName varchar(20), otherFamousMovie varchar(20))'
        print("Table Created Successfully")
        return self.conn.execute_query(query)

    def getRowByDirectorName(self, directorName):
        inspect_existing_query = f'SELECT director_id FROM Director WHERE directorName = "{directorName}"'
        try:
            self.conn.cursor.execute(inspect_existing_query)
            res = self.conn.cursor.fetchone()
        except Exception as e:
            print(e)
        return res

    def insert_directorDetails(self, directorDetails):
        existing_id = -1
        get_existing_id = self.getRowByDirectorName(
            directorDetails.get_directorName())
        if get_existing_id is not None:
            existing_id = get_existing_id[0]

        if existing_id == -1:
            query = f'INSERT INTO Director (directorName, otherFamousMovie) VALUES("{directorDetails.get_directorName()}", "{directorDetails.get_otherFamousMovie()}")'
            self.conn.execute_query(query)
            existing_id = self.conn.cursor.lastrowid
        return existing_id
