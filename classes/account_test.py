import BankAccount

# Main method
def main():
    
    start_balance = input("What is your account's starting balance? ")
    chequing = BankAccount.BankAccount(start_balance)
    
    deposit_amt = input("How much were you paid this month? ")
    chequing.deposit(deposit_amt)

    print(f"Your pay has been deposited. Your current balance is ${chequing.getBalance():.2f}")

    withdraw_amt = input("How much are your bills this month? ")
    chequing.withdraw(withdraw_amt)

    print(f"Now your balance is ${chequing.getBalance():.2f}")
    
main()
