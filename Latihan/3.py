skor = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh'", 39]]
hasil = []
nama = []

for siswa in skor :
  hasil.append(siswa[1])
a = sorted(hasil)
b = a[1]

for siswa in skor :
  if siswa[1] == b :
    nama.append(siswa[0])
    
c = sorted(nama)
for jawaban in c :
  print(jawaban)