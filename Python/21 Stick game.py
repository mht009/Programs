# Program to create 21 stick game where computer always wins
print("Rule of game(Total sticks = 21) : \n1) User and computer can pick one by one \n2) Maximum stick both can is 4 i.e. 1 to 4 \n3) Anyone with last stick will be the looser")
def PrintStick(n):
    print("o" * n)
    print("|" * n)
    print("|" * n)
    print("|" * n)
    print("|" * n)

TotalStick = 21
win = False
HumanPlayer = True
print("Welcome To Stick Picking Game : Computer Vs User")
print("-------------------Let's Begin------------------")
playername = input("Enter Your Name : ")
userPick = 0
PrintStick(TotalStick)

while win == False:
    if HumanPlayer == True :
        print("You can pick sick(s): ")
        userPick = 0
        while userPick <= 0 or userPick >4 :
            userPick = int(input(playername + " enter number of sticks to pick: "))
            TotalStick -= userPick
            HumanPlayer = False
            PrintStick(TotalStick)
            print("*" * 60)
            input("Press any key...")
        else:
            computerpick = (5 - userPick)
            print("Computer Picks : ", computerpick, "sticks")
            TotalStick -= computerpick
            PrintStick(TotalStick)
            if TotalStick <= 1 :
                print("Winner : Computer")
                win = True
                break
            print("*" * 60)
            input("Press any key...")
            HumanPlayer = True
