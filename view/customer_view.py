from model.customer import Customer
from controller.customer_controller import CustomerController
from view.view import View
from datetime import datetime

class CustomerView(View):

    def CustomerMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Customers')
        print('[2] -- New Customer')
        print('[3] -- Delete Customer')
        print('[4] -- Return to Main Menu')
        return int(input(self.REQUIRE_OPTION_MESSAGE))

    def insertCustomerForm(self): 
        customer_controller = CustomerController()
        
        name = input("Name: ")
        document = input("Document: ")
        active = 1
        register_date = datetime.now().strftime('%Y-%m-%d')
        update_date = datetime.now().strftime('%Y-%m-%d')
        
        customer = Customer(0, name, document, active, register_date, update_date)
        
        actionResponse = customer_controller.insert(customer)
        print(actionResponse)
    
    def listCustomers(self):
        customer_controller = CustomerController()
        customerList = customer_controller.listAll()
        for customer in customerList:
            print('----['+ str(customer.id) +']----')
            print("NAME = " + customer.name)
            print("DOCUMENT = " + customer.document)            
    
    def deleteCustomerForm(self):
        customer_controller = CustomerController()
        id = input("Customer ID: ")
        customer = customer_controller.findById(id)
        if customer: 
            confirm = input("Do you want to remove " + customer.name + "? [Y/N]")
            if confirm:
                print(customer_controller.delete(customer.id))
        else:
            print("\nCustomer with ID " + str(id) + " was not found")


