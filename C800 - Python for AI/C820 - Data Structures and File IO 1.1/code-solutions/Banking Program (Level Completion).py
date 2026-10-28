"""
Build Your Own Banking Program (Level Completion project).

A console banking system built with object-oriented programming. Customers
can open accounts, deposit, withdraw, transfer funds, and view a history of
every transaction. It uses a BankAccount base class with SavingsAccount and
CheckingAccount subclasses, plus a Transaction class for the history.
"""


class Transaction:
    def __init__(self, kind, amount):
        self.kind = kind
        self.amount = amount

    def __str__(self):
        return self.kind + ": $" + str(self.amount)


class BankAccount:
    def __init__(self, accountNumber, holder, balance=0):
        self.accountNumber = accountNumber
        self.holder = holder
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance = self.balance + amount
        self.history.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds.")
            return
        self.balance = self.balance - amount
        self.history.append(Transaction("Withdraw", amount))

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print("Account #" + self.accountNumber + " (" + self.holder + ")")
        print("Balance: $" + str(self.balance))
        print("Transactions:")
        for transaction in self.history:
            print("  " + str(transaction))


class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, holder, balance=0, rate=0.05):
        BankAccount.__init__(self, accountNumber, holder, balance)
        self.rate = rate

    def apply_interest(self):
        interest = self.balance * self.rate
        self.balance = self.balance + interest
        self.history.append(Transaction("Interest", round(interest, 2)))


class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, holder, balance=0):
        BankAccount.__init__(self, accountNumber, holder, balance)


def transfer(fromAccount, toAccount, amount):
    if amount > fromAccount.get_balance():
        print("Not enough funds to transfer.")
        return
    fromAccount.withdraw(amount)
    toAccount.deposit(amount)
    print("Transferred $" + str(amount) + " from " + fromAccount.holder + " to " + toAccount.holder)


def main():
    savings = SavingsAccount("S100", "Alex", 500)
    checking = CheckingAccount("C200", "Alex", 200)
    accounts = {"S100": savings, "C200": checking}

    option = 0
    while option != 6:
        print("\n===== My Bank =====")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Transfer")
        print("4) Apply interest to savings")
        print("5) View account info")
        print("6) Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            account = accounts[input("Account number: ")]
            account.deposit(float(input("Amount: ")))
        elif option == 2:
            account = accounts[input("Account number: ")]
            account.withdraw(float(input("Amount: ")))
        elif option == 3:
            transfer(accounts[input("From account: ")],
                     accounts[input("To account: ")],
                     float(input("Amount: ")))
        elif option == 4:
            savings.apply_interest()
            print("Interest applied. New balance: $" + str(savings.get_balance()))
        elif option == 5:
            accounts[input("Account number: ")].display_account_info()
        elif option == 6:
            print("Thank you for banking with us!")
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
