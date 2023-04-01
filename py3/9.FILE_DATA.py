a = open("orignal.txt")
counts = {}
total_string=''
for i in a:
    for j in i:
        total_string = total_string+j
a.close()

vowels = "abcdefghijklmnopqrstuvwxyz"

for i in vowels:
    count = total_string.count(i)
    counts[i] = count

print("Counts of each char in the string:")
for m, n in counts.items():
    print(m, ":", n)