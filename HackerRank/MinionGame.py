'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.'''

# Program
string = "NANANNA"
subStrings = []

for i in range(len(string)):
    for j in range(i+1, len(string) +1):
        subStrings.append(string[i:j])

vowel = ['A', 'E', 'I', 'O', 'U']
kevin = []      #vowel
stuart = []     #consonants


for sub in subStrings:
    if(sub[0] in vowel):
        kevin.append(sub)
    else:
        stuart.append(sub)


# print(subStrings)
# print(kevin)
# print(stuart)

if(len(stuart)>len(kevin)):
    print("Stuart", len(stuart))

#elif(len(stuart)<len(kevin)):
 #   print("Kevin", len(kevin))

else:
    print("Draw")
