# task4.py

class BankAccount:
    
    def __init__(self, initial_balance=0.0):
       """инициализация банковского счета."""
       self._balance = initial_balance
       self._transactions = []

    @property
    def balance(self):
      
       return self._balance

    def deposit(self, amount):
       """вносит деньги на счет и логирует операцию."""
       if amount > 0:
           self._balance += amount
           self._transactions.append(f"депозит: {amount}")
           return True
       return False

    def withdraw(self, amount):
       """снимает деньги со счета и логирует операцию."""
       if amount > 0 and amount <= self._balance:
           self._balance -= amount
           self._transactions.append(f"снятие: {amount}")
           return True
       return False

if __name__ == "__main__":
   account = BankAccount()
   account.deposit(100)
   account.withdraw(30)
   
   print(f"текущий баланс: {account.balance}")
