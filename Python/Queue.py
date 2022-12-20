# Program to demonstrate Queue

def isEmpty(Q):
    if len(Q) == 0:
        return True
    else:
        return False

def Enqueue(Q,item):
    Q.append(item)
    if len(Q) == 1 :
        front = rear = 0
    else :
        rear = len(Q) - 1

def Dequeue(Q):
    if isEmpty(Q):
        return "Underflow"
    else:
        val = Q.pop(0)

    if len(Q) == 0 :
        front = rear = None

    return val

def Peek (Q):
    if isEmpty(Q) :
        return "Underflow"
    else:
        front = 0
        return Q[front]

def Show(Q):
    if isEmpty(Q):
        print("Sorry no items in Queue")
    else:
        t = len(Q) - 1
        print("(Front)", end = "")
        front = 0
        i = front
        rear = len(Q) - 1
        while (i <= rear) :
            print(Q[i], "==>", end = '')
            i += 1
        print()

Q = []  # Created an empty queue
front = rear = None
while True :
    print('QUEUE DEMONSTRATION')
    print('1 Enqueue')
    print('2 Dnqueue')
    print('3 Peek')
    print('4 Show Queue')
    print('0 Exit')

    ch = int(input("Enter You choice : "))
    if ch == 1 :
        val = int(input("Enter the item to insert : "))
        Enqueue(Q, val)

    if ch == 2 :
        val = Dequeue(Q)
        if val == "Underflow" :
            print("Queue is Empty")
        else:
            print("\nDeleted item was : ", val)
            
    elif ch == 3 :
        val = Peek(Q)
        if  val == "Underflow" :
            print("Queue Empty")
        else :
            print("Front Item : ", val)

    elif ch == 4 :
        Show(Q)

    elif ch == 0 :
        print("Thank You !")
        break
