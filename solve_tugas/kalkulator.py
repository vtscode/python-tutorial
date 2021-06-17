"""
Buat program kalkulator sederhana, yang hanya bisa menghitung 4 buah operasi saja:

1. Operasi penjumlahan
2. Operasi pengurangan
3. Operasi perkalian
4. Operasi pembagian

Output
Bagaimana output dari kalkulatornya?

Output hasil akhirnya kira-kira akan terlihat seperti ini:

=========================
Operasi Matematika
  1. Jumlah      [+]
  2. Kurang      [-]
  3. Kali        [*]
  4. Bagi        [/]
=========================
Pilih operasi (1/2/3/4): 1
Masukkan bilangan pertama: 10
Masukkan bilangan kedua: 5
=========================
Hasil operasi dari 10 + 5 = 15

"""

print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))

print('=' * 25)

if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
  print('Tidak valid')