def round_custom(x):
    tam_kisim = int(x)
    ondalik = x - tam_kisim

    if ondalik >= 0.5:
        return tam_kisim + 1
    else:
        return tam_kisim


sayi = float(input("Bir sayi gir: "))
print("Sonuc:", round_custom(sayi))
