a = 1
b = 1

for i in range(10):
    print(a, end=" ")
    if i < 2:
        a += 1
    else:
        temp = a
        a += b
        b = temp
