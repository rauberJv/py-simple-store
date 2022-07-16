from argparse import _ActionStr
from atexit import register
from datetime import datetime
from model.customer import Customer
from model.item import Item
from controller.item_controller import ItemController
from controller.customer_controller import CustomerController


class View():
    HI_MESSAGE = "'\n##Welcome to PY Simple Store##\n'"
    BYE_MESSAGE = '\n##Thank you! Goodbye##\n'
    SELECT_OPTION_MESSAGE = "\nSelect a option from the menu below"

    def __init__(self):
        self.welcomeMessage()

    def welcomeMessage(self):
        now = datetime.now()
        print(self.HI_MESSAGE)
        print(now.strftime('%c'))

    def goodbyeMessage(self):
        now = datetime.now()
        print(self.BYE_MESSAGE)
        print(now.strftime('%c'))

    def MainMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- Items Menu')
        print('[2] -- Customer Menu')
        print('[3] -- Sale Menu')
        print('[4] -- Exit Program ')
        return int(input("Your option: "))

    def ItemsMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Items')
        print('[2] -- Find by Id')
        print('[3] -- Create Item')
        print('[4] -- Delete Item')
        print('[5] -- Return to Main Menu')
        return int(input("Your option: "))

    def insertItemForm(self):
        item_controller = ItemController()
        name = input("Name: ")
        description = input("Description: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        active = 1
        register_date = datetime.now().strftime('%Y-%m-%d')
        update_date = datetime.now().strftime('%Y-%m-%d')
        new_item = Item(0, name, description, price, quantity,
                        active, register_date, update_date)
        item_controller.insert(new_item)
        return 4

    def listItems(self):
        item_controller = ItemController()
        itemList = item_controller.listAll()
        print("----Item List----")
        for item in itemList:
            print("ID = " + str(item.id))
            print("NAME = " + item.name)
            print("DESCRIPTION = " + item.description)
            print("PRICE = $" + str(item.price))
            print("QUANTITY = " + str(item.quantity))
            print('\n')

    def deleteItemForm(self):
        item_controller = ItemController()
        id = input("Item ID: ")
        item = item_controller.findById(id)
        if item:
            confirm = input("Do you want to remove " + item.name + "? [Y/N]")
            if confirm:
                print(item_controller.delete(id))
        else:
            print("\nItem with ID " + str(id) + " was not found")

    def CustomerMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Customers')
        print('[2] -- New Customer')
        print('[3] -- Delete Customer')
        print('[4] -- Return to Main Menu')
        return int(input("Your optionn: "))

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


    def SalesMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Sales')
        print('[2] -- New Sale')
        print('[3] -- Sales Report')
        print('[4] -- Return to Main Menu')
        return int(input("Your option: "))


