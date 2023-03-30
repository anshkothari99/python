class Years:
    def __init__(self):
        self.a = input("Enter your name: ")
        self.a = self.a.upper()
        self.b = int(input("Enter your age: "))
        self.c = 0

    def calculate(self):
        self.c = 100 - self.b + 2023

    def result(self):
        print(self.a, "you will be 100 years old in", self.c)


x = Years()
x.calculate()
x.result()
