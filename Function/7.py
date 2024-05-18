def Cekpalindrom(kalimat):
    if kalimat == kalimat[::-1]:
        return f'"{kalimat}" adalah palindrom'
    else:
        return f'"{kalimat}" bukan palindrom'

print(Cekpalindrom("level"))
