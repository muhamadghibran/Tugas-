Nama = input("Nama: ")
TempatLahir = input("Tempat Lahir: ")
TanggalLahir = int(input("Tanggal Lahir: "))
BulanLahir = int(input("Bulan Lahir: "))
TahunLahir = int(input("Tahun Lahir: "))
NilaiInggris = float(input("Nilai Bahasa Inggris: "))
NilaiMtk = float(input("Nilai Matematika: "))
NilaiIndo = float(input("Nilai Bahasa Indonesia: "))
JenisKelamin = input("Jenis Kelamin: ")

def HitungNilai(NilaiInggris, NilaiMtk, NilaiIndo):
    return (NilaiInggris + NilaiMtk + NilaiIndo) / 3

def jurusan(NilaiRata, JenisKelamin, Umur):
    if Umur >= 25:
        return "Maaf, Anda tidak memenuhi syarat umur."
    elif NilaiRata >= 80:
        if JenisKelamin.lower() == "laki-laki":
            return "Jurusan yang direkomendasikan: Teknik Informatika"
        elif JenisKelamin.lower() == "perempuan":
            return "Jurusan yang direkomendasikan: Sistem Informasi"
    return "Jurusan yang direkomendasikan: DKV"

Umur = 2024 - TahunLahir
NilaiRata = HitungNilai(NilaiInggris, NilaiMtk, NilaiIndo)

print("Nama:", Nama)
print("Tempat Lahir: ",TempatLahir)
print("Tanggal Lahir: ",TanggalLahir, BulanLahir, TahunLahir)
print("Jenis Kelamin: ",JenisKelamin)
print("Umur: ",Umur)
print("Rata-Rata Nilai : %.2f"%NilaiRata)
print("Disarankan untuk masuk jurusan:",jurusan(NilaiRata, JenisKelamin, Umur))
