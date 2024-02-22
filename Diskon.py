uang_belanja = float(input(" Masukan Nomainal Uang Belanja : "))
total_belanja = float(input(" Masukan Nomainal Total Belanja : "))

if total_belanja > 70000:
  diskon = total_belanja *(10/100)
else : diskon = 0

print(" Anda mendapatkan diskon : %.0f" %diskon)

setelah_diskon = total_belanja - diskon
Kembalian = uang_belanja - setelah_diskon

print(" uang kembalian : %.0f"%Kembalian)