import json

try:
    with open("./#01 - Simple ATM/balance.json") as f:
        balance = json.load(f)["balance"]
except:
    balance = 10000

def save_bal(balance):
    with open("./#01 - Simple ATM/balance.json", "w") as file:
        json.dump({"balance": balance}, file)

def menu():
    print("""
    1 -> Check Balance
    2 -> Withdraw Balance
    3 -> Deposit Balance
    4 -> Exit
    """)

while True:
    menu()
    try:
        ch = int(input("Enter your choice (1-4): "))
        match(ch):
            case 1:
                print(f"Your balance: {balance:.2f}")

            case 2:
                withdraw = float(input("Enter an amount to withdraw: "))
                if (withdraw == 0):
                    print("Thank you for using our ATM")
                elif (withdraw < 0):
                    print("Amount must be positive")
                elif (withdraw > balance):
                    print(f"Insufficient funds | Your balance: Rs.{balance:.2f}")
                else:
                    balance -= withdraw
                    save_bal(balance)
                    print(f"Withdrawn successful: New balance Rs.{balance:.2f}")

            case 3:
                deposit = float(input("Enter an amount to deposit: "))
                if (deposit == 0):
                    print("Thank you for using our ATM")
                elif (deposit < 0):
                    print("Amount must be positive")
                else:
                    balance += deposit
                    save_bal(balance)
                    print(f"Deposit successful: New balance Rs.{balance:.2f}")

            case 4:
                print("Thank you for using our ATM. Goodbye!")
                break  # Better than exit()

            case _:
                print("Invalid option!! Try again")
        
    
    except ValueError:
        print("Invalid Input")
    
    except Exception as e:
        print("Something went wrong")
