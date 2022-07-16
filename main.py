from view.view import View


class main():

    def start(self):
        self.viewObject = View()

        mainMenuOption = 0

        while mainMenuOption != 4:
            mainMenuOption = self.viewObject.MainMenu()

            if mainMenuOption == 1:
                itemMenuOption = 0

                while itemMenuOption != 5:
                    itemMenuOption = self.viewObject.ItemsMenu()

                    if itemMenuOption == 1:
                        self.viewObject.listItems()
                    
                    if itemMenuOption == 2:
                        self.viewObject.listItems()

                    if itemMenuOption == 3:
                        itemMenuOption = self.viewObject.insertItemForm()

                    if itemMenuOption == 4:
                        self.viewObject.deleteItemForm()

            if mainMenuOption == 2:
                customerMenuOption = 0
                while customerMenuOption != 4:
                    customerMenuOption = self.viewObject.CustomerMenu()

                    if customerMenuOption == 2:
                        self.viewObject.insertCustomerForm()
            
            if mainMenuOption == 3:
                saleMenuOption = 0
                while saleMenuOption != 4:
                    saleMenuOption = self.viewObject.SalesMenu()


            if mainMenuOption == 4:
                self.viewObject.goodbyeMessage()


if __name__ == '__main__':
    mainApplication = main()
    mainApplication.start()
