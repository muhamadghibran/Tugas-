Nama = "Sukabumi"

for i in range(5):
  for j in range(len(Nama)):
    if(j>=i-1) and (j<10-i):
      print(Nama [j], end="")
    else:
      print("*", end="")
  print()