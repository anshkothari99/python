class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string


reverser = StringReverser()
input_string = input("enter more than one string:")
reversed_string = reverser.reverse_words(input_string)
print(reversed_string)