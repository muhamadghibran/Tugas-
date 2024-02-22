jerukperkilo = 15000
apelperkilo = 30000
manggaperkilo = 20000
manggisperkilo = 7000
durianperkilo = 50000

jeruk = 3
apel = 2
mangga = 0
manggis = 5
durian = 2

jumlahjeruk = jerukperkilo * jeruk
jumlahapel = apelperkilo * apel
jumlahmangga = manggaperkilo * mangga
jumlahmanggis = manggisperkilo * manggis
jumlahdurian = durianperkilo * durian
TotalJumlah = jumlahjeruk + jumlahapel + jumlahmangga + jumlahmanggis + jumlahdurian

print(" Total Yang Harus di bayar : ")
print(" 3 kilo jeruk : %.0f"%jumlahjeruk)
print(" 2 kilo apel : %.0f"%jumlahapel)
print(" 0 kilo mangga : %.0f"%jumlahmangga)
print(" 5 kilo manggis : %.0f"%jumlahmanggis)
print(" 3 kilo durian : %.0f"%jumlahdurian)
print(" Total Belanja : %.0f"%TotalJumlah)