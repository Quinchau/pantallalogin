import mysql.connector

conexion = mysql.connector.connect(user='root', password='SQLpassword',
                                    host='localhost',
                                    database='bd_maracay',
                                    port='3306')
print(conexion)