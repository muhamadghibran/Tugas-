def konversi_suhu(suhu, skala_awal):
  
  if skala_awal not in ("C", "F"):
    raise ValueError("Skala awal tidak valid.")

  if skala_awal == "C":
    return (suhu * 9/5) + 32
  else:
    return (suhu - 32) * 5/9

suhu = float(input("Masukkan suhu: "))
skala_awal = input("Masukkan skala awal (C/F): ")

try:
  skala_akhir = "Fahrenheit" if skala_awal == "C" else "Celsius"
  suhu_konversi = konversi_suhu(suhu, skala_awal)
  print(f"{suhu} derajat {skala_awal} sama dengan {suhu_konversi:.2f} derajat {skala_akhir}")
except ValueError as Eror:
  print(Eror)

