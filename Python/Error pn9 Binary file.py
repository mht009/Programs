# Program to create a binary file to store Rollno and name and search for Rollno and display record if found otherwise show Rollno not found
a = 'z'

import pickle
student = []
filehan = open("Student.dat","wb")
ans = 'y'
while ans.lower() == 'y' :
    rollno = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    student.append([rollno, name])
    ans = input("Do you want to add more (y/n) : ")
pickle.dump(student,filehan)
filehan.close()

filehan = open('Student.dat', 'rb')
student = []
while True :
    try:
        student = pickle.load(filehan)
    except EOFError:
        break

ans = 'y'
while ans.lower() == 'y' :
    found = False
    r = int(input("Enter Roll Number which is to be searched : "))
    for s in student :
        if s[0] == r :
            print ("Name of student with Roll no.", r, "is", s[1])
            found = True
            break
        if not found:
            print("Sorry! Roll number not found. ")
            
ans = input("Search more ? (y/n)")
filehan.close()
            
    
