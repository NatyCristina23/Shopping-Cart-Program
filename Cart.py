class shopping:
    def __init__ (self, item):

        self.item = item
        self.cart = []
        self.items = {"Pizza" : 10.99, "Meat" : 5.99, "Vegetables" : 7.99, "Fish" : 4.99, "Bread" : 1.99}

    def add(self, item):
        self.cart.append(item)

    def display_items(self):
        for item in self.cart:
            print(f"You bought: {item}")
