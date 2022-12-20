"""Decorators provide a way to modfy functions using other functions.
    This is ideal when need to extend the functionality of functions that you dont't want to modify"""

def decor(func):
    def wrap():
        print("====================")
        func()
        print("====================")
    return wrap

def print_text():
    print("Hello World!")

decorated = decor(print_text)
decorated() 