#Program to calculate the factorial of entered number
num = int(input("Enter Number : "))
fact = 1
z = num

while num >= 1 :     # loop to interate from n to 1
    fact = fact * num
    num = num - 1
    
print("Factorial of ",z," is : ",fact)
