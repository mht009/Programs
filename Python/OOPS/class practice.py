class Students:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name + " says hi")


obj = Students("John")
obj.greet()
        