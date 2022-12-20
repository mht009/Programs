sum = 0
k = 1
n = int(input("Enter the no.: "))
for i in range(0,n+1):

    k = i*2
    #print("k",k)

    sum = sum + k
    #print("sum",sum)

print("Sum of first",n,"even no. is",sum)