"""
Seperti yang sudah saya jelaskan di artikel sebelumnya bahwa arsitektur flask terdiri dari objek aplikasi, model dan templates. Model berperan untuk manipulasi data, template untuk menghasilkan view berupa kode-kode HTML dan objek aplikasi untuk menghubungkan antara model dan templates.

Membuat Aplikasi Web Dengan Flask Memakai Komponen Model dan Template
Langkah 1 : Membuat Model
Buatlah sebuah file dengan nama models.php dengan menggunakan teks editor, lalu simpan di dalam folder project aplikasi kalian.


class CobaData:
    def __init__(self):
        self.text='WKWOKWOWKOW'
    def getText(self):
        return self.text


Sintak di atas kita membuat kelas HelloWorld yang terdiri dari dua metode yaitu metode __init__(self) yang merupakan metode khusus dalam kelas di python, metode ini dikenal juga sebagai konstruktor dalam konsep pemrograman berorientasi objek. Metode ini berisi argumen string ‘Hello World’ dari kelas text. Fungsi yang kedua yaitu fungsi getText(self) yang mana fungsi ini akan menghasilkan nilai balik dari kelas text tersebut.

Langkah 2 : Membuat Template
Buatlah sebuah file html di dalam folder templates dengan nama helloworld.html

<html>
    <head>
        <title>Aplikasi dengan template dan model</title>
    </head>
    <body>
        <h2>{{ model.getText() }}</h2>
    </body>
</html>
Template ini berfungsi sebagai view yang akan menampilkan nilai dari model yang telah kita buat sebelumnya. Sintaknya kita tulis di dalam tanda {{ dan }}.

Langkah 3 : Membuat Objek Aplikasi
Buatlah file dengan app.py didalam folder project kalian, file app.py ini akan menjadi objek aplikasi yang akan menghubungkan antara model dan template yang telah kita buat.
"""
from flask import Flask, render_template
from models import HelloWorld

application = Flask(__name__)
@application.route('/')

def index():
    model = HelloWorld()
    return render_template('helloworld.html',model=model)

if __name__ == '__main__':
    application.run(debug=True)

"""
Baris pertama dan kedua pada kode di atas adalah untuk mengimport kelas flask render_template dan model HelloWorld.

Sintak application = Flask(__name__) berfungsi untuk membuat objek aplikasi dari kelas flask dengan melewatkan argumen modul utama (__name__).

Sintak @application.route(‘/’) berfungsi untuk memetakan fungsi dengan URL tertentu. Pada contoh ini URL ‘/’ dipetakan pada fungsi index().

Selanjutnya terdapat sintak:

def index():
    model = HelloWorld()
    return render_template('helloworld.html',model=model)
Yang merupakan fungsi/metode index() dengan membuat objek model dari kelas HelloWorld.

Fungsi index() akan menghasilkan nilai balik dari fungsi render_template() dengan argument yang dilewatkan yaitu template helloworld.html dan model dari objek model.

Apabila di lihat struktur direktori dari projek kali ini seperti berikut:

templates > helloworld.html


Langkah 4 : Menjalankan Aplikasi
Buka CMD arahkan direktori ke folder projek kalian, sebagai contoh saya membuat di direktori D:\web_python

run di terminal atau CMD perintah
python app.py


hasil di atas aplikasi web yang kita buat menggunakan flask (python) dengan menyertakan komponen model dan template telah berhasil. 

"""