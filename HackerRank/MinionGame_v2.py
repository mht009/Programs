from itertools import combinations

def repString(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            length = len(string)/len(substring)

            return substring, length

    length = int(len(string)/len(substring))

    return string, length


def minion_game(string):

    string, lenS = repString(string)
   
    try:

        subStrings = []
        vowel = ['A', 'E', 'I', 'O', 'U']

        kevin = 0     #vowel
        stuart = 0     #consonants

        lenO = 0 # size of all possible combinations of a string
        for i in range(len(string)):
            for j in range(i+1, len(string) +1):
                # sub = string[i:j]
                lenO +=1

        for x, y in combinations(range(int(len(string) + 1)), r = 2):
            sub = string[x:y] 
                
            if(sub[0] in vowel):
                kevin+=1
            else:
                stuart+=1

        
        if(stuart>kevin):
            print("Stuart", stuart*lenS)

        #else:
        elif(stuart<kevin):
            print("Kevin", kevin*lenS)

        else:
            print("Draw")


    except MemoryError:
        print("Memory Error")

if __name__ == '__main__':
    s = input()
    minion_game(s)
