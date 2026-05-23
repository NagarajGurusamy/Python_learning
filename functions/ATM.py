def check_balance(balance):
    print("Balance :",balance)

def deposit(balance):
    amount = int(input("Enter the deposit amount : "))
    balance += amount
    print("Deposit added succesfully")
    return balance

def withdraw(balance):
    amount = int(input("Enter the withdraw amount : "))
    if amount > balance :
        print("insufficient balance")

    else:
        balance -= amount
        print("withdrawal successfully")

    return balance

balance = 1000
atm_pin = 2345

user_pin = int(input("Enter your atm pin : "))
if atm_pin == user_pin:
    while True:
        print("\n===== ATM MENU ==== ")
        print("1. check balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. exit")

        choice = input("Enter the choice( 1 / 2 / 3 / 4) : " )

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            deposit(balance)
        elif choice == "3":
            withdraw(balance)
        elif choice == "4":
            print("Thankyou user")
            break
        else:
            print("invalid choice")

else:
    print("Wrong Pin")