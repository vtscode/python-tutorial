"""
File merupakan elemen penting dalam pemrograman termasuk di Python. Terkadang kita ingin membaca file untuk mengolah data atau menulis ke dalam file untuk menyimpan data

Python mempunyai fungi untuk menangani file seperti menulis, membaca, merubah dan menghapus file

Fungsi awal untuk dapat melakukan operasi file adalah open() yang mempunyai 2 parameter yaitu filename dan mode.

filename adalah nama file yang ingin diproses sedangkan mode adalah metode operasi yang ingin dilakukan. Ada 3 jenis metode operasi dasar di Python yaitu
mode	makna	deskripsi
r	read	Untuk membaca file
a	append	Untuk menambah data
w	write	Untuk menulis data
x     Opens a file for exclusive creation. If the file already exists, the operation fails.
t     Opens in text mode. (default)
b     Opens in binary mode.
+     open for exclusive creation, failing if the file already exists (Python 3)

r+    opens for reading and writing (cannot truncate a file)
w+    for writing and reading (can truncate a file)
rb    for reading a binary file. The file pointer is placed at the beginning of the file.
rb+   reading or writing a binary file
wb+   writing a binary file
a+    opens for appending
ab+   Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.


Contoh, Buatlah sebuah file dan simpan dengan nama data.txt dan isi file dengan kalimat berikut

 Latihan dasar menangani file di Python

Selanjutnya kita akan melakukan operasi dengan file data.txt """
#1 Operasi read
#membuka file data.txt dengan mode read
data = open('data.txt','r')

#mencetak isi data.txt
print(data.read())
"""
Buka editor dan salin kode dibawah, simpan dengan nama file.py

Pastikan file data.txt berada dalam 1 folder dengan kode di atas. Selanjutnya kita jalankan dan hasilnya adalah

$ python file.py
  Latihan dasar menangani file di Python
"""
#2 Operasi append
#membuka file data.txt dengan mode append untuk menambah data
data = open('data.txt','a')

#menambah kalimat
data.write("Belajar python di ngodingdata.com")
data.write("Yuk belajar coding")
data.write("Jago python handling dalam sehari")
data.close() 
"""
Fungsi close() digunakan untuk mengakhiri sumber daya yang digunakan dari program file

Setalah kode di atas dijalankan coba buka file data.txt maka isi file akan berubah seperti ini

Latihan dasar menangani file di Python
Belajar python di ngodingdata.com

Untuk menambah beberapa kalimat agar setiap kalimat berada di baris baru gunakan \n diakhir kalimat """
#membuka file data.txt dengan mode append untuk menambah data
data = open('data.txt','a')

#menambah / append kalimat
data.write("Yuk belajar coding\n")
data.write("Jago python handling dalam sehari\n")
data.write("Yuk rajin baca ngodingdata.com\n")
data.close() 
"""
Buka / reload kembali file data.txt maka isinya akan berubah seperti ini

Latihan dasar menangani file di Python
Belajar python di ngodingdata.com
Yuk belajar coding
Jago python handling dalam sehari
Yuk rajin baca ngodingdata.com

#3 Operasi write

Operasi write memberikan kita akses untuk menulis ke dalam file baru"""
#membaca file databaru.txt dengan mode write
file = open('databaru.txt','w') 

#menulis kalimat di file databaru.txt
file.write("Belajar nulis di file\n") 
file.write("nulis di file dengan mode write\n") 
file.close() 
"""
Setelah kode berhasil dijalankan maka akan terbuat file dengan nama databaru.txt dengan isi sebagai berikut

Belajar nulis di file
nulis di file dengan mode write

Trus apa bedanya mode append dan write kalau sama-sama bisa menulis di file?

Mode append akan menulis tanpa menghapus teks yang sudah ada di file sedangkan mode write akan mereplace ulang teks di file

Jadi semisal kita ingin menulis kembali di file databaru.txt dengan isi teks yang berbeda maka isi file sebelumnya akan hilang diganti dengan kalimat baru

Coba jalankan kode berikut: """
#membaca file databaru.txt dengan mode write
file = open('databaru.txt','w') 

#menulis kalimat baru di file databaru.txt
file.write("Coba tulis lagi\n")
file.close() 
"""
Coba setelah dijalankan buka file databaru.txt maka kalimat baru akan mengganti kalimat lama dan hasilnya adalah

Coba tulis lagi

Ada beberapa hal lagi yang harus diketahui untuk menangani file antara lain
# Menghapus file

Untuk menghapus file kita gunakan library os dengan fungsinya yaitu remove()

Misal kita ingin menghapus file databaru.txt maka kode akan seperti ini

""" 
import os

if(os.path.exists("databaru.txt")):
  os.remove("databaru.txt")


"""
# Menutup file secara otomatis

Dalam melakukan operasi file kita menggunakan fungsi close() untuk menutup file agar tidak mengambil resouce. Dengan with kita dapat menutup operasi file handling secara otomatis

Misal kita punya file data.txt yang mempunyai isi seperti ini

Latihan dasar menangani file di Python

Tambah data untuk operasi append dengan with """
with open("data.txt", "a") as file:
    file.write("gunakan with untuk menutup file secara otomatis")


"""
# Melakukan penanganan jika file tidak ditemukan

Jika kita ingin membaca file pastikan bahwa ada file yang akan kita gunakan. Ketika membaca file sedangkan file tidak ada maka akan ada error
"""
with open("dataku.txt", "r") as file:
    print(file.read())

"""
Hasil eror

FileNotFoundError Traceback (most recent call last) 
 ----> 1 with open("dataku.txt", "r") as file:       
       2 print(file.read()) FileNotFoundError: [Errno 2] No such file or directory: 'dataku.txt'

Kita bisa gunakan try dan except untuk menangani kondisi seperti itu.
"""

try:
  with open("dataku.txt", "r") as file:
    print(file.read())
except:
  print("File gak ada")

""" Jadi pada blok kode try akan dicek apakah ada file yang ingin dibaca. Jika ada maka akan lanjut di kode berikutnya yaitu fungsi read() tetapi jika tidak ada maka akan masuk di blok kode except untuk memberikan pesan error yang kita buat sehingga kode program tidak mengeluarkan error langsung dari sistem. 

Another mode with sign +
r+ :-

    Open the file for Reading and Writing
    Once Opened in the beginning file pointer will point to 0
    Now if you will want to Read then it will start reading from beginning
    if you want to Write then start writing, But the write process will begin from pointer 0. So there would be overwrite of characters, if there is any
    In this case File should be present, either will FileNotFoundError will be raised.

w+ :-

    Open the file for Reading and Writing
    If file exist, File will be opened and all data will be erased,
    If file does not exist, then new file will be created
    In the beginning file pointer will point to 0 (as there is not data)
    Now if you want to write something, then write
    File pointer will be Now pointing to end of file (after write process)
    If you want to read the data now, seek to specific point. (for beginning seek(0))

So, Overall saying both are meant to open the file to read and write but difference is whether we want to erase the data in the beginning and then do read/write or just start as it is.

abc.txt - in beginning

1234567
abcdefg
0987654
1234

Code for r+
"""
with open('abc.txt', 'r+') as f:      # abc.txt should exist before opening
    print(f.tell())                   # Should give ==> 0
    f.write('abcd')                   
    print(f.read())                   # Pointer is pointing to index 3 => 4th position
    f.write('Sunny')                  # After read pointer is at End of file
"""
Output

0
567
abcdefg
0987654
1234

abc.txt - After Run:

abcd567
abcdefg
0987654
1234Sunny

Resetting abc.txt as initial

Code for w+
"""
with open('abc.txt', 'w+') as f:     
    print(f.tell())                   # Should give ==> 0
    f.write('abcd')                   
    print(f.read())                   # Pointer is pointing to index 3 => 4th position
    f.write('Sunny')                  # After read pointer is at End of file
"""
Output

0


abc.txt - After Run:

abcdSunny
"""