from flask import Flask, render_template,url_for,request
from models import CobaForm

application = Flask(__name__)


@application.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username = request.form['Username']
        password = request.form['Password']
        return render_template('tampil.html',username=username,password=password)
    return render_template('login.html')

if __name__ == '__main__':
    application.run(debug=True)