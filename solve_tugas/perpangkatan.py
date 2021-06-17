# # silahkan uncomment jika ingin mencoba salah satu cara
# # cara 1
# bilangan = int(input('Masukkan bilangan: '))
# pangkat = int(input('Masukkan pangkat: '))

# hasil = bilangan ** pangkat
# print(f'Hasil = {hasil}')

# # cara 2
# bilangan = int(input('Masukkan bilangan: '))
# pangkat = int(input('Masukkan pangkat: '))

# hasil = pow(bilangan, pangkat)
# print(f'Hasil = {hasil}')

# # cara 3
# bilangan = int(input('Masukkan bilangan: '))
# pangkat = int(input('Masukkan pangkat: '))

# hasil = bilangan

# for i in range(pangkat - 1):
#   hasil *= bilangan

# print(hasil)

# cara 4
bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')