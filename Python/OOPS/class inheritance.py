#concept of inheritance

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self)