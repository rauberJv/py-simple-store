from controller.database import Database
from model.customer import Customer

class CustomerController():

    def __init__(self):
        self.db_connection = Database().createConnection()

    def listAll(self):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute('SELECT * FROM CUSTOMER WHERE ACTIVE = 1')
        list = db_cursor.fetchall()
        customerList = []
        for customer in list:
            customerList.append(Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5]))
        db_cursor.close()
        return customerList

    def insert(self, customer: Customer):
        actionResponse = ""
        db_cursor = self.db_connection.cursor()
        
        db_cursor.execute("INSERT INTO CUSTOMER("
                        + "NAME, DOCUMENT, ACTIVE,"
                        + "REGISTER_DATE, UPDATE_DATE)"
                        + "VALUES (:name, :document, :active,"
                        + ":register_date, :update_date)",
                        {"name": customer.name, "document": customer.document,
                        "active": customer.active, "register_date": customer.register_date,
                        "update_date": customer.update_date})
        self.db_connection.commit()
        
        if db_cursor.lastrowid > 0: 
            actionResponse = "Customer " + customer.name + " registered."
        else:
            actionResponse = "Failed on customer register."
        
        db_cursor.close()
        return actionResponse

        