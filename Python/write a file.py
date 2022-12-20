# Program to write a text file
filehan = open("pytextfile1.txt","w")

b = int(input("How many lines do you want to enter : "))
for i in range(b):
    text = input("Enter Text : " )
    filehan.write(text + "\n")
filehan.close()
