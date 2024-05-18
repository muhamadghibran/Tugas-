n = 5
def hasil (n):
  if n == 0:
    return 1
  else :
    return n * hasil(n-1)
  
print(hasil(n))