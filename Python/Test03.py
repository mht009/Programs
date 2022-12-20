evens = [i**2 for i in range(10) if i**2 % 2 ==0]
print(evens)

print("%10s"%"Mohit", "%20s"%"Nitin", "%20s"%"Gajbhiye")

nums = [4,5,6]
msg = "Numbers : {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)


a = "{x}, {y}".format(x=5, y=12)
print(a)