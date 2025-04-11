print("-------------------------------------------------------------------------------------------------")

import time
# Banking Program
"""  
    1. Check the balance
    2. Deposit money
    3. Withdraw money
    4. Quit the program
"""
print("-------------------  ABC Bank ATM  -------------------")
print("          Welcome to our Banking                  ")
print("-------------------------------------------------------")

def show_menu():
    print("________________________")
    print("1. Check the balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Quit the program")
    print("________________________")

def check_balance(balance):
    print()
    print("***********************************************")
    print(f"Your current balance is ${balance:.2f}")
    print("***********************************************")
    time.sleep(2)

def deposit_money():
    print()
    print("***********************************************")
    deposit_amount = float(input("Enter the amount to deposit: $"))
    print("***********************************************")
    if deposit_amount > 0:
        print()
        print("=================================================")
        print(f"Depositing ${deposit_amount:.2f} to your account")
        print("=================================================")
        return deposit_amount
    else:
        print()
        print("=============================================")
        print("Invalid amount. Please enter a valid amount.")
        print("=============================================")
        return 0
    time.sleep(2)

def withdraw_money(balance):
    print()
    print("***********************************************")
    withdraw_amount = float(input("Enter the amount to withdraw: $"))
    print("***********************************************")
    if balance == 0:
        print()
        print("=========================================================================")
        print("No amount withdrawn from your account!, You're still broke as *** Bro!😆 ")
        print("=========================================================================")
        time.sleep(4)
        return 0
    elif balance > withdraw_amount:
        print()
        print("=====================================================")
        print(f"Withdrawing ${withdraw_amount:.2f} from your account")
        print("=====================================================")
        return withdraw_amount
    else:
        print()
        print("=============================================")
        print("Invalid amount. Please enter a valid amount.")
        print("=============================================")
        return 0
    time.sleep(2)

def main():
  balance = 0
  is_running = True

  while is_running:
      show_menu()
      choice =  input("Enter your choice (1-4): ")
      if choice == "1":
          check_balance(balance)
      elif choice == "2":
          balance += deposit_money()
      elif choice == "3":
          balance -= withdraw_money(balance)
      elif choice == "4":
          print()
          print("=============================================================")
          print("| Thank you for using our Banking System. Have a great day! |")
          print("=============================================================")
          is_running = False
      else:
          print()
          print("===========================================================")
          print("| Invalid choice. Please enter a number between 1 and 4.  |")
          print("===========================================================")
          time.sleep(2)



print()
print("-------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()


