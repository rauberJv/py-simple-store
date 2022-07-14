from msilib.schema import tables
from controller.database import Database

DATABASE_NAME = 'py-simple-store.db'
ITEMS_TABLE = "ITEMS"
SALES_TABLE = "SALES"


def generateItemsTable():
    database = Database(DATABASE_NAME)
    database.createConnection()
    database_cursor = database.getCursor()
    database_cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=:table", {"table": ITEMS_TABLE})
    tablesResult = database_cursor.fetchall()

    if len(tablesResult) <= 0:
        database_cursor.execute("CREATE TABLE IF NOT EXISTS ITEMS( "
                                + "ID INTEGER PRIMARY KEY,"
                                + "NAME TEXT NOT NULL,"
                                + "DESCRIPTION TEXT,"
                                + "PRICE NUMERIC NOT NULL,"
                                + "QUANTITY INTEGER NOT NULL,"
                                + "ACTIVE INTEGER NOT NULL,"
                                + "REGISTER_DATE TEXT NOT NULL,"
                                + "UPDATE_DATE TEXT NOT NULL)")
    else:
        print('Table ' + ITEMS_TABLE + ' already exists.')

    database.closeConnection()


generateItemsTable()
