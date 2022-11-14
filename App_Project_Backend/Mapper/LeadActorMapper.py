from Connection import DBConnection

<< << << < HEAD

== == == =
>>>>>> > 3d1db693133c506c4426269e15fb7a8b418898c2


class LeadActorMapper:
    def __init__(self):
        self.conn = DBConnection.get_instance()
        self.conn.get_connection()

    def create_actorDetails(self):
        query = f'CREATE TABLE IF NOT EXISTS Actor(leadActor_id INTEGER PRIMARY KEY AUTOINCREMENT, actorName varchar(20) UNIQUE, actorAge int)'
        print("Table Created Successfully")
        return self.conn.execute_query(query)

    def getRowByActorName(self, actorName):
        inspect_existing_query = f'SELECT leadActor_id FROM Actor WHERE actorName = "{actorName}"'
        try:
            self.conn.cursor.execute(inspect_existing_query)
            res = self.conn.cursor.fetchone()
        except Exception as e:
            print(e)
        return res

    def insert_actorDetails(self, actorDetails):
        existing_id = -1
        get_existing_id = self.getRowByActorName(actorDetails.get_actorName())
        if get_existing_id is not None:
            existing_id = get_existing_id[0]
        if existing_id == -1:
            query = f'INSERT INTO Actor (actorName, actorAge) VALUES("{actorDetails.get_actorName()}", "{actorDetails.get_actorAge()}")'
            self.conn.execute_query(query)
            existing_id = self.conn.cursor.lastrowid
        return existing_id
