import mysql.connector

db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'Cuong-1705',
    database= 'database')
mycursor= db.cursor()

mycursor.execute("INSERT INTO new_table(name, email, password) VALUES(%s, %s, %s)", ('cuong', 'l.mcuong1705@gmail.com', '123cuong'))
db.commit()