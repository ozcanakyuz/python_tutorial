import pymysql
# Veritabani baglanti cumlesi
connection = pymysql.connect(host="localhost", 
                       user="root", 
                       password="admin1234", 
                       database="sys",
                       charset="utf8mb4") 
try:
    with connection.cursor() as cursor:
        #tek satir okuma
        sql = "SELECT `name` FROM sys.ozcanakyuz"
        cursor.execute(sql)

        for row in cursor.fetchall():
            # tum satirlari okuma
            id = int(row['id'])
            name = str(row['name'])
            surname = str(row['surname'])
            mail = str(row['mail'])

            #ekrana yazdirma
            print(f'ID: {id}')
            print(f'NAME: {name}')
            print(f'SURNAME: {surname}')
            print(f'MAIL: {mail}')
            
finally:
    connection.close()