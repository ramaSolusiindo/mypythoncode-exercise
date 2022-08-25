"""

daftar_buku = ['Seven Habits', 'How to Influence People', 'Go to']
print(daftar_buku)

for buku in daftar_buku:
    # print(buku, end=", ")
    print(buku)

print('\nTampilkan isi daftar buku pada indeks tertentu')
print(daftar_buku[0])

print()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# daftar_buku2 = [007, 'Kenji volume 2', -313, 3.14]
"""

daftar_buku2 = [7, 'Kenji volume 2', -313, 3.14]
# for buku in daftar_buku2:
    # print(buku)

for i in range(0, len(daftar_buku2)):
    print(daftar_buku2[i])

daftar_buku2.append('Shakura 2')

for i in range(0, len(daftar_buku2)):
    print(daftar_buku2[i])

daftar_buku2.clear()
print("\nDaftar buku kosong")
print(daftar_buku2)

print()
daftar_buku2 = [7, 'Kenji volume 2', -313, 3.14]
print(daftar_buku2)
daftar_buku2[0] = 'Power of mind'
print(daftar_buku2)
takeout = daftar_buku2.pop(1)
print(f"Buku yang diambil dari daftar adalah : {takeout}\n ")
print(daftar_buku2)

print()
daftar_buku2 = [7, 'Kenji volume 2', -313, 3.14]
print(daftar_buku2[:-1]) # START:END
del daftar_buku2[:-1]
print(daftar_buku2)
