''' Program to create CSV file and store empno, name, salary, and seach any
empno and display name, salary and if not found shows appropriate message'''

import csv
with open('Emplfile.csv', mode = 'w') as csvfile :
    filewriter = csv.writer(csvfile,delimiter = ',')
    ans = "y"
    while ans.lower() == "y" :
        empno = int(input("Enter Employee Number : "))
        name = input("Enter Name : ")
        salary = float(input("Enter salary of the Employee : "))
        filewriter.writerow([empno, name, salary])
        print("Data saved. ")
        ans = input("Want to add more ? (y/n) :")

ans = "y"
with open('Emplfile.csv', mode = "r") as csvfile :
    filereader = csv.reader(csvfile, delimiter =',')
    while ans == "y" :
        found = False
        enum = input("Enter Employee Number To Be Search : ")
        for row in filereader :
            if len(row) != 0 :
                if row[0] == enum :

                    print("-----------------------------------")
                    print("Name of employee : ",row[1])
                    print("Salary of employee : ",row[2])

                    found = True
                    break

        if found == False:
                    print("-------------------------------------")
                    print("Employee Not Found !!!")
                    
        ans = input("Want to serach more ? (y/n): ")
