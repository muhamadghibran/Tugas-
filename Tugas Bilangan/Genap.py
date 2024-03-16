def Analisis(Nomer):

  if Nomer == 0:
    return "0 (nol)"

  Positif = "positif" if Nomer > 0 else "negatif"
  Ganap = "genap" if Nomer % 2 == 0 else "ganjil"
  return f"{Nomer} ({Positif}), {Ganap}"


Nomer = float(input("Masukkan bilangan: "))

Hasil = Analisis(Nomer)
print(Hasil)
