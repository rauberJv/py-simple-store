from datetime import datetime
from model.customer import Customer
from model.item import Item
from controller.item_controller import ItemController
from controller.customer_controller import CustomerController
from controller.sales_controller import SaleController
from model.sale import Sale


class View():
    HI_MESSAGE = "'\n##Welcome to PY Simple Store##\n'"
    BYE_MESSAGE = '\n##Thank you! Goodbye##\n'
    SELECT_OPTION_MESSAGE = "\nSelect a option from the menu below"
    REQUIRE_OPTION_MESSAGE = "Your option: "

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
        return int(input(self.REQUIRE_OPTION_MESSAGE))