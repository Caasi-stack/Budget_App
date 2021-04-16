database = {}

class Budget():
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def balance(data):
        for category, balance in database.items():
            print(category, balance)

    def transfer(database, option1, amount, option2):
        input1 = database[option1]
        input2 = database[option2]

        database[option1] = int(input1) - amount
        database[option2] = int(input2) + amount


def init():
    print("=== ==== ==== ==== ==== ===")
    print(" Welcome to the Budget App ")
    print("=== ==== ==== ==== ==== ===")
    print()
    menu()

def menu():
    user = int(input("What would you like to do?: \n"
                     "(1) Create a new budget \n"
                     "(2) Deposit into a budget \n"
                     "(3) Withdraw from a budget \n"
                     "(4) Check budget balance \n"
                     "(5) Transfer \n"
                     "(6) quit \n"
                     "\n:"
                     ))
    if user == 1:
        new_budget()

    elif user == 2:
        deposit()

    elif user == 3:
        withdraw()

    elif user == 4:
        get_balance()

    elif user == 5:
        transfer()

    elif user == 6:
        logout()


def new_budget():
    print("=== ==== ==== ==== ===")
    print(" Create a new budget ")
    print("=== ==== ==== ==== ===")

    title = str(input("Enter a budget name \n"))
    amount = int(input("Enter amount \n#"))
    budget = Budget(title, amount)
    database[title] = amount

    print("=== ==== ==== ==== ==== ===== ===== ===== =====")
    print(f"Budget {title} has been created with #{amount}")
    print("=== ==== ==== ==== ==== ===== ===== ===== =====")
    menu()


def deposit():
    for key, value in database.items():
        print(f"- {key}")

    user = input("Select a budget \n")

    option = int(input("Would you like to continue with the transaction? \n (1) Yes \n (2) No \n"))

    if option == 1:
        if user in database:
            amount = int(input("Enter any amount \n#"))
            balance = int(database[user])
            budget = Budget("category", balance)
            new_balance = budget.deposit(amount)
            database[user] = new_balance
            print(f"Budget {user} has been credited with #{amount}")
            menu()

        else:
            print(f"Budget {user} does not exist!!!")
            select = int(input("(1) Create a new budget \n (2) Input a valid budget \n (3) Go back to the menu \n"))
            if select == 1:
                new_budget()
            elif select == 2:
                deposit()
            elif select == 3:
                menu()
            else:
                print("Invalid option selected.")
                deposit()

    elif option == 2:
        print("Transaction has been cancelled.")
        menu()

    else:
        print("Invalid option selected.")
        deposit()

def withdraw():
    for key, value in database.items():
        print(f"- {key}")

    user = input("Select a budget \n")

    option = int(input("Would you like to continue with the transaction? \n (1) Yes \n (2) No \n"))

    if option == 1:
        if user in database:
            amount = int(input("Enter any amount \n#"))
            if amount < database[user]:
                balance = int(database[user])
                budget = Budget("category", balance)
                new_balance = budget.withdraw(amount)
                database[user] = new_balance
                print(f"#{amount} has been debited from Budget-{user}")
                menu()

            else:
                print(f"===*** Insufficient amount ***===")
                option = int(input("Please select available options \n (1) Deposit \n (2) Enter a valid budget \n (3) Check balance"))
                if option == 1:
                    deposit()

                elif option == 2:
                    withdraw()

                elif option == 3:
                    get_balance()

                else:
                    print("Invalid option selected.")
                    withdraw()

        else:
            print(f"Budget {user} does not exist!!!")
            select = int(input("(1) Create a new budget \n (2) Input a valid budget \n (3) Go back to the menu \n"))
            if select == 1:
                new_budget()
            elif select == 2:
                withdraw()
            elif select == 3:
                menu()
            else:
                print("Invalid option selected.")
                withdraw()

    elif option == 2:
        print("Transaction has been cancelled.")
        menu()

    else:
        print("Invalid option selected.")
        withdraw()

def get_balance():
    check_balance = Budget.balance(database)
    if check_balance == None:
        menu()
    else:
        print(f"#{check_balance}")
        menu()

def transfer():
    for key, value in database.items():
        print(f"- {key}")

    from_budget = input("Enter the budget you wish to transfer from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you wish to transfer \n#"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter recipient destination \n")
            if to_budget in database:
                data = Budget.transfer(database, from_budget, from_amount, to_budget)
                print(f"You have transferred #{from_amount} from {from_budget} to {to_budget}.")
                for key, value in database.items():
                    print(key, value)
                menu()

            else:
                print(f"Budget {user} does not exist!!!")
                transfer()

        else:
            print(f"You do not have sufficient amount-#{from_amount} in {from_budget} budget")
            transfer()

    else:
        print(f"Budget {from_budget} does not exist!!!")
        transfer()

def logout():
    option = int(input("Do you wish to quit? \n (1) Yes \n (2) No \n"))
    if option == 1:
        print("Thank you for trusting us with your budget. See you next time!!!")
        exit()
    elif option ==2:
        menu()
    else:
        print("Invalid input.")
        logout()

init()


