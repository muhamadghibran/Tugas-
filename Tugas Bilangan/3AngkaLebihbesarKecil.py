Bilangan1= float(input("Masukkan bilangan pertama: "))
Bilangan2 = float(input("Masukkan bilangan kedua: "))
Bilangan3 = float(input("Masukkan bilangan ketiga: "))

Semua = Bilangan1 == Bilangan2 and Bilangan1 == Bilangan3
Dua = None

if Bilangan1 > Bilangan2 and Bilangan1 > Bilangan3:
    if Bilangan1 == Bilangan2 or Bilangan1 == Bilangan3:
       Dua = "dua bilangan sama dengan yang terbesar"
    else:
        
        Dua = Bilangan1
elif Bilangan2 > Bilangan1 and Bilangan2 > Bilangan3:
    if Bilangan2 == Bilangan1 or Bilangan2 == Bilangan3:
        Dua = "dua bilangan sama dengan yang terbesar"
    else:
        Dua = Bilangan2
else:
    pass


if Semua:
    print("Semua bilangan sama besar.")
elif Dua is not None:
    if isinstance(Dua, str):
        print(Dua)
    else:
        print("lebih besar dari 2 bilangan lainnya.%.0f"%Dua)
else:
    print("lebih besar dari 2 bilangan lainnya.%.0f"%Bilangan3)