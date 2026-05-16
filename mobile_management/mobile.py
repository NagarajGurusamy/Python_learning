class Mobile:
    def __init__(self, brand, model, price, stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock

    def show(self):
        print("\nMobile Details")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        print("Stock :", self.stock)

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated successfully!")

    def add_stock(self, quantity):
        self.stock += quantity
        print("Stock added successfully!")

    def sell_mobile(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            total = quantity * self.price
            print("Mobile sold successfully!")
            print("Total Bill :", total)
        else:
            print("Not enough stock available!")


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self):
        brand = input("Enter brand name: ")
        model = input("Enter model name: ")
        price = int(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))

        mobile = Mobile(brand, model, price, stock)
        self.mobiles.append(mobile)
        print("Mobile added successfully!")

    def view_all_mobiles(self):
        if len(self.mobiles) == 0:
            print("No mobiles available!")
        else:
            for i, mobile in enumerate(self.mobiles):
                print("\nMobile Number:", i + 1)
                mobile.show()

    def search_mobile(self):
        search_model = input("Enter model name to search: ")

        found = False
        for mobile in self.mobiles:
            if mobile.model.lower() == search_model.lower():
                mobile.show()
                found = True
                break

        if not found:
            print("Mobile not found!")

    def update_mobile_price(self):
        search_model = input("Enter model name: ")

        for mobile in self.mobiles:
            if mobile.model.lower() == search_model.lower():
                new_price = int(input("Enter new price: "))
                mobile.update_price(new_price)
                return

        print("Mobile not found!")

    def add_mobile_stock(self):
        search_model = input("Enter model name: ")

        for mobile in self.mobiles:
            if mobile.model.lower() == search_model.lower():
                quantity = int(input("Enter quantity to add: "))
                mobile.add_stock(quantity)
                return

        print("Mobile not found!")

    def sell_mobile(self):
        search_model = input("Enter model name: ")

        for mobile in self.mobiles:
            if mobile.model.lower() == search_model.lower():
                quantity = int(input("Enter quantity to sell: "))
                mobile.sell_mobile(quantity)
                return

        print("Mobile not found!")

    def menu(self):
        while True:
            print("\n===== Mobile Store Management =====")
            print("1. Add Mobile")
            print("2. View All Mobiles")
            print("3. Search Mobile")
            print("4. Update Mobile Price")
            print("5. Add Stock")
            print("6. Sell Mobile")
            print("7. Exit")

            choice = int(input("Enter your choice(1/2/3/4/5/6/): "))

            if choice == 1:
                self.add_mobile()
            elif choice == 2:
                self.view_all_mobiles()
            elif choice == 3:
                self.search_mobile()
            elif choice == 4:
                self.update_mobile_price()
            elif choice == 5:
                self.add_mobile_stock()
            elif choice == 6:
                self.sell_mobile()
            elif choice == 7:
                print("Thank you for using Mobile Store System!")
                break
            else:
                print("Invalid choice!")


store = MobileStore()
store.menu()