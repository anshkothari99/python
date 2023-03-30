count = 1
for i in range(1, 5):
    for j in range(count):
        if i % 2 == 1:
            print("*", end="")
        else:
            print("?", end="")
    print()
    count += 1
