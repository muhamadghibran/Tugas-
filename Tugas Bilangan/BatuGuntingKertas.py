import random

pilihan = ["batu", "gunting", "kertas"]

def pilihan_pemain1():
  while True:
    pilihan_pemain1 = input("Masukkan pilihan Anda (batu, gunting, kertas): ")
    if pilihan_pemain1 in pilihan:
      break
    else:
      print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")
  return pilihan_pemain1

def pilihan_pemain2():
  pilihan_pemain2 = random.choice(pilihan)
  return pilihan_pemain2

def menentukan_pemenang(pilihan_pemain1, pilihan_pemain2):
  if pilihan_pemain1 == pilihan_pemain2:
    pemenang = "Seri"
  elif pilihan_pemain1 == "batu":
    if pilihan_pemain2 == "gunting":
      pemenang = "Pemain 1"
    else:
      pemenang = "Pemain 2"
  elif pilihan_pemain1 == "gunting":
    if pilihan_pemain2 == "batu":
      pemenang = "Pemain 2"
    else:
      pemenang = "Pemain 1"
  elif pilihan_pemain1 == "kertas":
    if pilihan_pemain2 == "batu":
      pemenang = "Pemain 1"
    else:
      pemenang = "Pemain 2"
  return pemenang

while True:
  pilihan_pemain1 = pilihan_pemain1()
  pilihan_pemain2 = pilihan_pemain2()

  pemenang = menentukan_pemenang(pilihan_pemain1, pilihan_pemain2)

  print("Pemain 1 memilih: ", pilihan_pemain1)
  print("Pemain 2 memilih: ", pilihan_pemain2)
  print("Pemenangnya adalah : ",pemenang)
  
  lagi = input("Apakah ingin bermain lagi? (y/n) ")
  if lagi == "y":
    break
