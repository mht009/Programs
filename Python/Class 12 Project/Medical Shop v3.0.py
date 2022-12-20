# Medical Shop Managment system v3.0
# importing required modules
import csv
from logging import raiseExceptions
import os 
import mysql.connector as sqltor
from datetime import datetime, date, time


# Connecting to database & creating cursor 
mycon = sqltor.connect(host = '127.0.0.1', user = "root", passwd = "root")
cursor = mycon.cursor()

if mycon.is_connected():
    print('Connection to Database Successful')

cursor.execute('CREATE DATABASE IF NOT EXISTS MedicalShop_v3')
cursor.execute('USE MedicalShop_v3')
cursor.execute('CREATE TABLE IF NOT EXISTS Medicines(Code INT PRIMARY KEY, Name_of_Med VARCHAR(40), Name_of_Man VARCHAR(40), Batch_No VARCHAR(15), Man_Date DATE,\
     Exp_Date DATE, Quantity INT(5), PricePer10 FLOAT(6,2))')

'''
cursor.execute('SHow tables')
for i in cursor:
    print(i)
'''

# retrieving current date
Date = date.today()

# retrieving current time from mysql database
cursor.execute("SELECT NOW()")
t = cursor.fetchone()
for row in t:
    global Time
    Time = row

print(Time)


# Creating definations 
# Adding Medicine to database
def add_med():
    try:
        code = int(input("Enter Code : "))
        querys1 = 'SELECT * FROM Medicines where code = {}'.format(code)
        cursor.execute(querys1)
        result1 = cursor.fetchall()

        if cursor.rowcount == 0:

            querya = 'insert into Medicines values({}, "{}", "{}", "{}", "{}", "{}", {}, {})'.format(code, name_med(), name_manu(),\
                 batch_med(), mandate_med(), expdate_med(), quan_med(), price_med())
            cursor.execute(querya)
            mycon.commit()
            print('Data saved successfully')

            querys2 = 'SELECT * FROM Medicines'
            cursor.execute(querys2)
            result2 = cursor.fetchall()

            print("****************************************************************************************\n")
            
            print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
            for row in result2:
                print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                    '%10s'%row[6], '%12s'%row[7])
            print("****************************************************************************************\n")
            
        else:
            print("****************************************************************************************\n")
            print('Medicine with code ',code,' already present!')
            print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
            for row in result1:
                print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                    '%10s'%row[6], '%12s'%row[7])
            print("****************************************************************************************\n")
            

    except:
        print('Error')
        add_med()

def name_med():
    try:
        nmed = input("Enter Name of Medicine : ").capitalize()
        return nmed
    except:
        name_med()
    
def name_manu():
    try:
        nmanu = input("Enter Name of Manufacturer : ").capitalize()
        return nmanu
    except:
        name_manu()

def batch_med():
    try:
        batch = input("Enter Batch No. : ")
        return batch
    except:
        batch_med()

def mandate_med():
    try:
        global mandate
        mandate0 = input("Enter Date of Manufacturing (MM-YY) : ")
        mandate = '20' + mandate0[3:5] + '-' + mandate0[0:2] + '-01'
        
        a = date.fromisoformat(mandate)
        b = date.today()
        
        if a < b :
            print(str(mandate))
            return mandate
        else:
            print("Invalid Input! \n Enter valid date of manufacturing ")
            mandate_med()
    except:        
        mandate_med()

def expdate_med():
    try:
        
        expdate0 = input("Enter Date of Expiry (MM-YY) : ")
        expdate = '20' + expdate0[3:5] + '-' + expdate0[0:2] + '-01'

        a = date.fromisoformat(mandate)
        b = date.fromisoformat(expdate)
        if a < b :
            return expdate
        else:
            print("Invalid Input! \n Date of Expiry date should be after Manufacturing date ")
            expdate_med()
    except:
        expdate_med()
    
def quan_med():
    try:
        quan = int(input("Enter Quantity : "))
        return quan
    except:
        print("Invalid Input!")
        quan_med()

    

def price_med():
    try:
        price = float(input("Enter Price per 10 Tablets/ 10 Units : "))
        return price
    except:
        price_med()

# Removing Medicines From Database
def rem_med():
    try:
        nmed = input("Enter Name of Medicine : ").capitalize()
        queryr1 = 'SELECT * FROM Medicines where Name_of_Med LIKE "{}"'.format(nmed + "%")
        cursor.execute(queryr1)
        resultr1 = cursor.fetchall()
        
        if cursor.rowcount == 0:
            print("Medicine with name ", nmed, "not found.")
            
        else:
            print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
            for row in resultr1:
                print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                    '%10s'%row[6], '%12s'%row[7])
                nmed = row[1]
            print("****************************************************************************************\n")
        
            con = None
            con = input("Sure, Want to delete it. (y/n) : ").lower()
            if con == 'y':
                queryr2 = 'DELETE FROM Medicines WHERE Name_of_Med = "{}"'.format(nmed)
                cursor.execute(queryr2)
                mycon.commit()
                print("Successfully deleted the record.")
                print("****************************************************************************************\n")
            else:
                print('Deletion Cancelled')   

            de = input("Do you want to delete another record (y/n) : ").lower()         
            if de == 'y':
                rem_med()
            else:
                print("****************************************************************************************\n")
    
    except:
        print("Error!")
        rem_med()

# Updating Medicine Information
def up_med():
    try:
        nmed = input("Enter Name of Medicine : ").capitalize()
        queryu1 = 'SELECT * FROM Medicines where Name_of_Med LIKE "{}"'.format(nmed + "%")
        cursor.execute(queryu1)
        resultu1 = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Medicine not found!!!")
            n = input("Do you want to add Medicine (y/n) : ").lower()
            if n == 'y':
                add_med()
            else:
                print("Okay")
        else:
            print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
            for row in resultu1:
                print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                '%10s'%row[6], '%12s'%row[7])
                nmed = row[1]
            print("****************************************************************************************\n")
        
            con = None
            con = input("Sure, Want to update it. (y/n) : ").lower()
            if con == 'y':

                print("---You can update only Batch No., Date of manufacturing and expiry, Quantity and Price---")

                
                bno = input("Enter new batch No. (leave blank if you don't want to change it): ")
                if bno == '':
                    bno = row[3]
                                    
                Dman = input("Enter new Date of Manufacturing (leave blank if you don't want to change it)  (MM-YY) : ")
                if Dman == '':
                    Dman = row[4]               
                else:
                    Dman ='20' + Dman[3:5] + '-' + Dman[0:2] + '-01'

                Dexp = input("Enter new Date of Expiry (leave blank if you don't want to change it)  (MM-YY) : ")
                if Dexp == '':
                    Dexp = row[5]
                else:
                    Dexp ='20' + Dexp[3:5] + '-' + Dexp[0:2] + '-01'
                
                qua = input("Enter new Quantity(leave blank if you don't want to change it): ")
                if qua == '':
                    qua0 = row[6]
                    qua = int(qua0)

                pri0 = input("Enter new Price (leave blank if you don't want to change it): ")
                if pri0 == '':
                    pri = row[7]
                    pri = float(pri0)

                queryu2 = 'UPDATE Medicines SET Batch_No = "{}", Man_Date = "{}", Exp_Date = "{}", Quantity = {},\
                     PricePer10 = {} where Name_of_Med = "{}"'.format(bno, Dman, Dexp, qua, pri, nmed)
                cursor.execute(queryu2)
                mycon.commit()
                print("Successfully updated the record.")
                print("****************************************************************************************\n")
            else:
                print('Updation Cancelled')   

            upd = input("Do you want to update another record (y/n) : ").lower()         
            if upd == 'y':
                up_med()
            else:
                print("****************************************************************************************\n")
    
    except:
        print("Error!")
        up_med()

#Listing names of medicnes
def list_med():
    querylm1 = 'SELECT * FROM Medicines ORDER BY Name_of_Med'
    cursor.execute(querylm1)
    resultlm1 = cursor.fetchall()

    if cursor.rowcount == 0:
        print("Medicine list empty!!!")
        n = input("Do you want to add Medicine (y/n) : ").lower()
        if n == 'y':
            add_med()
        else:
            print("Okay")
    else:
            print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
            for row in resultlm1:
                print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                '%10s'%row[6], '%12s'%row[7])
            print("****************************************************************************************\n")

# Searching Medicines
def sea_med():
    nmed = input("Enter Name of Medicine : ").capitalize()
    queryse1 = 'SELECT * FROM Medicines where Name_of_Med LIKE "{}"'.format(nmed + "%")        
    cursor.execute(queryse1)
    resultse1 = cursor.fetchall()
    
    if cursor.rowcount == 0:
        print("Medicine with name ", nmed, "not found.")
        
    else:
        print('%0s'%'Code', '%25s'%'Name of Medicine', '%25s'%'Name of Manu', '%10s'%'Batch No.', '%12s'%'Manufac Date', '%12s'%'Expiry Date',\
                    '%10s'%'Quantity', '%12s'%'Price/10 units')
        for row in resultse1:
            print('%0s'%row[0], '%25s'%row[1], '%25s'%row[2], '%10s'%row[3], '%12s'%row[4], '%12s'%row[5],\
                    '%10s'%row[6], '%12s'%row[7])
              
            print("****************************************************************************************\n")

# main
while True:
    print('1. Update/ View stock on Database.\n2. Print Invoice/Bill for a purchase.\n3. Exit')
    print("****************************************************************************************\n")

    ch = int(input('Enter your choice (1/2/3) : '))
    if ch == 1 :
        while True:
            print('0. Exit to Main Menu\n1. Add Medicines\n2. Remove Medicines\n3. Update Medcine Information\n4. List of Medicine\n5. Search a Medicine')
            print("****************************************************************************************\n")

            ch1 = int(input('Enter Your Choice (0/1/2/3/4/5) : '))

            if ch1 == 1:
                print('Adding Medicine to Database...')
                add_med()

            elif ch1 == 2:
                print('Removing Medicines from Database...')
                rem_med()

            elif ch1 == 3:
                print("Updating Medicine Info...")
                up_med()

            elif ch1 == 4:
                print('List of Medicines...')
                list_med()

            elif ch1 == 5:
                print('Search Medicines...')
                sea_med()

            elif ch1 == 0 :
                print("****************************************************************************************\n")
                break

            else:
                print('Invalid Input!!!')
                print("****************************************************************************************\n")
