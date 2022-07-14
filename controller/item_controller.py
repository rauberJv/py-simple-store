from controller.database import Database
from model.item import Item


class ItemController():

    DATABASE_NAME = 'py-simple-store.db'

    def __init__(self):
        self.db_connection = Database(self.DATABASE_NAME)
        self.db_connection.createConnection()

    def insert(self, item: Item):
        db_cursor = self.db_connection.getCursor()
        db_cursor.execute("INSERT INTO ITEMS("
                          + "NAME, DESCRIPTION,"
                          + "PRICE, QUANTITY,"
                          + "ACTIVE, REGISTER_DATE,"
                          + "UPDATE_DATE) VALUES("
                          + ":name, :description, :price,"
                          + ":quantity, :active, :register_date,"
                          + ":update_date)",
                          {"name": item.name, "description": item.description,
                           "price": item.price, "quantity": item.quantity,
                           "active": item.active, "register_date": item.register_date,
                           "update_date": item.update_date})
        print(db_cursor.lastrowid)
        db_cursor.close()
