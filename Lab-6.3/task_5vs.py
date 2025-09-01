class bank_account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance
    def get_account_holder(self):
        return self.account_holder
# Example usage
def main():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = bank_account(account_holder, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            print(f"Current Balance: ${account.get_balance():.2f}")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()