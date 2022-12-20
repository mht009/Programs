import csv
import os
import mysql.connector as sqltor # Connecting to Database


mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'CS2020_21')

cursor = mycon.cursor() # Getting data from database as per medicine name

csv.field_size_limit(20)
print("\n--------------------USAVN Medical Shop Tumsar-----------------------\n")
billno = int(input("Bill No. : "))
date = input("Date :  ")
pname = input("Name of patient : ")
rdoc = input("Refered by Doctor : ")
n = int(input("Number of Medicines : ")) # getting the number of medicines prescibed by doctor
fname = (pname+ str(billno)+".csv")
        
with open(fname, mode = 'w', newline = '\n') as csvfile :
    filewriter = csv.writer(csvfile,delimiter = ',')
    
    filewriter.writerow(["-----------------------------------------------------------USAVN Medical Shop Tumsar---------------------------------------------------------------"])
    filewriter.writerow(["Bill No. : "+ str(billno) , "  ", "Date : " + str(date)])
    filewriter.writerow(["Patient's Name : " + pname ])
    filewriter.writerow(["Refered by Doctor : " + rdoc ])
    filewriter.writerow([])
    filewriter.writerow(["Sr.No.", "Name of Medicine",'', "         Mfg.Co.",'','', "Batch No.", "  Manu.Date",'', "Exp.Date", "Quantity", "Price", "Amount"])

    b = 0
    total = amt = 0
    ans = 'y'
    for i in range(n):
        print("\nSr. No.", i+1)
        nmed = input("Enter name of medicine : ")   # Using the name of medicine  the  other details will be obtained from the database

        query1 = 'select * from medical_shop where Name_of_Med = "{}"'.format(nmed)
        cursor.execute(query1)
        result = cursor.fetchall()

        if result == []:
                print("Sorry! medicine with name ", nmed, "not found\n")
                b = 1
                c = 0
                csvfile.close()
                break
            
            
        for row in result:      # Checking the existence of a medicine
            if cursor.rowcount == 0 :   
                print("\nSorry! medicine with name ", nmed, "not found\n")
                
            else:
                quan = int(input("Quantity : " ))
                code = row[0]       # Getting details according to name of medicine
                nmanu = row[2]
                batchn = row[3]
                mandate = row[4]
                expdate = row[5]
                stockquant = row[6]
                price = row[7]

                #print(price)
                oneprice = price / 10  # Calculating the amount of each tablet
                amt = quan * oneprice  # Calculating the amount of One medicine
                    
                text = [n, nmed,'', nmanu,'','', str(batchn), '   '+str(mandate),'', str(expdate), quan, price, amt]
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
        
        print("Invoice Printed Successfully ")

    if b == 1:
        os.remove(fname)
        print("Invoice Printing Failed ! ")
