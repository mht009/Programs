n = int(input("Enter No. : "))


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
print(0)      
for i in range(0, n-1):
    print(fibonacci(i))

