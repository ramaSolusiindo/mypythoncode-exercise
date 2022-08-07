"""
 Perulangan dengan if, joke programming
"""

print("Nak, beli susu 1 botol dan jika ada telur, beli 6")
print("Baik bu, segera!")

num_susu = 1
num_telur = 0

if num_susu != 0:
    if num_telur != 0:
        print("Telurnya ada!")
        print(f"{num_telur} Susu di beli")
    else:
        print("Telurnya tidak ada!")
        print(f"{num_susu} Susu di beli")
else:
    print("\nBu, susunya habis!")


