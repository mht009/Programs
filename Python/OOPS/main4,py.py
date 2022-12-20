class Item:
    pay_rate = 0.8      # The pay rate after 20% discount

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

    def app_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone", 1200, 10)
item2 = Item("Laptop", 5000, 3)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__)        # All attributes for class level
print(item1.__dict__)       # All attributes for instance level

print("###################################\n")

print("Before applying discount",item1.price)
item1.app_discount()
print("After applying discount", item1.price)
