class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    # Property prevents users from editing their details
    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def age(self):
        return self.__age

    def display_account_details(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")

# Testing code
# me = AccountHolderDetails("Matt Sokol", "27 Baker Street, Bravoos", "22")
#
# print(me.display())