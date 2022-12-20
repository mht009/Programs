# Program to input a character and to print whether a given character is an alphabet,digit or any other character
ch = input("Enter a character : ")
if ch.isalpha() :
    print(ch, "is an alphabet")
elif ch.isdigit():
    print(ch, "is a digit")
elif ch.isalnum() :
    print(ch, "is an alphanumeric")
else:
    print(ch, "is a special character")
