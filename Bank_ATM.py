class Account:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def display_transaction_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.accounts = {} 

    def create_account(self, account_number, pin):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            new_account = Account(account_number, pin)
            self.accounts[account_number] = new_account
            print("Account created successfully!")

    def login(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print("Login successful!")
            return account
        else:
            print("Invalid account number or PIN")
            return None

    def perform_transactions(self, account):
        while True:
            print("\nATM Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.check_balance()
            elif choice == '4':
                account.display_transaction_history()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def start(self):
        while True:
            print("\nWelcome to the ATM!")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                account_number = input("Enter account number: ")
                pin = input("Enter PIN: ")
                self.create_account(account_number, pin)
            elif choice == '2':
                account_number = input("Enter account number: ")
                pin = input("Enter PIN: ")
                account = self.login(account_number, pin)
                if account:
                    self.perform_transactions(account)
            elif choice == '3':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":  
    atm = ATM()
    atm.start()
