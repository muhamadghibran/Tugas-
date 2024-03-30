for i in range(4):
    for j in range(5):
        if (i + j) % 2 == 0:
            print('A', end=' ')
        else:
            print('B', end=' ')
    print()
