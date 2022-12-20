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
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 1200, 10)

print("Before applying discount",item1.price)
item1.app_discount()
print("After applying discount", item1.price)


item2 = Item("Laptop", 5000, 3)
item2.pay_rate = 0.7


print(f"Before applying discount on laptop :{item2.price}")
item2.app_discount()

print(f"After applying discount on laptop : {item2.price}\n")
