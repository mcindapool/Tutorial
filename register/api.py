from flask import Flask
from flask import  render_template, request
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__,template_folder='templates')


db = yaml.load(open('db'))
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

mysql= MySQL(app)

@app.route('/signup', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email= userDetails['email']
        password= userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO new_table(name, email, password) VALUES(%s, %s)", (name, email, password))
        mysql.connection.commit()
        cur.close()
        return'success'
    
    return render_template ('register.html')

if __name__ == '__main__':
    
 app.run(debug= True, port=8000)