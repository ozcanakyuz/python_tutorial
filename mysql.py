import mysql.connector

# Veritabani baglanti cumlesi
connection = mysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='ogrenciler',
                             charset='utf8mb4',
                             cursorclass=mysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        #tek satir okuma
        sql = "SELECT `id`, `firstname`, `lastname`, FROM `users`"
        cursor.execute(sql)

        for row in cursor.fetchall():
            # tum satirlari okuma
            firstname = str(row["firstname"])
            lastname = str(row["lastname"])

            #ekrana yazdirma
            print(f'ISIM: {firstname}')
            print(f'SOYISIM: {lastname}')
finally:
    connection.close()