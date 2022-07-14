import sqlite3


class Database():

    def __init__(self, db_name):
        self.db_name = db_name

    def createConnection(self):
        self.connection = sqlite3.connect(self.db_name)

    def closeConnection(self):
        self.connection.close()

    def getCursor(self):
        return self.connection.cursor()

