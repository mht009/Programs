# Program to read the contents of a file and display the total nmber of consonant, upper case and lower case characters
fileh = open("pytextfile.txt", "r")
vw = cn = uc = lc = ot = 0
data = fileh.read()
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for ch in data :
    if ch.isalpha():
        if ch in vowels :
            vw += 1
        else:
            cn += 1

    if ch.isupper():
        uc += 1
    elif ch.islower():
        lc += 1
    elif ch != ' ' and ch != '\n' :
        ot += 1
print("Total Vowels in the file : ", vw)
print("Total Consonants in the file : ", cn)
print("Total Capital Letters in the file : ", uc)
print("Total Small Letters in the file : ", lc)
print("Total Words other than letters in the file : ", ot)
fileh.close()
