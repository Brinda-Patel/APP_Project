from connection_to_db import DBConnection


class movieDetailsMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()
        self.table_name = "movieDetails"
