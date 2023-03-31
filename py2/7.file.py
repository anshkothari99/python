a=open("a.txt")
b=list(a)
c=reversed(b)
for line in c:

    print(line.rstrip())
