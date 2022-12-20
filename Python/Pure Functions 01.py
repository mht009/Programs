#pure function
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

#impure function
some_list =[]

def impure(arg):
    some_list.append(arg)


print(pure_function(5, 6))
print(impure(1))
print(some_list)