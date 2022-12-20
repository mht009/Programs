''' Program to create CSV file and store empno, name, salary, and seach any
empno and display name, salary and if not found shows appropriate message'''

import csv

while True :
    
    a = int(input("Press 1 for Entering Data..\nPress 2 for searching Data..\nPress 3 for Quitting..."))
    
    if a == 1:
        with open('Emplfile.csv', mode = 'a') as csvfile :
            filewriter = csv.writer(csvfile,delimiter = ',')
            ans = "y"
            while ans.lower() == "y" :
                empno = int(input("Enter Employee Number : "))
                name = input("Enter Name : ")
                salary = float(input("Enter salary of the Employee : "))
                filewriter.writerow([empno, name, salary])
                print("Data saved. ")
                ans = input("Want to add more ? (y/n) :")

    elif a == 2 :
        ans = "y"
        with open('Emplfile.csv', mode = "r") as csvfile :
            filereader = csv.reader(csvfile, delimiter =",")
            while ans.lower() == "y" :
                found = 0
                enum = input("Enter Employee Number To Be Search : ")
                for row in filereader :
                    if len(row) != 0 :
                        if row[0] == enum :
                    
                            print("-----------------------------------")
                            print("Name of employee : ",row[1])
                            print("Salary of employee : ",row[2])

                            found = 1
                            break
                
                if found == 0:
                    print("-------------------------------------")
                    print("Employee Not Found !!!")
            
                        
                ans = input("Want to serach more ? (y/n): ")

    elif a == 3 :
        break
    else:
        print("Invalid Input !")
        break
