def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))

#named function
def polynomial(x):
    return x**2 + 5*x + 4

print(polynomial(-4))


#lambda(anonymous function)
print((lambda x: x**2 + 5*x + 4) (-4))

#lambda using variable
double = lambda x: x * 2
print(double(4))