class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds exist."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Return the current balance as a formatted string."""
        return f"Current Balance: ${self.account_balance:.2f}"



import sys
from bank_account import BankAccount

def main():
    # Example starting balance
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        # Use `display_balance` to ensure the format matches
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
