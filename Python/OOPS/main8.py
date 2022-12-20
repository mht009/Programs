class Item:
    pay_rate = 0.8      # The pay rate after 20% discount

    all =[]

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the recievied arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quanity {quantity} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to be executed
        Item.all.append(self)

        #print(f"{name} {price}")

    def cal_tprice(self):
        return self.price * self.quantity

    def app_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"



print(Item.all)

for instance in Item.all:
    print(f"{instance.name}")