# Program to create a Binary File to store Rollno and name
import pickle
student = []
filehan = open('student1.dat','wb')

ans = 'y'
while ans.lower() == 'y' :
    roll = int(input("Enter Roll number : "))
    name = input("Enter name : ")
    marks = int(input("Enter marks :"))
    student.append([roll,name,marks])
    ans = input("Add More (y/n): ")
    pickle.dump(student,filehan)
filehan.close()

filehan = open('student1.dat','rb+')
student = []
while True:
    try:
        student = pickle.load(filehan)
    except EOFError:
        break

ans = 'y'
while ans.lower() == 'y' :
    found = False
    r = int(input("Enter roll no. to update : "))
    for s in student :
        if s[0] == r :
            print("Name is ", s[1]) 
            print("Current Marks are ", s[2])
            m = int(input("Enter new Marks : "))
            s[2] = m
            print("Record Updated ! ")
            found = True
            break
        if not found :
            print("Roll Number not found")
    ans = input("Want To update more ? (y/n) : ")
    filehan.close
