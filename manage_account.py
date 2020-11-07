from bank_account import MyAccount

class ManageAccount(MyAccount):
    def __init__(self, account_number, balance, name, address, age):
        super().__init__(account_number, balance, name, address, age) # Inherits everything from the bank account class
        self.display()

    def display(self):
        print("""
        MENU
        Available Options:
        1. Account Holder Details - Display your personal information
        2. Bank Account Details - Display your account number and balance
        3. Deposit - Deposit money into your account
        4. Withdraw - Withdraw money from your account
        """)

        self.continue_displaying = True
        while self.continue_displaying:
            self.action()

    def action(self):
        selection = input("Please choose one of the available options in the menu --> (1,2,3,4).\n "
                          "(Or type 'exit' to stop the program)\n-> ").lower()

        if '1' in selection:
            self.display_account_details()

        elif '2' in selection:
            self.display_bank_details()

        elif '3' in selection:
            self.deposit()

        elif '4' in selection:
            self.withdraw()

        elif "exit" in selection:
            self.continue_displaying = False

        else:
            print("Please choose an action displayed on the menu")

        return


def main():

    user = ManageAccount(73763632, 200000, "Matt Sokol", "27 Baker Street, Bravoos", "22")

if __name__ == '__main__':
    main()