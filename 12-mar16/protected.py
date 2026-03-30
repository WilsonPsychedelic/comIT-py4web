class BankAccount:
    def __init__(self, balance):
        self.public_balance = balance           # Public
        self._internal_info = "Internal use"    # Protected by convention
        self.__account_number = "12345"         # "Private" via name mangling

# Access examples:
account = BankAccount(100)
print(account.public_balance) # Accessible: 100

# Convention suggests not accessing these directly:
print(account._internal_info) # Accessible, but discouraged: Internal use

# Direct access to __account_number fails
try:
    print(account.__account_number)
except AttributeError as e:
    print(f"Error accessing __account_number directly: {e}") 

# Access via name mangling (possible, but strongly discouraged):
print(account._BankAccount__account_number) # Accessible: 12345
