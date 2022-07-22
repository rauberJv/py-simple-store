from controller.item_controller import ItemController
from model.item import Item
from datetime import datetime

from view.view import View

class ItemView(View):

    def ItemsMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Items')
        print('[2] -- Find by Id')
        print('[3] -- Create Item')
        print('[4] -- Delete Item')
        print('[5] -- Return to Main Menu')
        return int(input(self.REQUIRE_OPTION_MESSAGE))

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