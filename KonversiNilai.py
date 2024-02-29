nilai = float(input("Masukkan Nilai: "))

def konversiNilai(nilai):

    if nilai < 50:
        return "E"
    elif nilai >= 50 < nilai < 60:
        return "D"
    elif nilai >= 60 < nilai < 70:
        return "C"
    elif nilai >= 70 < nilai < 80:
        return "B"
    else:
        return "A"

hasilKonversi = konversiNilai(nilai)

print(" Hasil konversi nilai : ",hasilKonversi)
