def hitung_keliling(p,l):
  keliling = 2 * (p + l)
  luas = p * l
  return (keliling,luas)
p = 5
l = 3
hasil = sorted(hitung_keliling(p,l))
print(hasil)