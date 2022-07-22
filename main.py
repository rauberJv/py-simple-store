from view.customer_view import CustomerView
from view.item_view import ItemView
from view.sale_view import SaleView
from view.view import View


class main():

    def start(self):
        self.viewObject = View()
        self.itemView = ItemView()
        self.customerView = CustomerView()
        self.saleView = SaleView()

        mainMenuOption = 0
        
        self.viewObject.welcomeMessage()

        while mainMenuOption != 4:
            mainMenuOption = self.viewObject.MainMenu()

            if mainMenuOption == 1:
                itemMenuOption = 0

                while itemMenuOption != 5:
                    itemMenuOption = self.itemView.ItemsMenu()

                    if itemMenuOption == 1:
                        self.itemView.listItems()
                    
                    if itemMenuOption == 2:
                        self.itemView.listItems()

                    if itemMenuOption == 3:
                        self.itemView.insertItemForm()

                    if itemMenuOption == 4:
                        self.itemView.deleteItemForm()

            if mainMenuOption == 2:
                customerMenuOption = 0
                while customerMenuOption != 4:
                    customerMenuOption = self.customerView.CustomerMenu()

                    if customerMenuOption == 1:
                        self.customerView.listCustomers()

                    if customerMenuOption == 2:
                        self.customerView.insertCustomerForm()
                    
                    if customerMenuOption == 3:
                        self.customerView.deleteCustomerForm()
            
            if mainMenuOption == 3:
                saleMenuOption = 0
                while saleMenuOption != 4:
                    saleMenuOption = self.saleView.SalesMenu()

                    if saleMenuOption == 1:
                        self.saleView.listSales()

                    if saleMenuOption == 2:
                        self.saleView.insertSaleForm()


            if mainMenuOption == 4:
                self.viewObject.goodbyeMessage()


if __name__ == '__main__':
    mainApplication = main()
    mainApplication.start()
