from msilib.schema import tables
from controller.database import Database

DATABASE_NAME = 'py-simple-store.db'

def generateItemsTable():
    database = Database()
    database.createConnection()
    database_cursor = database.getCursor()
    database_cursor.execute("CREATE TABLE IF NOT EXISTS ITEMS( "
                            + "ID INTEGER PRIMARY KEY,"
                            + "NAME TEXT NOT NULL,"
                            + "DESCRIPTION TEXT,"
                            + "PRICE NUMERIC NOT NULL,"
                            + "QUANTITY INTEGER NOT NULL,"
                            + "ACTIVE INTEGER NOT NULL,"
                            + "REGISTER_DATE TEXT NOT NULL,"
                            + "UPDATE_DATE TEXT NOT NULL)")
    
    database_cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER( "
                            + "ID INTEGER PRIMARY KEY,"
                            + "NAME TEXT NOT NULL,"
                            + "DOCUMENT TEXT,"
                            + "ACTIVE INTEGER NOT NULL,"
                            + "REGISTER_DATE TEXT NOT NULL,"
                            + "UPDATE_DATE TEXT NOT NULL)")

    database_cursor.execute("CREATE TABLE IF NOT EXISTS SALE( "
                            + "ID INTEGER PRIMARY KEY,"
                            + "ITEM_ID INTEGER NOT NULL,"
                            + "CUSTOMER_ID INTEGER NOT NULL,"
                            + "QUANTITY INTEGER NOT NULL,"
                            + "REGISTER_DATE TEXT NOT NULL,"
                            + "UPDATE_DATE TEXT NOT NULL,"
                            + "FOREIGN KEY (ITEM_ID) REFERENCES ITEM(ID),"
                            + "FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID))")

    database.closeConnection()


generateItemsTable()
