from controller.database import Database

from model.sale import Sale

class SaleController():

    def __init__(self):
        self.db_connection = Database().createConnection()

    def insert(self, sale: Sale):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("INSERT INTO SALE("
                        + "ITEM_ID, CUSTOMER_ID,"
                        + "QUANTITY, REGISTER_DATE,"
                        + "UPDATE_DATE) VALUES(:item_id,"
                        + ":customer_id, :quantity,"
                        + ":register_date, :update_date)", {
                          "item_id": sale.item_id,
                          "customer_id": sale.customer_id,
                          "quantity": sale.quantity,
                          "register_date": sale.register_date,
                          "update_date": sale.update_date  
                        })
        if db_cursor.rowcount > 0:
            print('$$$ Success on Sale $$$')
        self.db_connection.commit()
        db_cursor.close()
    
    def listAll(self): 
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("SELECT SALE.ID, ITEMS.NAME, CUSTOMER.NAME, SALE.QUANTITY, SALE.REGISTER_DATE, SALE.UPDATE_DATE FROM SALE INNER JOIN ITEMS ON SALE.ITEM_ID = ITEMS.ID INNER JOIN CUSTOMER ON SALE.CUSTOMER_ID = CUSTOMER.ID")
        saleList = []
        for row in db_cursor.fetchall():
            saleList.append(Sale(row[0], row[1], row[2],
                                row[3], row[4], row[5]))
        db_cursor.close()
        return saleList