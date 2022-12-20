def count_char(text, char):
    count = 0 
    for c in text:
        if c == char :
            count += 1
    return count


fh1 = open("poetry.txt")
text =  fh1.read()
char = input("Enter the character : ")

n = count_char(text, char)
print("No. of character ", char, "is", n)