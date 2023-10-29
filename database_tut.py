import pymysql
# Veritabani baglanti cumlesi

connection = pymysql.connect(host="localhost", 
                       user="root", 
                       password="admin1234", 
                       database="sys",
                       charset="utf8mb4") 
try:
    with connection.cursor() as cursor:
        # Kayıt okuma işlemi
        sql = "SELECT `id`,`name`,`surname`,`mail` FROM `ozcanakyuz`"
        cursor.execute(sql)

        myresult = cursor.fetchall()

        for row in myresult:
            id = str(row[0])
            name = row[1] + " " + row[2]
            mail = row[3]

            #Ekrana Yazdırma İşlemi
            print("ID: " + id)
            print("NAME: " + name)
            print("E-MAIL: " + mail)
        # for row in cursor.fetchall():
        #     #veriyi satırlardan nasıl çekeriz 
        #     name = str(row['name'])
        #     mail = str(row['mail'])

        #     #Ekrana Yazdırma İşlemi
        #     print("Ad Soyad : " + name)
        #     print("E-Mail : " + mail)

finally:
    connection.close()


