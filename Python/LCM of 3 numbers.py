from itertools import count

x = int(input("Enter 1st no. : "))
y = int(input("Enter 2nd no. : "))
z = int(input("Enter 3rd no. : "))

for i in count(1):
    if (i % x == 0) and (i % y == 0) and (i % z == 0) :
        print("LCM of ", x, y, z, "is ", i)
        break
    else:
        pass
