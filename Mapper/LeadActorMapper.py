from connection_to_db import DBConnection

class LeadActorMapepr:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def create_actorDetails(self):
        query = f'CREATE TABLE IF NOT EXISTS Actor(leadActor_id INTEGER PRIMARY KEY AUTOINCREMENT, actorName varchar(20), actorAge int)'
        return self.conn.execute_query(query)

    def insert_actorDetails(self, actorDetails):
        query = f'INSERT INTO Actor (actorName, actorAge) VALUES("{actorDetails.get_actorName()}", "{actorDetails.get_actorAge()}")'
        return self.conn.execute_query(query)

    