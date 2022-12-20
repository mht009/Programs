# Program to take input from user and check whether it is prime or not
import math
num = int(input("Enter a Number : "))
isPrime = True

for i in range(2,int(math.sqrt(num))+ 1):
    if num % i == 0:
        isPrime = False

if isPrime:
    print("Number is Prime Number")
else:
    print("Number is not Prime Number")
