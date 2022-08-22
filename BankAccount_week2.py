class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        print("Balance: $", self.balance)
    def yield_interest(self):
        if self.balance >= 0:
            self.balance += int(self.balance * self.int_rate)

acct1 = BankAccount(.05, 100)
acct2 = BankAccount(.03, 100)

acct1.deposit(35)
acct1.deposit(35)
acct1.deposit(35)
acct1.withdraw(5)
acct1.yield_interest()
acct1.display_account_info()

acct2.deposit(10)
acct2.deposit(10)
acct2.withdraw(10)
acct2.withdraw(10)
acct2.withdraw(10)
acct2.withdraw(10)
acct2.yield_interest()
acct2.display_account_info()