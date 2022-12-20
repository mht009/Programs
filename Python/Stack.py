# Program to implement stack

def isEmpty(S) :
    if len(S) == 0 :
        return True
    else:
        return False

def Push(S, item):
    S.append(item)
    top = len(S) - 1

def Pop(S):
    if isEmpty(S):
        return "Umderflow"
    else:
        val = S.pop()
        if len(S) == 0:
            top = None
        else:
            top = len(S) - 1
        return val

def Peek(S):
    if isEmpty(S):
        return "Underflow"
    else:
        top = len(S) - 1
        return S[top]

def Show(S) :
    if isEmpty(S):
        print("Sorry No Items in Stack")
    else :
        t = len(S) - 1
        print("(Top)", end = '')
        while(t >= 0):
            print(S[t], "<==", end = '')
            t = t-1
        print()

# Main Program Begins Here
S = []      #Stack
top = None
while True :
    print("STACK DEMONSTRATION")
    print("1 Push")
    print("2 Pop")
    print("3 Peek")
    print("4 Show Stack")
    print("0 Exit")
    print()
    ch = int(input("Enter You Choice : "))

    if ch == 1 :
        val = int(input("Enter Item To Push : "))
        Push(S, val)

    elif ch == 2 :
        val = Pop(S)
        if val == "Underflow":
            print("Stack is Empty")
        else :
            print("\nDeleted Item was :  ", val)

    elif ch == 3:
        val = Peek(S)
        if val == "Underflow" :
            print("Stack Empty")
        else:
            print("Top Item : ", val)
    
    elif ch == 4 :
        Show(S)

    elif ch == 0 :
        print("Thank You ! ")
        break
