a = int(input("enter a number: "))
mul_5 = True if a % 5 == 0 else False
mul_7 = True if a % 7 == 0 else False

if mul_7 and mul_5:
    print(a, "is multiple of 5 & 7")
elif mul_5:
    print(a, " is multiple of 5 but not 7")
elif mul_7:
    print(a, " is multiple of 7 but not 5")
else:
    print("idiot")
