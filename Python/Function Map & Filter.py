# Map Function

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]

result =  list(map(add_five, nums))
#result =  list(map(add_five(nums)))        line 7 & 8 will give type error
#result =  list(add_five, nums)

print(result)       # We could achieve the same result using lambda syntax

#Alternate code
nums = [11, 22, 33, 44, 55]

result1 = list(map(lambda x : x + 5, nums))             # we have to explicitly convert the result into list(or tuple)
print(result1)

print("--------------------------------------------------------------")
# Filter Function

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2 == 0, nums))            # we have to explicitly convert the result into list(or tuple)
print(res)