# The SavingsAccount class extends the BankAccount class

import BankAccount

class SavingsAccount(BankAccount):
    
    def __init__(self, start_balance):
        super().__init__(start_balance)
        
    def add_monthly_int_rate(self, annual_rate):
        monthly_int_rate = annual_rate / 12.0
        monthly_interest = self.balance * monthly_int_rate
        self.balance += monthly_interest
    
