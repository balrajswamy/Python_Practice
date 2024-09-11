class InsufficientBalanceException(Exception):
    def __init__(self, message, balance, amount):
        super().__init__(message)
        self.balance = balance
        self.amount = amount
        #self.message = message

    def __str__(self):
        return f"{self.args[0]} | Current Balance: {self.balance}, Withdrawal Amount: {self.amount}"


#ob = InsufficientBalanceException("Hello",300,200)
#print(ob)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException("Insufficient balance for this withdrawal", self.balance, amount)
        self.balance -= amount
        return self.balance

# Example Usage
try:
    account = BankAccount(1500)  # Initial balance of $500
    balance = account.withdraw(1600)       # Trying to withdraw $600
    print(f"Balance Amount:\t{balance}")
except InsufficientBalanceException as e:
    print(e)
