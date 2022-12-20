# Program to read the contents of a file line by line and write it to another file except the line tha contains "a" letter
import time
print('Copying lines from poerty to poetry copy without letter "a" ')
time.sleep(0.5)

# main program starts here
fh1 = open("Poetry.txt")
fh2 = open("poetrycopy.txt", "w")

for line in fh1 :               # fh1 is the file handle of the file poetry.txt 
    if "a" not in line :
        fh2.write(line)         # fh2 is the file handle of the file poetrycopy.txt

print("File Copied Successfully !")
print()

fh1.close()
fh2.close()

print("Original Poetry :",end = "\n\n")
fh1 = open("poetry.txt")
line = " "
while line :
    line = fh1.read()
    print(line)
    
print()
print('Poetry after removing lines with letter "a"',end = "\n\n")
fh2 = open("poetrycopy.txt")
line = " "
while line :
    line = fh2.read()
    print(line)
    
