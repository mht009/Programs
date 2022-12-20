import mysql.connector as sqltor
mycon = sqltor.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21')
if mycon.is_connected():
    print('Successfully Connected to MySQL Databases')

cursor = mycon.cursor()
print('*' * 60)
print("Update info of employees")
print("\n\n")

ans = 'y'
while ans.lower() == 'y':
    eno = int(input("Enter Employee Number to be updated: "))
    query = 'select * from Employee where Employee_No = {}'.format(eno)
    cursor.execute(query)
    result = cursor.fetchall()

    if cursor.rowcount == 0 :
        print("Sorry! Employee with ", eno, "not found")


    else:
        print('%10s'%'Employee No.', '%20s'%'Name of Employee', '%15s'%'Department', '%10s'%'Salary')
        for row in result:
            print('%10s'%row[0], '%20s'%row[1], '%15s'%row[2], '%10s'%row[3])
            choice = input("Sure to Update(y/n) : ") 
            if choice.lower() == 'y':
                print("---You can update only Department and Salary---")

                
                Dpt = input("Enter new Department(leave blank if you don'twant to change it): ")
                if Dpt == '':
                    Dpt = row[2]

                
                Sal = input("Enter new Salary(leave blank if you don'twant to change it): ")
                if Sal == '':
                    Sal = row[3]

                queryup = 'update employee set Department = "{}", Salary = {} where Employee_No = {}'.format(Dpt, Sal, eno)
                cursor.execute(queryup)
                mycon.commit()
                print("Record updated succesfully")
                    

    ans = input('Want to update more ?(y/n): ')
    
                
