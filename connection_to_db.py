import sqlite3


class DBConnection:
    __instance = None

    def __init__(self) -> None:
        if DBConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DBConnection.__instance = self

    @staticmethod
    def get_instance():
        if DBConnection.__instance is None:
            DBConnection()
        return DBConnection.__instance

    def get_connection(self):
        try:
            self.conn = sqlite3.connect('dataset5.db')
            self.cursor = self.conn.cursor()
            print("Connection to database is successful")
        except sqlite3.Error as e:
            print("Connection to database is not successful")
            print(e)

    def close_connection(self):
        try:
            self.conn.close()
            print("Connection to database is closed")
        except sqlite3.Error as e:
            print("Connection to database is not closed")
            print(e)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.conn.commit()
            # print("Query executed successfully!!!")
            return result

        except sqlite3.Error as e:
            print("Query not executed")
            print(e)
