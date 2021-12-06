class Item:
    price_after_discount = 0.8
    items_list = []
    def __init__(self, name: str, price: float, quantity=0):

        # validations
        assert price >= 0, f"the price {price} is negative"
        assert quantity > 0, f"the quantity cannot be zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        #actions
        Item.items_list.append(self)


    def calculate_total(self):
        return self.actual_amt()*self.quantity

    def actual_amt(self):
        self.price = self.price*self.price_after_discount

        return self.price


i1 = Item("Phone", 100, 1)
i2 = Item("laptop", 1000, 3)
i3 = Item("Cable", 10, 3)
i4 = Item("Mouse", 50, 3)
i5 = Item("Keyboard", 75, 5)

for items in i1.items_list:
    print(items.name)


