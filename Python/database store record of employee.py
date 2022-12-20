# Peogram to connect with database and store record of employee and display record
import mysql.connector as sqltor
mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'CS2020_21')
if mycon.is_connected():
    print('Successfully Connected to MySQL Databases')

cursor = mycon.cursor()
cursor.execute('CREATE TABLE Employee(Employee_No INT(3) PRIMARY KEY, Name VARCHAR(10), Department VARCHAR(15), Salary INT(7));')
mycon.commit()

choice = None
while choice != 0:
    print('1 Add Record')
    print('2 Display Record')
    print('0 Exit')
    choice = int(input("Enter Choice :"))

    if choice == 1:
        eno = int(input("Enter Employee Number : "))
        name = input("Enter Name of Employee : ")
        dept = input("Enter Department : ")
        sal = int(input("Enter Salary: "))

        query = 'insert into Employee values({}, "{}", "{}", {})'.format(eno, name, dept, sal)
        cursor.execute(query)
        mycon.commit()
        print('Data Saved Successfully')

    elif choice == 2 :
        query = 'select * from Employee'
        cursor.execute(query)
        result = cursor.fetchall()
        print('%10s'%'Employee No.', '%20s'%'Name of Employee', '%15s'%'Department', '%10s'%'Salary')
        for row in result:
            print('%10s'%row[0], '%20s'%row[1], '%15s'%row[2], '%10s'%row[3])
            
        
    elif choice == 0:
        mycon.close()
        print("Thank you!")

    else:
        print("Invalid Choice ")
