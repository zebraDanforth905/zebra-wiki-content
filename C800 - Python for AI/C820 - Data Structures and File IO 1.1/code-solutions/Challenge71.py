class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited $" + str(amount))
        else:
            print("You can only deposit a positive amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in the account.")
        else:
            self.balance = self.balance - amount
            print("Withdrew $" + str(amount))

    def __str__(self):
        return self.owner + "'s account: $" + str(self.balance)


account = BankAccount("Sam", 100)

option = 0
while option != 4:
    print("\n" + str(account))
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Check balance")
    print("4) Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        account.deposit(int(input("How much to deposit? ")))
    elif option == 2:
        account.withdraw(int(input("How much to withdraw? ")))
    elif option == 3:
        print("Your balance is $" + str(account.balance))
    elif option == 4:
        print("Goodbye!")
    else:
        print("Invalid option!")
