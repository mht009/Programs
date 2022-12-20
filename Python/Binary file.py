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
print(student)

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
                found = True
                
                break
                ans='n'
    if found==True:
         print("The name with roll no.",r,"is",s[1])
    else:
        print("Not Found")

    ans = input("Search more ? (y/n)")

filehan.close()
            
    
