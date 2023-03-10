'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to forma new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets the item in first set but not in the second.
The symmetric difference operator ^ gets items in either set but not in both.
'''

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
