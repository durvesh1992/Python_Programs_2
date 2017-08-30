class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def printBalance(self):
        print "Amount in Bank: ",self.balance
user1 = BankAccount()

user1.deposit(1000)
user1.printBalance()

user1.withdraw(88)
user1.printBalance()

user2 = BankAccount()
user2.deposit(2222)

user2.printBalance()
