print("ansh 033")
f1 = open("orignal.txt", "r")
contents = f1.read()

f2= open("dublicate.txt", "w")
f2.write(contents)

print(f"Contents of orignal file have been copied to dublicate.")
