''' Due to the fact that they yield one item at a time, generaors don't have the memory restrictions of the lists.
    Infact they can be infinite
'''

def infinite_sevens():
    while True:
        yield 7

for i in infinite_sevens():
    print(i)

# inshort, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop