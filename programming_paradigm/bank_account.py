# bank_account.py

Class BankAccount:
     def __init__(self, initial_balance=0):
          self.__account_balance = initial_balance  # Private attribute

     def deposit(self,amount):
         if amount > 0:
           self.__account_balance += amount

     def withdraw(self, amount):
         if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
         return False

     def display_balance(self):
         print("Current Balance: ${self.__account_balance}")

 # main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  #Example starting balance

    if len(sys.argv) < 2:
         print("Usage: python main-0.py <command>:<amount>")
         print("Commands: deposit, withdraw, display")
         sys.exit(1)
      
    try:
          command_parts = sys,argv[1].split(':')
          command = command_parts[0]
          amount = float(command_parts[1]) if len(command_parts) > 1 else None

           if command == "deposit" and amount is not None:
              account.deposit(amount)
              print(f"Deposited: ${amount}")
           elif command == "withdraw" and amount is not None:
                if account.withdraw(amount):
                   print("Insufficient funds.")
           elif command == "display":
                account.display_balance()
           else:
                print("Invalid command")
    except ValueError:
       print("Invalid amount. Please enter a numeric value.")

if __name__ == "__main__":
     main()
  


                  
  
      
  
      
       
