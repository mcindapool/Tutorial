from flask import Flask
from flask import  render_template, redirect, url_for


app=Flask(__name__,template_folder='templates')

@app.route('/index')
def index():
    return render_template ('index.html.html')

if __name__ == '__main__':
    
    app.run()
