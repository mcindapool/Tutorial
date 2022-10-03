from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector

app=Flask(__name__,template_folder='templates')

db= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'Cuong-1705',
    database= 'database')

app.config['MYSQL_HOST']= db
app.config['MYSQL_USER']= db
app.config['MYSQL_PASSWORD']= db
app.config['MYSQL_DB']= db
mysql= MySQL(app)

@app.route('/signup', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']
        password= request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO new_table(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        cur.close()
        return'success'
    return render_template ('register.html')

if __name__ == '__main__':
    
 app.run(debug= True, port=8000)