import time

def atm_machine():
    print("Please insert your CARD")
    time.sleep(5)
    
    password = 1234
    balance = 5000
    
    try:
        pin = int(input("Enter your ATM pin: "))
    except ValueError:
        print("Invalid pin format")
        return
    
    if pin == password:
        while True:
            print("""
                  1 == Balance Inquiry
                  2 == Withdraw Balance
                  3 == Deposit Balance
                  4 == Exit
                  """)
            
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Please enter a valid option")
                continue
            
            if option == 1:
                print(f"Your current balance is {balance}")
            
            elif option == 2:
                try:
                    withdraw_amount = int(input("Please enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount format")
                    continue
                
                if withdraw_amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"Your current balance is {balance}")
            
            elif option == 3:
                try:
                    deposit_amount = int(input("Please enter your deposit amount: "))
                except ValueError:
                    print("Invalid amount format")
                    continue
                
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account")
                print(f"Your updated balance is {balance}")
            
            elif option == 4:
                print("Thank you for using our service!")
                break
            
            else:
                print("Invalid option, please try again")
    else:
        print("Wrong pin, please try again")

atm_machine()

