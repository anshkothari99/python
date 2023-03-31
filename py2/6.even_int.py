for i in range(100, 201):
    b = 0
    a = str(i)
    for j in a:
        m = int(j)
        b += m
    print(i, ":", b, end='')
    print()
