a = open("a.txt")
counts = {}

for i in a:
    for j in i:
        count = a.count(i)
        counts[i] = count
a.close()

vowels = "aeiou"

for i in vowels:
    count = a.count(i)
    counts[i] = count

print("Counts of each vowel in the string:")
for m, n in counts.items():
    print(m, ":", n)