"""
Untuk membuat aplikasi web dengan python kita bisa menggunakan web framework seperti flask, Django, CherryPy, dll. Pada artikel ini kita hanya akan bahas framwork flask.

Apai itu Flask?
Flask adalah kerangka kerja aplikasi web (web framework) yang bersifat micro, istilah ini dipakai karena flask menyediakan pustaka atau alat bantu inti yang digunakan untuk proses membangun sebuah aplikasi web, jadi istilah micro ini bukan berarti bahwa mengembangkan aplikasi web dengan flask hanya dilakukan dalam skala kecil. Apabila ada kebutuhan lain yang dibutuhkan, flask mengizinkan kita untuk menambah fitur lain yang spesifik sebagai ekstensi.

Arsitektur Flask
Jika kalian pernah mengembangankan aplikasi web dengan framework PHP seperti Laravel atau Codeigniter kalian pasti sudah tidak asing lagi degan pola desain MVC (Model, View, Controller), yang mana konsep ini membagi tugas tanggung jawab dari setiap komponen utama aplikasi seperti manipulasi data, menghasilkan keluarah (output) dan bagian yang menjadi kontrol aplikasi.

Bagaimana dengan flask, apakah menerapkan konsep yang sama?

Flask tidak sepenuhnya menerapkan konsep MVC, karena di dalam flask istilah controller tidak dikenali. Fungsi controller sebetulanya telah di jalankan oleh aplikasi itu sendiri (objek dari kelas flask).

Struktur Direktori Aplikasi Flask
Berbeda dengan framework lainnya, Flask tidak menyediakan struktur direktori untuk menyimpan file-file yang dibutuhkan oleh aplikasi.

Kita dapat menentukan sendiri direktori nya, seperti contoh berikut ini:
static > img,css,js
templates > template.html
file.py
file2.py

File-file yang berhubungan dengan gambar, style CSS dan javascript kita buat sub folder masing-masing di dalam folder static, kemudian untuk template bisa di simpan di folder templates.

Cara Menginstal Flask
Kita bisa menginstal flask melalui program pip. pip adalah program manajemen paket standar di python, fungsinya untuk memudahkan kita untuk menginstal atau uninstal paket/modul di python. Berikut ini adalah cara menginstal flask di pyhton:

1. Buka command prompt (CMD) atau terminal
2. Ketik pip install flask
3. Tekan enter dan proses instalasi akan berjalan, tunggu hingga selesai dengan output ‘succsessfully installed flask-1.1.2′
4. Untuk mengecek apakah flask sudah benar-benar berhasil di instal coba masuk ke dalam IDLE (python shell) dengan cara ketik python untuk masuk ke program python interpreter setelah masuk yang ditandai dengantanda >>> ketik perintah import flask

Jika tidak ada pesan error itu berarti Flask sudah terpasang dengan benar dan siap untuk digunakan.

Membuat Aplikasi Web Pertama
Buatlah sebuah folder project baru, contoh disini saya membuat folder web_python lalu di dalam folder tersebut buat file baru dengan text editor dengan isi script berikut:
"""

from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
    return '<h1>Belajar Web dengan Python</h1>'

if __name__ == '__main__':
    application.run(debug=True)


"""
Perintah from flask import Flask untuk menginport kelas flask yang terdapat dalam modul flask.

Perintah application = Flask(name) merupakan objek dari kelas flask.

Perintah:

@application.route('/')
def index():
    return '<h1>Belajar Web dengan Python</h1>'

Berfungsi untuk memetakan URL ‘/’ pada fungsi index(). ini artinya ketika pengguna mengakses URL aplikasi web maka fungsi index() ini yang akan di panggil dan di jalankan.

Berfungsi untuk memetakan URL ‘/’ pada fungsi index(). ini artinya ketika pengguna mengakses URL aplikasi web maka fungsi index() ini yang akan di panggil dan di jalankan.

Perintah:
if __name__ == '__main__':
    application.run(debug=True)

Perintah di atas berfungsi untuk menjalankan aplikasi dengan metode run() dengan membawa argumen debug=True yang akan berfungsi untuk pelacakan kesalahan (debugging) pada aplikasi yang kita buat.

Simpan dan Coba Jalankan
Simpan file dengan nama app.py, lalu kemudian buka CMD dan arahkan direktori ke folder web_python

Saya menyimpannya di direktori D:\web_python (sesuaikan dengan direktori yang kalian buat)

Setelah itu jalankan aplikasi dengan perintah python app.py
Ketika di jalanakan aplikasi bisa di buka melalui URL yang diberikan seperti contoh di atas pada alamat http://127.0.0.1:5000/ atau bisa juga diganti dengan http://localhost:5000/. Maka akan tampil tulisan besar dan tebal

==> Belajar Web dengan Python

Selamat kalian sudah berhasil membuat aplikasi web dengan python menggunakan flask. Pada tutorial pertama sampai disini dulu tutorial berikut akan kita bahas mengenai penggunaan model dan template.

"""
