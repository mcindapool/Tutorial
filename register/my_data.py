import mysql.connector

def new_func():
    db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'Cuong-1705',
    database= 'database')
        
    return db

db = new_func()

mycursor= db.cursor()

if __name__ == '__main__':
    new_func()

