# Program to find the ASCII code of a character and vice versa
var = True
while var :
    ans = int(input("Press 1 to find the ordinal value of a character \nPress 2 to find a character value \n"))
    if ans == 1 :
        ch = input("Enter a character : ")
        print(ord(ch))
    elif ans == 2 :
        val = int(input("Enter an integer value : "))
        print(chr(val))
    else :
        print("You entered wrong choice")
    ans = input("Do you want to continue? Y/N")
    if ans == "n" or ans == "N" :
        break
    
            
