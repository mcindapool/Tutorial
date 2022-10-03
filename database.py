import mysql.connector

db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'Cuong-1705',
    database= 'testdatabase')
#file= 'CREATE DATABASE testdatabase '
#file1= ["CREATE TABLE \'testdatabase\'.\'costumer\'(\'ID\' INT NOT NULL, \'BUY\' VARCHAR(45) NULL, \'SALE\' VARCHAR(45) NULL, \'PRIMARY KEY\' (\'ID\'))"]


mycursor= db.cursor()
#mycursor.execute('CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')
#mycursor.execute("INSERT INTO Person(name, age) VALUES(%s,%s)",("Hung", 26))
#db.commit()
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
 print(x)
