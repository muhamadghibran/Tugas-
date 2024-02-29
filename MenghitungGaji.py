Gajipokok = float(input(" Masukan Gaji Pokok  : Rp. ")) 
Uangtransport = float(input(" Masukan Uang Transport Harian   : Rp. "))
Uangmakan = float(input(" Masukan Uang Makan Harian  : Rp.  "))
Tunjangan = float(input(" Masukan Tunjangan Jabatan : Rp.  "))
Honorlembur = float(input(" Masukan Honor Lembur : Rp.  "))

TotalGaji = Gajipokok - Uangtransport - Uangmakan + Tunjangan + Honorlembur

print(" Gaji Karyawan Rp : %.0f"%TotalGaji)