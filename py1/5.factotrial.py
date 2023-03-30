a = int(input("enter a number \n"))
b = 1
for i in range(a + 1):
    if i != 0:
        b *= i

print("factorial of", a, "is", b)
