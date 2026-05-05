def round_custom(x):
    tam_kisim = int(x)
    ondalik = x - tam_kisim

    if ondalik >= 0.5:
        return tam_kisim + 1
    else:
        return tam_kisim


while True:
    giris = input("Bir sayi gir (cikmak icin q): ")

    if giris.lower() == "q":
        print("Program kapatildi.")
        break

    sayi = float(giris)
    print("Sonuc:", round_custom(sayi))
