''' Program to connect with database and delete employee number in table Employee and display the record'''

import mysql.connector as sqltor
mycon = sqltor.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21')
if mycon.is_connected():
    print('Successfully Connected to MySQL Databases')

cursor = mycon.cursor()
print('*' * 60)
print("\n\n")

ans = 'y'
while ans.lower() == 'y':
    eno = int(input("Enter Employee Number to be Deleted: "))
    query = 'select * from Employee where Employee_No = {}'.format(eno)
    cursor.execute(query)
    result = cursor.fetchall()

    if cursor.rowcount == 0 :
        print("Sorry! Employee with ", eno, "not found")


    else:
        print('%10s'%'Employee No.', '%20s'%'Name of Employee', '%15s'%'Department', '%10s'%'Salary')
        for row in result:
            print('%10s'%row[0], '%20s'%row[1], '%15s'%row[2], '%10s'%row[3])
            ch = input("\n\nWant to delete Sure(y/n): ")
            if ch.lower() == 'y':
                queryde = 'delete from employee where Employee_No = {}'.format(eno)
                cursor.execute(queryde)
                mycon.commit()
                print('Record Deleted Successfully')


    ans = input('Want to delete more ?(y/n): ')
                
