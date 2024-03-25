kolom = 6

for i in range(kolom, 0, -1):
    for j in range(i, 1, -1):
        if j % 2 == 0:
            print("2", end=" ")
        else:
            print("3", end=" ")
    print()
