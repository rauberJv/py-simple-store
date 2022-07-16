import sqlite3


class Database():
    DATABASE_NAME = 'py-simple-store.db'        

    def createConnection(self):
        self.connection = sqlite3.connect(self.DATABASE_NAME)
        return self.connection

    def closeConnection(self):
        self.connection.close()

    def getCursor(self):
        return self.connection.cursor()

