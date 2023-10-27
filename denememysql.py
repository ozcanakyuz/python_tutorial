import pymysql

mydb = pymysql.connect(host="localhost", 
                       user="root", 
                       password="admin1234", 
                       database="schema_tutorial",
                       charset="utf8mb4") 

cursor = mydb.cursor()

query = ("SELECT * FROM schema_tutorial.pytutorial")

cursor.execute(query)

for FULL in cursor:
    print(FULL)

cursor.close()
mydb.close()