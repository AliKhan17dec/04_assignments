class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, customer):
        self.customer = customer

    def show(self):
        print(f"Customer: {self.customer}, Bank: {Bank.bank_name}")

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Creating instances
customer1 = Bank("Ali")
customer2 = Bank("Sara")

# Displaying initial bank name
customer1.show()
customer2.show()

# Changing the bank name using class method
Bank.change_bank_name("Global Bank")

# Displaying updated bank name
customer1.show()
customer2.show()
