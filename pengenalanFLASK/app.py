from flask import Flask, render_template,url_for,request
from models import CobaData

application = Flask(__name__)

@application.route('/')
def index():
    model = CobaData()
    return render_template('helloworld.html',model=model)
# def index():
#     if request.method=='POST':
#         nama = request.form['nama']
#         email = request.form['email']
#         return render_template('tampil.html',nama=nama,email=email)
#     return render_template('index.html')

@application.route('/index')
# def index():
#     kalimat='Menyertakan file gambar dan CSS di Flask'
#     return render_template('home.html',kalimat=kalimat)

@application.route('/contact')
def contactSaya():
    return render_template('contact.html')

@application.route('/about')
def aboutSaya():
    return render_template('about.html')

if __name__ == '__main__':
    application.run(debug=True)