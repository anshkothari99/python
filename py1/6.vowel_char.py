def vowelcheck(ch):
    if ch in ('a', 'e', 'i', 'o', 'u'):
        return True

    else:
        return False


a = input("enter a character")
print('Is (', a, ') a vowel:', vowelcheck(a))
