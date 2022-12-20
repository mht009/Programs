Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Mohit\Desktop\Programming\Python\Class 12 Project\CS project Medical shop (alter with name csv file) V2.8.py
-----Medical Shop Management System------
---------USAVN Medical Shop---------

Date : 2022-06-16

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 1
Successfully Connected to MySQL Databases 

--------------------------------------------------
-----Medicine Database------


1. Add Medicine 
2. Remove Medicine 
3. Update Medicine Information 
4. List Of Medicine 
5. Main Menu
What do you want to do ? (1/2/3/4/5) : 4
------ Medicines in Stock------

Code Name of Medicine       Name of Man.  Batch No.  Man. Date   Exp.Date   Quantity      Price
101          Medler Comed Chemicals Ltd.    RGT0095 2020-05-01 2023-04-01        104       42.0
102      Montemac-L             Macleods    Rmx4502 2022-01-01 2024-01-01        450      123.0
103       Montex FX           Sun Pharma    RGT0095 2018-05-01 2022-04-01         75      124.5
104        benadryl    Johnson & Johnson    RBH4521 2022-05-01 2024-04-01         98     1180.0
105        Azee 500                Cipla    C111118 2021-08-01 2024-06-01         94     236.66
------------------------------------------------------------

For Database Menu Press y and Press Enter(return) for Main Menu : y
1. Add Medicine 
2. Remove Medicine 
3. Update Medicine Information 
4. List Of Medicine 
5. Main Menu
What do you want to do ? (1/2/3/4/5) : 1

------Adding Medicine to Stock------

Enter Code : 106
Enter Name of Medicine : Pacimol 650
Enter Name of Manufacturer : Piramal
Enter Batch No. : YTG4562
Enter Date of Manufacturing (YYYY-MM-DD) : 2022-01-01
Enter Date of Expiry (YYYY-MM-DD) : 2024-12-01
Enter Quantity : 500
Enter Price Per 10 Tablets / 10 units : 10
Data Saved Successfully
Want to add more ?(y/n): n
------------------------------------------------------------

For Database Menu Press y and Press Enter(return) for Main Menu : y
1. Add Medicine 
2. Remove Medicine 
3. Update Medicine Information 
4. List Of Medicine 
5. Main Menu
What do you want to do ? (1/2/3/4/5) : 4
------ Medicines in Stock------

Code Name of Medicine       Name of Man.  Batch No.  Man. Date   Exp.Date   Quantity      Price
101          Medler Comed Chemicals Ltd.    RGT0095 2020-05-01 2023-04-01        104       42.0
102      Montemac-L             Macleods    Rmx4502 2022-01-01 2024-01-01        450      123.0
103       Montex FX           Sun Pharma    RGT0095 2018-05-01 2022-04-01         75      124.5
104        benadryl    Johnson & Johnson    RBH4521 2022-05-01 2024-04-01         98     1180.0
105        Azee 500                Cipla    C111118 2021-08-01 2024-06-01         94     236.66
106     Pacimol 650              Piramal    YTG4562 2022-01-01 2024-12-01        500       10.0
------------------------------------------------------------

For Database Menu Press y and Press Enter(return) for Main Menu : 

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 2
Time : 2022-06-16 19:50:48

---------------------------------USAVN Medical Shop Tumsar--------------------------------------

Bill No. 14
Date & Time : 2022-06-16 19:50:48
Name of patient : Bhumeshwar Chintanwar
Traceback (most recent call last):
  File "C:\Users\Mohit\AppData\Local\Programs\Python\Python38\lib\site-packages\mysql\connector\connection_cext.py", line 535, in cmd_query
    self._cmysql.query(query,
_mysql_connector.MySQLInterfaceError: Data too long for column 'Patient_Name' at row 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Mohit\Desktop\Programming\Python\Class 12 Project\CS project Medical shop (alter with name csv file) V2.8.py", line 272, in <module>
    cursor.execute(query0)
  File "C:\Users\Mohit\AppData\Local\Programs\Python\Python38\lib\site-packages\mysql\connector\cursor_cext.py", line 269, in execute
    result = self._cnx.cmd_query(stmt, raw=self._raw,
  File "C:\Users\Mohit\AppData\Local\Programs\Python\Python38\lib\site-packages\mysql\connector\connection_cext.py", line 540, in cmd_query
    raise errors.get_mysql_exception(exc.errno, msg=exc.msg,
mysql.connector.errors.DataError: 1406 (22001): Data too long for column 'Patient_Name' at row 1
>>> 
============================== RESTART: C:\Users\Mohit\Desktop\Programming\Python\Class 12 Project\CS project Medical shop (alter with name csv file) V2.8.py ==============================
-----Medical Shop Management System------
---------USAVN Medical Shop---------

Date : 2022-06-16

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 1
Successfully Connected to MySQL Databases 

--------------------------------------------------
-----Medicine Database------


1. Add Medicine 
2. Remove Medicine 
3. Update Medicine Information 
4. List Of Medicine 
5. Main Menu
What do you want to do ? (1/2/3/4/5) : 4
------ Medicines in Stock------

Code Name of Medicine       Name of Man.  Batch No.  Man. Date   Exp.Date   Quantity      Price
101          Medler Comed Chemicals Ltd.    RGT0095 2020-05-01 2023-04-01        104       42.0
102      Montemac-L             Macleods    Rmx4502 2022-01-01 2024-01-01        450      123.0
103       Montex FX           Sun Pharma    RGT0095 2018-05-01 2022-04-01         75      124.5
104        benadryl    Johnson & Johnson    RBH4521 2022-05-01 2024-04-01         98     1180.0
105        Azee 500                Cipla    C111118 2021-08-01 2024-06-01         94     236.66
106     Pacimol 650              Piramal    YTG4562 2022-01-01 2024-12-01        500       10.0
------------------------------------------------------------

For Database Menu Press y and Press Enter(return) for Main Menu : 

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 2
Time : 2022-06-16 19:55:14

---------------------------------USAVN Medical Shop Tumsar--------------------------------------

Bill No. 14
Date & Time : 2022-06-16 19:55:14
Name of patient : Sahil Chintanwar
Refered by Doctor : Dr. Saira
Address of Patient : Bhandara
Number of Medicines : 4

Sr. No. 1
Enter name of medicine : Pacimol 600
Sorry! medicine with name  Pacimol 600 not found

Invoice Printing Failed ! 
_____________________________________ 

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 2
Time : 2022-06-16 19:55:14

---------------------------------USAVN Medical Shop Tumsar--------------------------------------

Bill No. 14
Date & Time : 2022-06-16 19:55:14
Name of patient : Sahil
Refered by Doctor : Dr. Saira
Address of Patient : Bhandara
Number of Medicines : 4

Sr. No. 1
Enter name of medicine : Pacimol 650
Quantity : 20


Sr. No. 2
Enter name of medicine : benadryl
Quantity : 1


Sr. No. 3
Enter name of medicine : Azee 500
Quantity : 6


Sr. No. 4
Enter name of medicine : Montemaz-L
Sorry! medicine with name  Montemaz-l not found

Invoice Printing Failed ! 
_____________________________________ 

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 2
Time : 2022-06-16 19:55:14

---------------------------------USAVN Medical Shop Tumsar--------------------------------------

Bill No. 14
Date & Time : 2022-06-16 19:55:14
Name of patient : Sahil
Refered by Doctor : Dr. Saira
Address of Patient : Bhandara
Number of Medicines : 4

Sr. No. 1
Enter name of medicine : Pacimol 600
Sorry! medicine with name  Pacimol 600 not found

Invoice Printing Failed ! 
_____________________________________ 

---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 2
Time : 2022-06-16 19:55:14

---------------------------------USAVN Medical Shop Tumsar--------------------------------------

Bill No. 14
Date & Time : 2022-06-16 19:55:14
Name of patient : Sahil
Refered by Doctor : Dr. Saira
Address of Patient : Bhandara
Number of Medicines : 2

Sr. No. 1
Enter name of medicine : benadryl
Quantity : 1


Sr. No. 2
Enter name of medicine : Montemac-L
Quantity : 10


Invoice Printed Successfully 
_____________________________________ 


---------------------------------------------------------------------------------
1. Update\View Stock On Database. 
2. Print Invoice/Bill for a Purchase.(Create a file) 
3. Exit. 
What do you want to do ? (1/2/3) : 3
>>> 