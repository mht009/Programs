def minion_game(string):
   
    try:
        subStrings = []

        for i in range(len(string)):
            for j in range(i+1, len(string) +1):
                subStrings.append(string[i:j])

        vowel = ['A', 'E', 'I', 'O', 'U']
        kevin = 0     #vowel
        stuart = 0     #consonants


        for sub in subStrings:
            if(sub[0] in vowel):
                kevin+=1
            else:
                stuart+=1


        # print(subStrings)
        # print(kevin)
        # print(stuart)

        if(stuart>kevin):
            print("Stuart", stuart)

        #else:
        elif(stuart<kevin):
            print("Kevin", kevin)

        else:
            print("Draw")


    except MemoryError:
        print("Memory Error")

if __name__ == '__main__':
    s = input()
    minion_game(s)