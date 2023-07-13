import main


def menu():
    print("***** Bank Menu *****")
    print("1. Create an account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View balance")
    print("5. Exit")

    bank = None

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender: ")
            bank = main.Bank(name, age, gender)
            print("Account created successfully!")

        elif choice == "2":
            if bank:
                amount = float(input("Enter the amount to deposit: "))
                bank.deposit(amount)
            else:
                print("No account found. Please create an account first.")

        elif choice == "3":
            if bank:
                amount = float(input("Enter the amount to withdraw: "))
                bank.withdraw(amount)
            else:
                print("No account found. Please create an account first.")

        elif choice == "4":
            if bank:
                bank.view_balance()
            else:
                print("No account found. Please create an account first.")

        elif choice == "5":
            print("Thank you for using the Marco Bank program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == '__main__':
    menu()
