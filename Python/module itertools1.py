'''
The module itertools is a standard library that contains several functions that are useful in functional programming.
One type of function it produces is infinite itereators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable(eg. list or strings)
The function repeat repeates an object, either infinite or a specific no. of times.
'''

from itertools import count, accumulate, takewhile, product, permutations


for i in count(3):
    print(i)
    if i >= 11:
        break

nums = list(accumulate(range(9)))
print(nums)
print(list(takewhile(lambda x : x <= 6, nums)))

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
