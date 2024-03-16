def hitung_luas_keliling_segitiga(a, b, c):

  s = (a + b + c) / 2

  luas = (s * (s - a) * (s - b) * (s - c))
  
  keliling = a + b + c

  return luas, keliling

a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))

luas, keliling = hitung_luas_keliling_segitiga(a, b, c)

print("Luas segitiga:%.2f"%luas)
print("Keliling segitiga: %.2f"%keliling)
