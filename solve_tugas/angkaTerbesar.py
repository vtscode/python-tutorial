a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if a > b and a > c:
  print('A yang terbesar')
elif b > a and b > c:
  print('B yang terbesar')
else:
  print('C yang terbesar')

if a < b and a < c:
  print('A yang terkecil')
elif b < a and b < c:
  print('B yang terkecil')
else:
  print('C yang terkecil')

if (b > a > c) or (c > a > b):
  print('A adalah nilai tengah')
elif (a > b > c) or  (c > b > a):
  print('B adalah nilai tengah')
else:
  print('C adalah nilai tengah')