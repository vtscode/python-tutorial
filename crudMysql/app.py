"""
Aplikasi Create, Read, Update, Detele (CRUD) adalah aplikasi standar yang pasti 
ada jika kita ingin membuat aplikasi web dinamis. Dengan fungsi CRUD kita dapat 
melakukan manipulasi data di dalam database melalui aplikasi yang dibuat. 
Saat ini kita akan belajar bagaimana membuat aplikasi CRUD dengan menggunakan Python 
dengan database yang dipakai adalah MySQL.

File app.py adalah file yang menjadi file utama 
atau bisa kita sebut sebagai controllernya. 
Dimana file ini sebagai objek aplikasi yang menghubungkan 
antara template melalui fungsi view() 
dengan data yang kita ambil dari database MySQL.

Sampai saat ini untuk di indonesia python bukanlah bahasa pemrograman 
yang populer untuk membuat aplikasi web, kebanyakan dari kita 
lebih memilih PHP karena lebih mudah dan mempunyai dokumentasi yang banyak. 
Namun jangan salah di luar negeri trends bahasa python sudah sangat tinggi 
bahkan lebih tinggi trendnya jika dibandingkan dengan PHP. 

contoh aplikasi web CRUD di python kalian perlu menyiapkan beberapa hal seperti:
- Server Database MySQL
- Modul PyMySQL
- Flask
- Bootstrap

Buat database dengan nama db_penjualan.

create database db_penjualan;
Setelah itu buat tabel barang di dalam database db_penjualan

create table barang (
   id_barang int not null auto_increment primary key,
   nama_barang varchar(20) not null,
   harga int,
   stok int
);


Apa itu PIP
Pip merupakan program manejer paket yang ada di python digunakan untuk menginstall modul yang kita butuhkan dalam hal ini adalah Flask dan PyMySQL.

Apa itu PyMySQL
PyMySQL merupakan salah satu interface atau modul yang tersedia di dalam python, library ini berfungsi untuk menghubungkan ke server database mysql dengan menggunakan python. Requirements yang dibutuhkan untuk menggunakan interface ini adalah kita sudah menggunakan pythonn dengan versi >=2.7 atau 3.5 dan database mysql server dengan versi diatas 5.5.

Menginstal Modul PyMySQL
Untuk menginstall modul PyMySQL sangatlah mudah, kita hanya perlu menginstall lewat program pip. Langkah-langkahnya seperti berikut:

Buka Command Prompt dan ketikan perintah:

python -m pip install PyMySQL
Atau bisa juga

pip install PyMySQL

Apai itu Flask?
Flask adalah kerangka kerja aplikasi web (web framework) yang bersifat micro, istilah ini dipakai karena flask menyediakan pustaka atau alat bantu inti yang digunakan untuk proses membangun sebuah aplikasi web, jadi istilah micro ini bukan berarti bahwa mengembangkan aplikasi web dengan flask hanya dilakukan dalam skala kecil. Apabila ada kebutuhan lain yang dibutuhkan, flask mengizinkan kita untuk menambah fitur lain yang spesifik sebagai ekstensi.


"""

"""
Setelah itu buat file app.py menggunakan teks editor. 
File ini berfungsi sebagai objek aplikasi (kalo di dalam 
framework lain bisa kita sebut sebagai controller

File app.py adalah file yang menjadi file utama atau bisa kita sebut sebagai controllernya. Dimana file ini sebagai objek aplikasi yang menghubungkan antara template melalui fungsi view() dengan data yang kita ambil dari database MySQL.

fungsi
"""

from flask import Flask, render_template, \
  request, redirect, url_for
import pymysql.cursors, os

application = Flask(__name__)

# membuat variabel awal dengan nilai awal None
# conn = variabel untuk menampung koneksi
# cursor = menampung nilai data dari database
conn = cursor = None

#fungsi koneksi database
def openDb():
   # mengambil variabel global ke dlm function
   global conn, cursor
   # inisiasi connection ke database dengan host=localhost, user=root, password="",
   # nama db="db_penjualan setting charset utf8"
   conn = pymysql.connect(host="localhost",user="root",password="",db="db_penjualan",charset='utf8')
   # menaruh value koneksi ke dlm variabel cursor
   cursor = conn.cursor()	

#fungsi untuk menutup koneksi
def closeDb():
   # mengambil variabel global ke dlm function
   global conn, cursor
   # menutup koneksi dari variabel conn dan cursor
   cursor.close()
   conn.close()

#fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():
   # memanggil function openDB()
   openDb()
   # membuat variabel penampung data
   container = []
   # query sql utk menselect semua kolom di dlm table barang
   sql = "SELECT * FROM barang"
   # eksekusi query dengan variabel cursor
   cursor.execute(sql)
   # menampung data yang di dapat dari cursor ke dalam variabel results
   results = cursor.fetchall()
   # melooping variabel results dan menambahkan satu per satu ke dlm variabel container
   for data in results:
      container.append(data)
   # kita harus close koneksi jika sudah di eksekusi.
   closeDb()
   # nilai data kita render dlm index.html dengan nama variabel pembawa yaitu container
   return render_template('index.html', container=container,)

#fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      # mengambil data dari request form
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      openDb()
      sql = "INSERT INTO barang (nama_barang, harga,stok) VALUES (%s, %s, %s)"
      val = (nama, harga, stok)
      cursor.execute(sql, val)
      # koneksi di jalankan ke dlm mysql
      conn.commit()
      closeDb()
      # mengarahkan user ke dlm routing index atau /
      return redirect(url_for('index'))
   else:
      # render tampilan jika method GET
      return render_template('tambah.html')
#fungsi view edit() untuk form edit
@application.route('/edit/<id_barang>', methods=['GET','POST'])
def edit(id_barang):
   openDb()
   # mengambil data dengan id_barang tertentu
   cursor.execute('SELECT * FROM barang WHERE id_barang=%s', (id_barang))
   # fetchone untuk mengambil 1 data saja
   data = cursor.fetchone()
   if request.method == 'POST':
      id_barang = request.form['id_barang']
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      sql = "UPDATE barang SET nama_barang=%s, harga=%s, stok=%s WHERE id_barang=%s"
      # menampung data dalam bentuk tuple ke dlm variabel val 
      val = (nama, harga, stok, id_barang)
      cursor.execute(sql, val)
      # koneksi di jalankan ke dlm mysql
      conn.commit()
      closeDb()
      # mengarahkan user ke dlm routing index atau /
      return redirect(url_for('index'))
   else:
      closeDb()
      # render tampilan jika method GET dengan memberikan data di dlm variabel pembawa yaitu data
      return render_template('edit.html', data=data)

#fungsi untuk menghapus data
@application.route('/hapus/<id_barang>', methods=['GET','POST'])
def hapus(id_barang):
   openDb()
   # menghapus data dlm mysql dengan id_barang tertentu
   cursor.execute('DELETE FROM barang WHERE id_barang=%s', (id_barang,))
   # koneksi di jalankan ke dlm mysql
   conn.commit()
   closeDb()
   # mengarahkan user ke dlm routing index atau /
   return redirect(url_for('index'))
      
if __name__ == '__main__':
   application.run(debug=True)