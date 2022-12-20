''' Generators are a type of iterables, like lists or tuples.
    Unlike list they do not allow indeing with arbitrary indices, but they still be iterated through with for loops.
    They can be created using functions and the yield statement
'''

def countdown():
    i = 10
    while i > 0 :
        yield i
        i -= 1

for i in countdown():
    print(i)
    #print("#")

''' The yield statement is used to define a generator, replacing the return of a function to provide a result to its 
    caller without destroying local variables
'''