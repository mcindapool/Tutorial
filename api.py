from flask import Flask
from flask import  render_template, redirect, url_for


app=Flask(__name__,template_folder='templates')

@app.route('/')
def home ():
    return "welcome"

@app.route('/login')
def login():
    return render_template ('login.html.html')

if __name__ == '__main__':
    
 app.run(debug= True, port=8000)