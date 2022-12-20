# Collatz Conjecture
'''
Take any natural number
if even- divide it by two
if odd- multiply by 3 and add 1 (3x+1)
repeat until we get 1
'''

from time import sleep
import matplotlib.pyplot as plt
import matplotlib


def scan():
    try:
        number = int(input("Enter a positive integer: "))
        
        if(number>0):
            return number

        if(number == 0):
            print("Invalid!")
            scan()

        else:
            return number * (-1)

    except (ValueError, TypeError, KeyboardInterrupt):
        print("Invalid Input!!!")
        scan()


def HailStone_Numbers(num, step, x, y):
    try:
        # sleep(1)
        if(num == 1):
            return num, step, x, y
        
        if(num%2 == 0):
            num /= 2
            step +=1

            x.append(step)
            y.append(num)
            # print(int(num), step, x, y)
            print(int(num))


            HailStone_Numbers(num, step, x, y)

        else:
            num = (3 * num)+1
            step +=1

            x.append(step)
            y.append(num)
            # print(int(num), step, x, y)
            print(int(num))


            HailStone_Numbers(num, step, x, y)


    except KeyboardInterrupt:
        return

def graph(x, y, num):
    plt.plot(x, y)
    plt.xlabel('No.of Steps')
    plt.ylabel('Hailstone Number')

    plt.xscale('linear')
    plt.yscale('linear')

    plt.title("Collatz Conjecture")

    plt.show()



def main():
    
    step = 0

    num1 = scan()
    x = [0]
    y = [num1]

    HailStone_Numbers(num1, step, x, y)

    # print(x, y)

    graph(x, y, num1)


main()
