print("Nak, beli susu 1 botol dan jika ada telur, beli 6 telur!")
print("Baik bu, segera!")


def membeli(susu, telur=False):
    if susu:
        print(f"{susu} Susu dibeli")
        if telur:
            print(f"Beli susu {telur}")
        else:
            print('\tTelur tidak ada!')
    else:
        print("Tidak ada susunya bu!")


membeli(1,7)
# belanja = membeli(2,2)
# print(belanja)
