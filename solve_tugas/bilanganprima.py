# check apakah suatu bilangan adalah bilangan prima
def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True
print(is_prima(4)) # False
print(is_prima(11)) # True

# list bilngan prima
def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima
"""
Pejelasan

    Pada fungsi di atas kita membuat satu buah list dengan nama list_bilangan_prima
    List tersebut selanjutnya akan kita isi dengan bilangan-bilangan prima menggunakan fungsi list.append()
    Kita melakukan perulangan dari range angka awal sampai angka akhir + 1.
        Kenapa pakai + 1? Itu akibat dari fungsi range() yang tidak menjadikan batas sebagai angka terakhir, sehingga kita perlu menambahkannya dengan angka 1–jika ingin memasukkannya.
    Pada setiap iterasi, kita memanggil fungsi is_prima(x) untuk memeriksa apakah nilai x adalah bilangan prima atau bukan.
    Jika iya, maka ia akan dimasukkan ke dalam list.
    Dan jika tidak, program akan melanjutkan ke iterasi berikutnya
"""
print(cari_bilangan_prima(1, 40))