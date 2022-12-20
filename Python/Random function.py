# Program to generate random number between 1-6 simulating a dice
import random
import time
print("Press CTRL + C to stop the dice ")
play = "y"
while play.lower() == "y" :
    try:
        while True :
            for i in range(2) :
                print()
            n = random.randint(1,6)
            print(n, end = '')
            time.sleep(0.0001)
    except KeyboardInterrupt :
        print('Number is ' , n)
        ans = input('Want To Play More ? (y/n) : ' )
        if ans.lower() != 'y' :
            play = 'n'
            break
