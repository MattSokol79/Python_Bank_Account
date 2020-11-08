# Account number should be hidden i.e. used getters and setters
from account_holder_details import AccountHolderDetails

# This represents the bank account of the account holder
class MyAccount(AccountHolderDetails):
    def __init__(self, account_number, balance, name, address, age):
        super().__init__(name, address, age) # Inherits the Account Holder Details
        self.__account_number = account_number
        self.__balance = balance
        self.bank_fees_deducted = 0.95

    # Prevents editing of the account number
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return float("{:.2f}".format(self.__balance))

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self):
        deposit_amount = float(input("How much would you like to deposit?\n => "))
        if deposit_amount <= 0:
            output = "Please try again"
        else:
            self.balance += deposit_amount
            output = f"Your current balance is:\n => £{self.balance}"
        return output

    def withdraw(self):
        withdrawal_amount = float(input("How much would you like to withdraw from your account?\n => "))
        if withdrawal_amount <= 0:
            output = "Please try again"
        else:
            self.balance -= withdrawal_amount
            print(f"You have withdrawn £{withdrawal_amount} from your account.")
            print("=" * 20)
            output = f"After applying 5% charge in bank fees, your current balance is:\n => £{self.balance * self.bank_fees_deducted}"
        return output

    def display_bank_details(self):
        print("")
        print("=" * 20)
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: £{self.balance}")
        print("=" * 20)



def main():

    test = MyAccount(73763632, 200000, "Matt Sokol", "27 Baker Street, Bravoos", "22")

    #print(test.deposit())
    #print(test.withdraw())
    #print(test.account_number)
    #print(test.display())

if __name__ == '__main__':
    main()