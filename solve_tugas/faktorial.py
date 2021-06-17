# cara 1
n = int(input('Masukkan nilai n: '))
faktorial = 1

for i in range(2, n + 1):
  faktorial *= i

print(f'{n}! = {faktorial}')

# # cara 2
# n = int(input('Masukkan nilai n: '))

# def hitung_faktorial (n):
#   if n > 2:
#     return n * hitung_faktorial(n - 1)

#   return 2

# faktorial = hitung_faktorial(n)
# print(f'{n}! = {faktorial}')

# # cara 3
# import math

# n = int(input('Masukkan nilai n: '))
# faktorial = math.factorial(n)
# print(f'{n}! = {faktorial}')