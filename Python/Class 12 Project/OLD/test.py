# Python Project
# Program to manage medical shop using SQL, File

print("-----Medical Shop Management System------\n---------USAVN Medical Shop---------\n")

#----------------------------------------------------------------Imported Required Modules--------------------------------------------------#

import time
from datetime import *
import csv
import os
import mysql.connector as sqltor # Connecting to Database

#----------------------------------------------------------------Database Connection--------------------------------------------------#

mycon = sqltor.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21') # Name of database is CS2020_21
cursor = mycon.cursor() # Creating Cursor

cursor.execute("CREATE TABLE IF NOT EXISTS Medical_Shop(Code INT PRIMARY KEY, Name_Of_Med VARCHAR(40), Name_Of_Manu VARCHAR(40), Batch_No VARCHAR(15), Manu_Date Date, Exp_Date Date, Quantity INT(4), Price_Per10 FLOAT(5,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS Bill(Billno INT(5) PRIMARY KEY,Patient_Name VARCHAR(40),Date Date)")

#--------------------------------------------------Fetching Current date and time from database--------------------------------------------------#

cursor.execute("select NOW()")      # getting current date with the help of my sql database
t = cursor.fetchone()
for row in t :
    Time = row
    #print("Time :", Time)

cursor.execute("select CURDATE()")      # getting current date with the help of my sql database
d = cursor.fetchone()
for row in d :
    Date = row
    print("Date :", Date)

    '''
    We can also use
    print(date.today())
    '''
    
#-----------------------------------function to reduce quantity of stock whenever a medicine is purchased-------------------------------------------#
def reduce():
    cursor = mycon.cursor()  # creating cursor object

    quant = stockquant - quan 

    queryup = 'update medical_shop set Quantity = {} where Code = {}'.format(quant, code) # Updating the quantity
    cursor.execute(queryup)
    mycon.commit()

#-----------------------------------------------------------------------Main Code------------------------------------------------------------#
    #----------------------------------------------------------------main menu--------------------------------------------------#
    
answer1 = 'y'
while answer1.lower() == 'y' :
     
    print("\n---------------------------------------------------------------------------------")
    print("1. Update\View Stock On Database. \n2. Print Invoice/Bill for a Purchase.(Create a file) \n3. Exit. ") # Choice
    ch = int(input("What do you want to do ? (1/2/3) : "))

    if not ch.get():
        print("Please enter a Valid Value") 
    
    elif ch.get().isalpha():
        print("Please enter a Valid Integer Value")
#----------------------------------------------------------------Adding Medicine To Database--------------------------------------------------#
    if ch == 1 :
        
        if mycon.is_connected():
            print('Successfully Connected to MySQL Databases \n')

        print("--------------------------------------------------")
        cursor = mycon.cursor() # creating cursor object
            
        print("-----Medicine Database------\n\n")

        answer = 'y'
        while answer.lower() == 'y' :
            print("1. Add Medicine \n2. Remove Medicine \n3. Update Medicine Information \n4. List Of Medicine \n5. Main Menu")
            ch1 = int(input("What do you want to do ? (1/2/3/4/5) : "))

            if ch1 == 1 :  # Adding Medicine to stock
                ans = 'y'
                while ans.lower() == 'y':
                    print()	
                    print("------Adding Medicine to Stock------\n")
                      
                    code = int(input("Enter Code : "))
                    queryup = 'select * from medical_shop where Code = {}'.format(code)
                    cursor.execute(queryup)
                    result = cursor.fetchall()

                    if cursor.rowcount == 0 : # Checking for duplicate entry
                        
                        nmed = input("Enter Name of Medicine : ")
                        nmanu = input("Enter Name of Manufacturer : ")
                        batch = input("Enter Batch No. : ")
                        mandate = input("Enter Date of Manufacturing (YYYY-MM-DD) : ")
                        expdate = input("Enter Date of Expiry (YYYY-MM-DD) : ")

                        a = date.fromisoformat(mandate)
                        #print(a)
                        b = date.fromisoformat(expdate)
                        #print(b)

                        if a < b :
                            pass
                        else:
                            print('Invalid Input ! \nDate Expiry Date shoud be after Manufacturing date ')
                            break
    
                        quan = int(input("Enter Quantity : "))
                        price = float(input("Enter Price Per 10 Tablets / 10 units : "))
        
                        query = 'insert into medical_shop values({}, "{}", "{}", "{}", "{}", "{}", {}, {})'.format(code, nmed, nmanu, batch, mandate, expdate, quan, price)
                        cursor.execute(query)
                        mycon.commit()
                         
                        print('Data Saved Successfully')
                        
                        ans = input('Want to add more ?(y/n): ')

                    else:
                         
                        print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%15s'%'Batch No.', '%25s'%'Date of Manufacturer', '%15s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                        for row in result:
                            print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%13s'%row[3], '%18s'%row[4], '%20s'%row[5], '%20s'%row[6], '%21s'%row[7])
                        print("Medicine with code", code, "Already Present !!!\n") 
                        break

#----------------------------------------------------------------Deleting Medicine from Database--------------------------------------------------#
                    
            elif ch1 == 2 :  
                ans = 'y'
                while ans.lower() == 'y':
                    print("------Deleting Medicine from Stock------\n")
                    nmed = input("Enter name of medicine to be Deleted: ")
                    query = 'select * from medical_shop where Name_of_Med = "{}"'.format(nmed)
                    cursor.execute(query)
                    result = cursor.fetchall()

                    if cursor.rowcount == 0 :
                        tim.sleep(0.5)
                        print("Sorry! medicine with ", nmed, "not found")

                    else:
                        print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%15s'%'Batch No.', '%25s'%'Date of Manufacturer', '%15s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                        for row in result:
                            print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%13s'%row[3], '%18s'%row[4], '%20s'%row[5], '%20s'%row[6], '%21s'%row[7])
                            code = row[0]
                            su = input("\n\nWant to delete Sure(y/n): ")
                            
                            if su.lower() == 'y':
                                queryde = 'delete from medical_shop where code = {}'.format(code)
                                cursor.execute(queryde)
                                mycon.commit()
                                 
                                print('Record Deleted Successfully')
                                 
                    ans = input('Want to delete more ?(y/n): ')

#----------------------------------------------------------------Updating Medicine of previously entered Database--------------------------------------------------#

            elif ch1 == 3 :   # Updating Medicine Information
                print("------Updating Info of Medicine of Stock------\n")
                ans = 'y'
                while ans.lower() == 'y':
                    nmed = input("Enter name of medicine to be updated: ")
                    queryup = 'select * from medical_shop where Name_of_Med = "{}"'.format(nmed)
                    cursor.execute(queryup)
                    result = cursor.fetchall()

                    if cursor.rowcount == 0 :
                         
                        print("Sorry! medicine ", nmed, "not found\n")

                    else:
                        print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%15s'%'Batch No.', '%25s'%'Date of Manufacturer', '%15s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                        for row in result:
                            code = row[0]
                            print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%13s'%row[3], '%18s'%row[4], '%20s'%row[5], '%20s'%row[6], '%21s'%row[7])
                            choice = input("Sure to Update(y/n) : ") 

                            if choice.lower() == 'y':
                                print("---You can update only Batch No., Date of manufacturing and expiry, Quantity and Price---")

                
                                bno = input("Enter new batch No. (leave blank if you don't want to change it): ")
                                if bno == '':
                                    bno = row[3]
                                    
                                Dman = input("Enter new Date of Manufacturing (leave blank if you don't want to change it): ")
                                if Dman == '':
                                    Dman = row[4]

                                Dexp = input("Enter new Date of Expiry (leave blank if you don't want to change it): ")
                                if Dexp == '':
                                    Dexp = row[5]
                
                                qua = input("Enter new Quantity(leave blank if you don'twant to change it): ")
                                if qua == '':
                                    qua0 = row[6]
                                    qua = int(qua0)

                                pri = input("Enter new Price (leave blank if you don't want to change it): ")
                                if pri == '':
                                    pri0 = row[7]
                                    pri = int(pri0)
                    
                                queryup = 'update medical_shop set Batch_No = "{}", Manu_Date = "{}", Exp_Date = "{}", Quantity = {}, Price_Per10 = {} where code = {}'.format(bno, Dman, Dexp, qua, pri, code)
                                cursor.execute(queryup)
                                mycon.commit()
                                 
                                print("Record updated succesfully\n")
                                
                    ans = input('Want to update more ?(y/n): ')

#----------------------------------------------------------------Getting Medicine(List) Details from Database--------------------------------------------------#
                    
            elif ch1 == 4 :
                print("------ Medicines in Stock------\n")
                query = 'select * from medical_shop'
                cursor.execute(query)
                result = cursor.fetchall()
                print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%15s'%'Batch No.', '%25s'%'Date of Manufacturer', '%15s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                for row in result:
                    print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%13s'%row[3], '%18s'%row[4], '%20s'%row[5], '%20s'%row[6], '%21s'%row[7])

#----------------------------------------------------------------If User want to go to main menu--------------------------------------------------#
                    
            elif ch1 == 5 :
                break

#----------------------------------------------------------------In case invalid input is given--------------------------------------------------#            
            else :
                 
                print("Invalid Input ! ")
            
#----------------------------------------------------------------Shows option to choose menu and sub menu--------------------------------------------------#
                
            print("------------------------------------------------------------\n")
            answer = input("For Database Menu Press y and Press Enter(return) for Main Menu : ")
            

#----------------------------------------------------------------Print Invoice--------------------------------------------------#
            
    elif ch == 2 :

        print("Time :", Time)
        
#----------------------------------------------------------------Getting Bill no. from database--------------------------------------------------#

        query2 = 'select * from bill'
        cursor.execute(query2)
        result2 = cursor.fetchall()
        if result2 == [] :
            billno = 0
        else:
            for row in result2 :
                billno = row[0]
#----------------------------------------------------------------Invoice Interface--------------------------------------------------#
                
        print("\n---------------------------------USAVN Medical Shop Tumsar--------------------------------------\n")
        billno = billno + 1 #int(input("Bill No. : "))
        print("Bill No.",billno)
        
        print("Date & Time :", Time)
        pname = input("Name of patient : ") # Patient name

        query1 = 'select * from bill where Billno = {}'.format(billno)
        cursor.execute(query1)
        result1 = cursor.fetchall()        

#----------------------------------------------------------------inserting current billno. to database--------------------------------------------------#
        
        if result1 == [] :
        
            query0 = 'insert into bill values({}, "{}", "{}")'.format(billno, pname, Date) # saving Bill No to database
            cursor.execute(query0)
            mycon.commit()
        
#----------------------------------------------------------------getting details about patient--------------------------------------------------#
            
            rdoc = input("Refered by Doctor : ")
            add = input("Address of Patient : ")
            n = int(input("Number of Medicines : ")) # getting the number of medicines prescibed by doctor
            fname = (pname+ str(billno)+".csv")

#----------------------------------------------------Creating and opening a csv file using patient name and billno.--------------------------------------------------#        
            with open(fname, mode = 'w', newline = '\n') as csvfile :
                
                date0 = Date.strftime("%A, %d %B %Y")
                time0 = str(Time)
                time1 = time0[11:19]
                #print(time1)
                
                filewriter = csv.writer(csvfile,delimiter = ',')

#----------------------------------------------------------------Writing data onto csv file-------------------------------------------------------------#
                
                filewriter.writerow(["------------------------------------------------------USAVN Medical Shop Tumsar---------------------------------------------------"])
                filewriter.writerow(["Bill No. : "+ str(billno),'','','','','','','', str(date0)])
                filewriter.writerow(["Patient's Name : " + pname ,'','','','','','','', 'Issue Time :' + str(time1)])
                filewriter.writerow(["Address : " + add ])
                filewriter.writerow(["Refered by Doctor : " + rdoc ])
                filewriter.writerow([])
                filewriter.writerow(["Sr.No.", "Name of Medicine",'', " Manufacturing.Co.",'', "Batch No.", "Man.Date", "Exp.Date", "Quantity", "Price", "Amount"])

                b = c =0
                total = amt = 0
                ans = 'y'
                for i in range(n):
                    print("\nSr. No.", i+1)
                    
                    nmed0 = input("Enter name of medicine : ")   # Using the name of medicine  the  other details will be obtained from the database
                    nmed = nmed0.capitalize()
                    query1 = 'select * from medical_shop where Name_of_Med = "{}"'.format(nmed)
                    cursor.execute(query1)
                    result = cursor.fetchall()
                    for row in result:
                        if row[6] <= 50 :
                            print(row[1], 'is getting out of stock\n')
                        else:
                            pass

                    if result == []:
                        print("Sorry! medicine with name ", nmed, "not found\n")
                        b = 1
                        c = 0
                        csvfile.close()
                        break
                        
                    for row in result:      # Checking the existence of a medicine
                        if cursor.rowcount != 0 :   
                            quan = int(input("Quantity : " ))
                            code = row[0]       # Getting details according to name of medicine
                            nmanu = row[2]      # Fetching data from database
                            batchn = row[3]
                            
                            mandate0 = str(row[4])
                            mandate = mandate0[0:7]
                            
                            expdate0 = str(row[5])
                            expdate = expdate0[0:7]
                            
                            #print(mandate, expdate)
                            stockquant = row[6]
                            price = row[7]

                            #print(price)
                            oneprice = price / 10  # Calculating the amount of each tablet
                            amt = quan * oneprice  # Calculating the amount of One medicine
                    
                            text = [str(i+1), nmed,'', nmanu,'', str(batchn), str(mandate), str(expdate), str(quan), str(price), str(amt)]
                            filewriter.writerow(text)
                
                        print()
                        total = total + amt   # Total Amount
                        reduce()    # Calling reduce function to reduce the purchased medicine from database
                        c = 1
            
                if c == 1:
                    filewriter.writerow([])
                    filewriter.writerow(["Total Amount: " + str(total)])
                    filewriter.writerow(["Inclusive of all taxes. "])
                    csvfile.close()

                    
                    print("\nInvoice Printed Successfully ")
                    print("_____________________________________ \n")

#----------------------------------------------------------------incase medicine not found----------------------------------------------------------------#
                if b == 1:
                    os.remove(fname)
                    
                    print("Invoice Printing Failed ! ")
                    print("_____________________________________ ")

                    queryde = 'delete from bill where billno = {}'.format(billno)
                    cursor.execute(queryde)
                    mycon.commit()
        else :
             
            print("Bill no.",billno, "present already\n")
            print('%10s'%'Bill No.', '%20s'%'Name of Patient', '%25s'%'Date',)
            for row in result1 :
                print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2])
            print()

#----------------------------------------------------------------Closing connection with database when user quits--------------------------------------------------#        
    elif ch == 3 :
        break
        mycon.close() # closing connection with database

    else :
        print("Invalid Input")








        







                
                    

    

            
   
