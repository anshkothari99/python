user_name = input("Enter your name: ")
user_name = user_name.lower()


def count():
    b = len(user_name)
    str_len = 0
    for i in range(b):
        str_len += 1
    return str_len


def vowel_calc():
    vowel = 0
    con = 0
    for i in range(len(user_name)):
        if user_name[i] in ('a', 'e', 'i', 'o', 'u'):
            vowel += 1
        elif user_name[i] == ' ':
            pass
        else:
            con += 1
    result = (vowel, con)
    return result


print('\nTOTAL CHARACTER ', count(),
      '\n\n`fun fact a space is a characterIt takes up as much memory as any other character.`')
print('\nTOTAL VOWEL ARE ', vowel_calc()[0], '\nTOTAL CON ARE ', vowel_calc()[1])
