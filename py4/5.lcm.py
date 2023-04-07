def gcd_lcm(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    gcd = num1

    lcm = (num1 * num2) // gcd
    return gcd, lcm

num1 = int(input("enter first no."))
num2 = int(input("enter second no."))
result = gcd_lcm(num1, num2)
print("GCD of {} and {} is {}".format(num1, num2, result[0]))
print("LCM of {} and {} is {}".format(num1, num2, result[1]))
