for i in range(5, 0, -1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print('O', end=' ')
        else:
            print('S', end=' ')
    print()
