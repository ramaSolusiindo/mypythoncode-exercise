print("Nak, beli susu 1 botol dan jika ada telur, beli 6 telur!")
print("Baik bu, segera!")


def membeli(susu, telur=False):
    if susu:
        print("Susu dibeli")
        if telur:
            print("Beli telur 6")
        else:
            print('\tTelur tidak ada!')
    else:
        print("Tidak ada susunya bu!")


membeli(0)
# belanja = membeli(2,2)
# print(belanja)
