def skorToBobot(skor):
  if skor >= 85:
    return 4.0
  elif skor >= 80:
    return 3.75
  elif skor >= 75:
    return 3.5
  elif skor >= 70:
    return 3.25
  elif skor >= 65:
    return 3.0
  elif skor >= 60:
    return 2.75
  elif skor >= 55:
    return 2.5
  elif skor >= 50:
    return 2.25
  else:
    return 2.0


algoritma = float(input("Masukkan nilai Algoritma: "))
nilai_kredit_algoritma = int(input("Masukkan SKS Algoritma: "))

objek = float(input("Masukkan nilai Perancangan Objek: "))
nilai_kredit_objek = int(input("Masukkan SKS Perancangan Objek: "))

kalkulus = float(input("Masukkan nilai Kalkulus: "))
nilai_kredit_kalkulus = int(input("Masukkan SKS Kalkulus: "))

etika = float(input("Masukkan nilai Etika Profesi: "))
nilai_kredit_etika = int(input("Masukkan SKS Etika Profesi: "))

database = float(input("Masukkan nilai Databases: "))
nilai_kredit_database = int(input("Masukkan SKS Databases: "))

english = float(input("Masukkan nilai Bahasa Inggris: "))
nilai_kredit_english = int(input("Masukkan SKS Bahasa Inggris: "))


total_skor = (
  skorToBobot(algoritma) * nilai_kredit_algoritma +
  skorToBobot(objek) * nilai_kredit_objek +
  skorToBobot(kalkulus) * nilai_kredit_kalkulus +
  skorToBobot(etika) * nilai_kredit_etika +
  skorToBobot(database) * nilai_kredit_database +
  skorToBobot(english) * nilai_kredit_english
)

total_kredit = (
  nilai_kredit_algoritma +
  nilai_kredit_objek +
  nilai_kredit_kalkulus +
  nilai_kredit_etika +
  nilai_kredit_database +
  nilai_kredit_english
)


ipk = total_skor / total_kredit


print("IPK Anda semester ini adalah: %.2f"%ipk)
