# Account number should be hidden i.e. used getters and setters
from account_holder_details import AccountHolderDetails

# This represents the bank account of the account holder
class BankAccount(AccountHolderDetails):
    def __init__(self):
        super().__init__() # Inherits the Account Holder Details

    accountNumber = 2325182642
    balance = 300000



    def deposit(self):
        deposit_amount = float(input("How much would you like to deposit?\n => "))
        if deposit_amount < 0:
            print("Try again")
        else:
            self.balance += deposit_amount
        return f"Your current balance is:\n => £{self.balance}"

    def withdraw(self):
        withdrawal_amount = float(input("How much would you like to withdraw from your account?\n => "))
        if withdrawal_amount < 0:
            print("Try again")
        else:
            self.balance -= withdrawal_amount
        return f"Your current balance is:\n => £{self.balance}"



def main():

    test = BankAccount()

    print(test.deposit())
    print(test.withdraw())
    print(test.accountNumber)

if __name__ == '__main__':
    main()