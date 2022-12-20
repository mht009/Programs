'''import mysql.connector

mycon = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'CS2020_21')
if mycon.is_connected():
    print('Successfully Connected to MySQL Databases')

else:
    print("Connectio lost")

'''
lst = []
dict = {"this" : 4, "is": 2, "an" : 2, "awesome" : 7, "text" : 4}
for i in dict.values():
    print(i)
    lst.append(i)

print(lst)
m = (max(lst))

for a in dict:
    if dict[a] == m :
        print("longest word is ", a)


print(max(['this', 'is', 'an', 'awesome', 'text']))