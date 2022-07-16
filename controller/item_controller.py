import json
from controller.database import Database
from model.item import Item


class ItemController():

    

    def __init__(self):
        self.db_connection = Database().createConnection()

    def insert(self, item: Item):
        db_cursor = self.db_connection.cursor()
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
        self.db_connection.commit()
        db_cursor.close()
    
    def listAll(self):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute('SELECT * FROM ITEMS WHERE ACTIVE = 1')
        itemList = []
        for row in db_cursor.fetchall():
            itemList.append(Item(row[0], row[1],
                                row[2], row[3],
                                row[4], row[5],
                                row[6], row[7]))
        db_cursor.close()
        return itemList
    
    def findById(self, id):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute('SELECT * FROM ITEMS WHERE id = :id', {"id":id})
        row = db_cursor.fetchone()
        db_cursor.close()
        if row:
            return Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        else:
            return False
    
    def delete(self, id):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("UPDATE ITEMS SET active = 0 WHERE id = :id", {"id": id})
        message = ""
        if db_cursor.rowcount > 0:
            message = "*** Item removed with success ***"
        else:
            message ="*** This item cannot be removed ***"
        
        self.db_connection.commit()
        db_cursor.close()
        
        return message