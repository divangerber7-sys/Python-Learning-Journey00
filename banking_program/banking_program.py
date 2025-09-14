# Python Banking Program

def show_balance(balance):
    print("****************************************")
    print(f"Your balance is R {balance:.2f}")
    print("****************************************")

def deposit():
    print("****************************************")
    amount = float(input("Please enter the amount to deposit: "))
    print("****************************************")

    if amount < 0:
        print("****************************************")
        print("Please enter a positive number")
        print("****************************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************************************")
    amount = float(input("Please enter the amount to withdraw: "))
    print("****************************************")

    if amount > balance:
        print("****************************************")
        print("Insufficient funds")
        print("****************************************")
        return 0
    elif amount < 0:
        print("****************************************")
        print("Please enter a valid amount")
        print("****************************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************************************")
        print("Aloha and Welcome to the Banking Program")
        print("****************************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************************************")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("****************************************")
            print("I am sorry but that is an Invalid choice")
            print("****************************************")
            break

    print("****************************************")
    print("Thank you for using the Banking Program\nHave a good day!\nMahalo!")
    print("****************************************")

if __name__ == "__main__":
    main()
