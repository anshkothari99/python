a = input("Enter a string: ")
a = a.lower()
vowels = "aeiou"
counts = {}

for vowel in vowels:
    count = a.count(vowel)
    counts[vowel] = count

print("Counts of each vowel in the string:")
for m, n in counts.items():
    print(m, ":", n)
