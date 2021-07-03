from flask import Flask, render_template,url_for,request

application = Flask(__name__)

"""
Pada bagian route objek aplikasi terdapat parameter methods dengan nilai GET dan POST, ini 
berfungsi untuk menentukan nilai action yang digunakan pada form.

Di dalam fungsi view index() kita buat kondisi IF dengan pernyataan request.
method==’POST’ maka nilai dari form untuk nama dan email akan di ambil menggunakan modul request.form.

Fungsi view index() akan melakukan render pada template tampil.html 
dengan membawa nilai nama dan email.

Sedangkan jika tidak ada permintaan (request) pada form, 
fungsi view index() akan menampilkan template login.html.
"""

@application.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        username = request.form['Username']
        password = request.form['Password']
        # Template tampil.html berfungsi untuk menampilkan nilai nama 
        # dan email yang di kirim dari form.
        return render_template('tampil.html',username=username,password=password)
    return render_template('login.html')

# untuk running aplikasi secara development
if __name__ == '__main__':
    application.run(debug=True)