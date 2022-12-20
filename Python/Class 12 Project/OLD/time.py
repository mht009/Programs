import mysql.connector as sqltor # Connecting to Database

mycon = sqltor.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21') # Name of database is CS2020_21
cursor = mycon.cursor() # Creating Cursor

cursor.execute("select NOW()")      # getting current date with the help of my sql database
t = cursor.fetchone()
for row in t :
    Time = row
    print("Time :", Time)
    
time0 = str(Time)
time1 = time0[11:19]
print(time1)
