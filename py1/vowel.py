a = input("enter your name")
b = len(a)
vowel = 0
con = 0
for i in range(b):
    if a[i] in ('a', 'e', 'i', 'o', 'u'):
        vowel += 1
    else:
        con += 1

print(vowel, con)
