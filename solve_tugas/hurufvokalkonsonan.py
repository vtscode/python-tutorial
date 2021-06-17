# teks = 'Halo! 😁'

# # melakukan perulangan pada tiap karakter
# for karakter in teks:
#   print(karakter)

# cara 1
teks = input('Tuliskan teks: ').lower()
huruf_vokal = {
  'a': 0,
  'i': 0,
  'u': 0,
  'e': 0,
  'o': 0
}
total_huruf_vokal = 0

for karakter in teks:
  if karakter in ['a', 'i', 'u', 'e',  'o']:
    huruf_vokal[karakter] += 1
    total_huruf_vokal += 1

print(f'Total karakter: {len(teks)}')
print(f'Total huruf vokal: {total_huruf_vokal}')
print(f"""\
  a -> {huruf_vokal['a']}
  i -> {huruf_vokal['i']}
  u -> {huruf_vokal['u']}
  e -> {huruf_vokal['e']}
  o -> {huruf_vokal['o']}\
""")


# cara 2
teks = input('Tuliskan teks: ').lower()
dictionary_huruf_vokal = {
  'a': 0,
  'i': 0,
  'u': 0,
  'e': 0,
  'o': 0
}

for huruf_vokal in dictionary_huruf_vokal.keys():
  dictionary_huruf_vokal[huruf_vokal] = teks.count(huruf_vokal)

total_huruf_vokal = sum(dictionary_huruf_vokal.values())

print(f'Total karakter: {len(teks)}')
print(f'Total huruf vokal: {total_huruf_vokal}')
print(f"""\
  a -> {dictionary_huruf_vokal['a']}
  i -> {dictionary_huruf_vokal['i']}
  u -> {dictionary_huruf_vokal['u']}
  e -> {dictionary_huruf_vokal['e']}
  o -> {dictionary_huruf_vokal['o']}\
""")