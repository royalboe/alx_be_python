class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return None
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        return None
    

    

    