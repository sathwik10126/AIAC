class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid amount. Please enter a positive value."
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid amount. Please enter a positive value."
    
    def check_balance(self):
        return f"Current balance: ${self.balance}"

# Example usage
if __name__ == "__main__":
    # Get user input for account creation
    print("=== Bank Account System ===")
    name = input("Enter account holder name: ")
    try:
        initial_balance = float(input("Enter initial balance: $"))
    except ValueError:
        print("Invalid balance. Setting to $0.")
        initial_balance = 0
    
    # Create a bank account
    account = BankAccount(name, initial_balance)
    print(f"\nWelcome, {account.name}!")
    print(account.check_balance())
    
    # Main menu loop
    while True:
        print("\n=== Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            print(account.check_balance())
        
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                print(account.deposit(amount))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == "4":
            print(f"Thank you for using our bank, {account.name}!")
            print(f"Final balance: ${account.balance}")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    