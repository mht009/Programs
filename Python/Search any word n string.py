#Program to find the presence of any word from a sentence
def countWord(str1, word):
    sen = sentence.split()
    count = 0
    for a in sen :
        if a == word :
            count += 1
    return count

sentence = input("Enter sentence : ")
word = input("Enter the word which is to be searched : ")
count = countWord(sentence, word)

if count == 0:
    print("Entered word", word, "is not present in given sentence")
else:
    print(word, "occurs", count, "times !")
