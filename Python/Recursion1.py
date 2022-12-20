def factorial(x):
    if x == 1:
        #print("one")
        return True
    else:
        return x * factorial(x-1)

print(factorial(5))
