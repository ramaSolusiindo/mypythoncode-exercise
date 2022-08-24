"""
Ini adalah dasar tipe data list
"""
daftar_buku = ['Seven Samurai', 'Sherlock Holmes', 'Harry Potter', "17an"]

print("Menampilkan data list :")
print(daftar_buku)

print("\nMenampilkan data list dengan slicing :")
print(daftar_buku[:])
print(daftar_buku[4:])

print("\nMenampilkan data list dengan for, :")
for buku in daftar_buku:
    print(buku)

print("\nMenampilkan data list dengan for dan range :")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
