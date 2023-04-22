import time


def drama():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)


class BankAccount:
    def __init__(self):
        self.a = 0
        self.pin = 1234
        self.balance = 0
        self.st = time.time()
        self.td = self.st - time.time()
        self.fp = open("balance.txt", "w")
        self.fp.close()
        self.text = '   '

    def get_balance(self):
        print("Your current balance is: ", self.balance)

    def deposit(self):
        self.fp = open("balance.txt", "a")
        self.a = int(input("Enter an amount: "))
        self.balance = self.balance + self.a
        print("Your updated balance is: ", self.balance)

        self.fp.writelines('deposited:' + str(self.a) + ' balance: ' + str(self.balance) + '\n')
        self.fp.close()

    def withdraw(self):
        self.fp = open("balance.txt", "a")
        self.a = int(input("Enter an amount: "))
        if self.a > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= self.a
            print("Your updated balance is: ", self.balance)
            self.fp.writelines('Withdraw:' + str(self.a) + ' balance: ' + str(self.balance) + '\n')
            self.fp.close()

    def change_pin(self):
        new_pin = int(input("enter a new pin (only numerical): "))
        self.pin = new_pin
        print("your pin has been updated ")

    def interest(self):
        # if round(self.td)%10 == 0:

        print("Old balance:", self.balance, "\nInterest earned:", round((self.balance * 0.06)), "New balance:",
              self.balance + (self.balance * .06))
        self.balance = self.balance + round((self.balance * 0.06))
        self.fp = open("balance.txt", "a")
        self.fp.writelines('Interest deposited:' + str(self.a) + ' balance: ' + str(self.balance) + '\n')
        self.fp.close()


a = BankAccount()
sys = True
while sys:
    print("welcome tho AKB\nplease enter your pin to get access")
    u_pin = int(input("PIN: "))
    if u_pin == a.pin:
        print("entered pin was correct :)")
        print("you are in the bank account\n\nEnter codes for your task\n")
        print(
            "For current balance:1\nFor deposit:2\nFor withdraw:3\nUpdate Interest:7 \nLogout:0\nShut down:9\nChange "
            "Pin:8\n")
        p = open("balance.txt", "a")
        p.writelines("Log in time- " + str(time.time()))
        p.close()
        access = True
    else:
        print("entered pin was incorrect ;(")
        access = False

    while access:
        b = int(input("input: "))
        if b == 1:
            a.get_balance()
        elif b == 2:
            a.deposit()
        elif b == 3:
            a.withdraw()
        elif b == 0:
            drama()
            print("logging out buddy")
            time.sleep(1)
            print("see you soon ;P\n")
            break
        elif b == 9:

            print("logging out")
            drama()
            print("i am dying bye bye")
            access = False
            sys = False
        elif b == 8:
            a.change_pin()
            drama()
            print("success")
        elif b == 7:
            a.interest()
        else:
            print("WRONG INPUT SIR JI ;)")
            print("you are in the bank account\n\nEnter codes for your task\n")
            print("For current balance:1\nFor deposit:2\nFor withdraw:3\nLogout:0\nShut down:9\nChange Pin:8\n")
