alas = int(input("Masukan Luas: "))
Tinggi = int(input("Masukan Keliling: "))

sisi1 = int(input(" Masukan Sisi 1: "))
sisi2 = int(input(" Masukan Sisi 2: "))
sisi3 = int(input(" Masukan Sisi 3: "))

luasSegitiga = 1 / 2 * alas * Tinggi
kelilingSegitiga = sisi1 + sisi2 + sisi3

print("Luas Segitiga:  %.0f"%(luasSegitiga))
print("Keliling Segitiga: %.0f"%(kelilingSegitiga))