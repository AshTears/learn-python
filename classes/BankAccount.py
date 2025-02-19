# The BankAccount class simulates a bank account

class BankAccount:

    balance = 0.0
    
    # The constructor sets the starting balance
    def __init__(self, start_balance):
        self.balance = float(start_balance)
        print(f"The account balance is ${self.balance:.2f}")
        
    # The deposit method makes a deposit into the account.
    # @param amount The amount to add to the balance field.
    def deposit(self, amount):
        self.balance += float(amount)
        
    # The withdraw method withdraws an amount from the account.
    # @param amount The amount to subtract from the balance field.
    def withdraw(self, amount):
        self.balance -= float(amount)
        
    # The setBalance method sets the account balance
    # @param The value to store in the balance field
    def setBalance(self, bal):
        self.balance = float(bal)
    
    # The getBalance method returns the account balance
    # @return The value in the balance field.
    def getBalance(self):
        return self.balance
        

