import pymysql

mydb = pymysql.connect(host="localhost", 
                       user="root", 
                       password="admin1234", 
                       database="sys",
                       charset="utf8mb4") 

cursor = mydb.cursor()

query = ("SELECT * FROM sys.ogrenci_listesi")

cursor.execute(query)

for FULL in cursor:
    print(FULL)

cursor.close()
mydb.close()