def cek_kelayakan(jenis_kelamin, berat_badan, tinggi_badan, usia, nilai_akademis, memiliki_skill, memiliki_cacat):
    if memiliki_cacat:
        return False

    if jenis_kelamin == "perempuan":
        if 45 <= berat_badan <= 50 and tinggi_badan >= 165 and usia < 20:
            return True
        else:
            return False

    elif jenis_kelamin == "laki-laki":
        if berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25:
            return True
        else:
            return False

    elif nilai_akademis >= 90 and usia < 30:
        return True

    elif memiliki_skill in ["menembak", "memanah", "berkuda"]:
        return True

    else:
        return False


def main():
    print("Program Kelayakan Anggota Organisasi X ")
    print("Silakan isi data berikut untuk mengetahui kelayakan Anda:")
    jenis_kelamin = input("Jenis Kelamin (laki-laki / perempuan): ")
    berat_badan = float(input("Berat Badan (kg): "))
    tinggi_badan = int(input("Tinggi Badan (cm): "))
    usia = int(input("Usia (tahun): "))
    nilai_akademis = int(input("Nilai Akademis (0-100): "))
    memiliki_skill = input("Apakah Anda memiliki skill menembak, memanah, atau berkuda? (ya / tidak): ")
    memiliki_cacat = input("Apakah Anda memiliki cacat anggota tubuh? (ya / tidak): ")

    if memiliki_skill.lower() == "ya":
        memiliki_skill = True
    else:
        memiliki_skill = False

    if memiliki_cacat.lower() == "ya":
        memiliki_cacat = True
    else:
        memiliki_cacat = False

    if cek_kelayakan(jenis_kelamin, berat_badan, tinggi_badan, usia, nilai_akademis, memiliki_skill, memiliki_cacat):
        print("Selamat! Anda memenuhi kelayakan untuk menjadi anggota Organisasi X.")
    else:
        print("Maaf, Anda tidak memenuhi kelayakan untuk menjadi anggota Organisasi X.")


if __name__ == "__main__":
    main()