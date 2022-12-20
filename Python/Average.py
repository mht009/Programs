# To get maths, physics, and chemistry marks from the user and calculates and diaplays its average
maths = int(input("Enter Maths marks : "))
phy = int(input("Enter Physics marks : "))
chem = int(input("Enter Chemistry marks : "))

print("marks of maths : ", maths)
print("marks of physics : ", phy)
print("marks of chemistry : ", chem)
avg = (maths + phy + chem)/3
print("Average of all the above subject is ", avg)
