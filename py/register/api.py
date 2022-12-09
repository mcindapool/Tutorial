from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__,template_folder='templates')



app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'Cuong-1705'
app.config['MYSQL_DB']= 'database'

mysql= MySQL(app)

@app.route('/signup', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password= request.form.get('password')
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO new_table(email, name, password) VALUES(%s, %s, %s)", (email, name, password))
        mysql.connection.commit()
        cur.close()
        return'success'
    return render_template ('register.html')

if __name__ == '__main__':
    
 app.run(debug= True)