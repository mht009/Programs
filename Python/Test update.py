import mysql.connector as sqltor

mycon = sqltor.connect(host = '127.0.0.1', user = "root", passwd = "root", database = 'MedicalShop_v3')
cursor = mycon.cursor()

def up_med():
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

            pri = input("Enter new Price (leave blank if you don't want to change it): ")
            if pri == '':
                pri0 = row[7]
                pri = float(pri0)

            queryu2 = 'UPDATE Medicines SET Batch_No = "{}", Man_Date = "{}", Exp_Date = "{}", Quantity = {},\
                     PricePer10 = {} where Name_of_Med = "{}"'.format(bno, Dman, Dexp, qua, pri, nmed)
            cursor.execute(queryu2)
            print("Successfully updated the record.")
            print("****************************************************************************************\n")
        else:
            print('Updation Cancelled')   

        upd = input("Do you want to update another record (y/n) : ").lower()
        if upd == 'y':
            up_med()
        else:
            print("****************************************************************************************\n")
    '''
    except:
        print("Error!")
        up_med()
'''
mycon.close()

        
