def count_line():
    a = open("a.txt")
    count_line = 0
    for i in a:
        count_line += 1
    print("total lines in file :", count_line)
    a.close()

def count_char():
    a = open("a.txt")
    count_char = 0
    for i in a:
        for j in i:
            count_char += 1
    print("total character in file :",count_char)
    a.close()


def count_word():
    a = open("a.txt")
    b = a.read()
    c = b.split()
    print("total words in file :", len(c))
    a.close()

count_line()
count_word()
count_char()
