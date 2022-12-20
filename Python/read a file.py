# Program to read a file line by line each word separated by %
filer = open("pytextfile.txt", "r")
for l in filer:
    word = l.split()
    for w in word:
        print(w + "%", end = "")
    print()
filer.close()
