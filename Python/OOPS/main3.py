class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recievied arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quanity {quantity} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #print(f"{name} {price}")

    def cal_tprice(self):
        return self.price * self.quantity

item1 = Item("Phone", 1200, 10)
item2 = Item("Laptop", 5000, 3)


#item2.has_nampad = False

print(item1.cal_tprice())
print(item2.cal_tprice())