# Python Project
# Program to manage medical shop using SQL, File

# Defining a function to reduce quantity of stock whenever a medicine is purchased
def reduce():
    import mysql.connector as sqltor  # connecting to Database
    mycon = sqltor.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21') # Name of database is CS2020_21
    cursor = mycon.cursor()  # creating cursor object

    quant = stockquant - quan 

    queryup = 'update medical_shop set Quantity = {} where Code = {}'.format(quant, code) # Updating the quantity
    cursor.execute(queryup)
    mycon.commit()
    mycon.close() # closing connection with database

answer1 = 'y'
while answer1.lower() == 'y' :
    print("1. Update Stock On Database. \n2. Print Invoice/Bill for a Purchase.(Create a file) \n3. Exit. ") # Choice
    ch = int(input("What do you want to do ? (1/2/3) : "))

    if ch == 1 :
        import mysql.connector as sqltor # connecting to Database
        mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'CS2020_21')  # Name of database is CS2020_21
        if mycon.is_connected():
            print('Successfully Connected to MySQL Databases \n')

        print("--------------------------------------------------")
        cursor = mycon.cursor() # creating cursor object
            
        print("-----Medicine Database------\n\n")

        answer = 'y'
        while answer.lower() == 'y' :
            print("1. Add Medicine \n2. Remove Medicine \n3. Update Medicine Information \n4. List Of Medicine \n5. Main Menu")
            ch1 = int(input("What do you want to do ? (1/2/3/4/5) : "))

            if ch1 == 1 :
                print("------Adding Medicine to Stock------\n")
                      
                code = int(input("Enter Code : "))
                nmed = input("Enter Name of Medicine : ")
                nmanu = input("Enter Name of Manufacturer : ")
                mandate = input("Enter Date of Manufacturing (YYYY-MM-DD) : ")
                expdate = input("Enter Date of Expiry (YYYY-MM-DD) : ")
                quan = int(input("Enter Quantity : "))
                price = float(input("Enter Price Per 10 Tablets : "))
        
                query = 'insert into medical_shop values({}, "{}", "{}", "{}", "{}", {}, {})'.format(code, nmed, nmanu, mandate, expdate, quan, price)
                cursor.execute(query)
                mycon.commit()
                print('Data Saved Successfully')

            elif ch1 == 2 :
                ans = 'y'
                while ans.lower() == 'y':
                    print("------Deleting Medicine from Stock------\n")
                    code = int(input("Enter code of medicine to be Deleted: "))
                    query = 'select * from medical_shop where code = {}'.format(code)
                    cursor.execute(query)
                    result = cursor.fetchall()

                    if cursor.rowcount == 0 :
                        print("Sorry! medicine with code ", code, "not found")


                    else:
                        print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%30s'%'Date of Manufacturer', '%20s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                        for row in result:
                            print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%23s'%row[3], '%25s'%row[4], '%20s'%row[5], '%20s'%row[6])
                            su = input("\n\nWant to delete Sure(y/n): ")
                            if su.lower() == 'y':
                                queryde = 'delete from medical_shop where code = {}'.format(code)
                                cursor.execute(queryde)
                                mycon.commit()
                                print('Record Deleted Successfully')

                    ans = input('Want to delete more ?(y/n): ')

            elif ch1 == 3 :
                print("------Updating Info of Medicine of Stock------\n")
                ans = 'y'
                while ans.lower() == 'y':
                    code = int(input("Enter code of medicine to be updated: "))
                    queryup = 'select * from medical_shop where code = {}'.format(code)
                    cursor.execute(queryup)
                    result = cursor.fetchall()

                    if cursor.rowcount == 0 :
                        print("Sorry! medicine with code ", code, "not found")


                    else:
                        print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%30s'%'Date of Manufacturer', '%20s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                        for row in result:
                            print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%23s'%row[3], '%25s'%row[4], '%20s'%row[5], '%20s'%row[6])
                            choice = input("Sure to Update(y/n) : ") 

                            if choice.lower() == 'y':
                                print("---You can update only Date of manufacturing and expiry, Quantity and Price---")

                
                                Dman = input("Enter new Date of Manufacturing (leave blank if you don't want to change it): ")
                                if Dman == '':
                                    Dman = row[3]

                                Dexp = input("Enter new Date of Expiry (leave blank if you don't want to change it): ")
                                if Dexp == '':
                                    Dexp = row[4]
                
                                qua = int(input("Enter new Quantity(leave blank if you don'twant to change it): "))
                                if qua == '':
                                    qua = row[5]

                                pri = input("Enter new Price (leave blank if you don't want to change it): ")
                                if pri == '':
                                    pri = row[6]
                    
                                queryup = 'update medical_shop set Manu_Date = "{}", Exp_Date = "{}", Quantity = {}, Price_Per10 = {} where code = {}'.format(Dman, Dexp, qua, pri, code)
                                cursor.execute(queryup)
                                mycon.commit()
                                print("Record updated succesfully")      

                    ans = input('Want to update more ?(y/n): ')
    
            elif ch1 == 4 :
                print("------ Medicines in Stock------\n")
                query = 'select * from medical_shop'
                cursor.execute(query)
                result = cursor.fetchall()
                print('%10s'%'Code', '%20s'%'Name of Medicine', '%25s'%'Name of Manufacturer', '%30s'%'Date of Manufacturer', '%20s'%'Date of Expiry', '%20s'%'Quantity', '%18s'%'Price')
                for row in result:
                    print('%10s'%row[0], '%20s'%row[1], '%25s'%row[2], '%23s'%row[3], '%25s'%row[4], '%20s'%row[5], '%20s'%row[6])

            elif ch1 == 5 :
                break
            
            else :
                print("Invalid Input ! ")
            
            print("------------------------------------------------------------\n")
            answer = input("For Database Menu Press y and n for Main Menu : ")
            
    
    elif ch == 2 :
        import mysql.connector as sqltor # Connecting to Database
        mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'CS2020_21')

        cursor = mycon.cursor() # Getting data from database as per medicine name

        print("\n---------USAVN Medical Shop Tumsar----------\n")
        billno = int(input("Bill No. : "))
        pname = input("Name of patient : ")
        rdoc = input("Refered by Doctor : ")
        n = int(input("Number of Medicines : ")) # getting the number of medicines prescibed by doctor
        print()

        # Creating File For Bill
        fname = (pname+ str(billno)+".txt") # The name of file will be the concatnation of patient's name and bill no as this will create a unique name
        filehan = open(fname,"w")
        filehan.write("---------USAVN Medical Shop Tumsar----------\n")
        filehan.write("Bill No. : "+ str(billno) + "\n")
        filehan.write("Patient's Name : " + pname + "\n")
        filehan.write("Refered by Doctor : " + rdoc + "\n")
        filehan.write("Sr.No." + "   Name of Medicine" + "       Manufacturer" + "              Manu. Date" + "   Exp Date" + "   Quantity" + "   Price" + "   Amount" + "\n")

        total = amt = 0
        for i in range(n):
            print("Sr. No.", i+1)
            nmed = input("Enter name of medicine : ")   # Using the name of medicine  the  other details will be obtained from the database
            query1 = 'select * from medical_shop where Name_of_Med = "{}"'.format(nmed)
            cursor.execute(query1)
            result = cursor.fetchall()
            
            
            for row in result:
                if cursor.rowcount == 0 :   # Checking the existence of a medicine
                    print("Sorry! medicine with name ", nmed, "not found")
                else:
                    quan = int(input("Quantity : " ))
                    code = row[0]       # Getting details according to name of medicine
                    nmanu = row[2]
                    mandate = row[3]
                    expdate = row[4]
                    stockquant = row[5]
                    price = row[6]

                    #print(price)
                    oneprice = price / 10  # Calculating the amount of each tablet
                    amt = quan * oneprice  # Calculating the amount of One medicine
                    
                    text = (str(i+1) + "         " + nmed + "          " + str(nmanu) + "           " + str(mandate) + "    " + str(expdate) + "    " + str(quan) + "      " + str(price) + "    " + str(amt))

                total = total + amt   # Total Amount     
            filehan.write(text + "\n")
            reduce()    # Calling reduce function to reduce the purchased medicine from database    

        filehan.write("Total Amount: " + str(total) + "\n")
        filehan.close()
        
    elif ch == 3 :
        break

    else :
        print("Invalid Input")







                
                    

    

            
   
