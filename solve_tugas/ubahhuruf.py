# cara 1
teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

teks = teks.replace('a', pengganti)
teks = teks.replace('i', pengganti)
teks = teks.replace('u', pengganti)
teks = teks.replace('e', pengganti)
teks = teks.replace('o', pengganti)

print(f'\n{teks}')

# cara 2
teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

for huruf in 'aiueoAIUEO':
  teks = teks.replace(huruf, pengganti)

print(f'\n{teks}')