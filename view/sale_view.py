from controller.customer_controller import CustomerController
from controller.item_controller import ItemController
from model.sale import Sale
from controller.sales_controller import SaleController
from view.view import View
from datetime import datetime

class SaleView(View):

    def SalesMenu(self):
        print(self.SELECT_OPTION_MESSAGE)
        print('[1] -- List Sales')
        print('[2] -- New Sale')
        print('[3] -- Sales Report')
        print('[4] -- Return to Main Menu')
        return int(input(self.REQUIRE_OPTION_MESSAGE))
    
    def listSales(self):
        sale_controller = SaleController()
        saleList = sale_controller.listAll()
        for sale in saleList:
            print("ID = " + str(sale.id))
            print("ITEM = " + str(sale.item_id))
            print("CUSTOMER = " + str(sale.customer_id))
            print("QUANTITY = " + str(sale.quantity))
            print('\n')

    def insertSaleForm(self):
        customer_controller = CustomerController()
        item_controller = ItemController()
        sale_controller = SaleController()
        item_id = input("Item ID: ")
        customer_id = input("Customer ID: ")
        quantity = input("Quantity: ")
        item = item_controller.findById(item_id)
        customer = customer_controller.findById(customer_id)
        register_date = datetime.now().strftime('%Y-%m-%d')
        update_date = datetime.now().strftime('%Y-%m-%d')

        if item and customer:
            if int(quantity) <= int(item.quantity):
                sale = Sale(0, item.id, customer.id, quantity, register_date, update_date)
                sale_controller.insert(sale)
            else:
                print("### Item has only " + item.quantity + " unities")
        else:
            print("??? Item or Customer not found. Try again ???")    