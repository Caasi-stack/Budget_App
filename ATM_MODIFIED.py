import random
import datetime

database = {}
balance = {2}

now = datetime.datetime.now()


#initializing the system
def init():

    print("Welcome to bank Zuri")
    print(now)

    account_request = int(input("Do you have an account with us: 1. (Yes) 2. (No) \n"))
    if account_request == 1 :
        login()

    elif account_request == 2 :
        print(register())

    else:
        print("You have selected an invalid option")
        init()


#login function
def login():
    print("************ Login ************")

    account_number_from_user = int(input("Enter your account number: \n"))
    password = input("Enter your password: \n")

    for account_number,user_details in database.items() :
        if account_number == account_number_from_user :
                if user_details[3] == password:
                    bank_operation(user_details)
                    return -1

    print("Invalid account or password")
    init()
    login()




#registration function
def register():
    print("*****************************")
    print("Register for your new account")
    print("*****************************")
    email = input ("Enter your email address: \n")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    password = input("Create a password:  \n")
    confirm_password = input("Confirm your password: \n")

    if password == confirm_password:

        account_number = generate_account_number()

        database[account_number] = [ first_name, last_name, email, password ]

        print("Your account as been created")
        print("=== ==== ==== ==== ==== ==== ==== ==== ===")
        print(f"your account number is: {account_number}")
        print("Keep your account details safe")
        print("=== ==== ==== ==== ==== ==== ==== ==== ===")

    else:
        print("Password doesn't match. Please try again")
        register()
        return -1


    login()
    database_2()

def database_2():
    data = register()
    database.update(data)
    print(database)


#bank operation function
def bank_operation(user):
    print(f"Welcome {user[0], user[1]}")
    selected_option =int(input("What would you like to do: (1) Deposit (2) Withdrawal (3) Check balance (4) Logout (5) Exit \n"))

    if selected_option == 1:
        deposit()

    elif selected_option == 2:
        withdrawal()

    elif selected_option == 3:
        check_balance()

    elif selected_option == 4:
        login()

    elif selected_option == 5:
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user)
    logout()


def withdrawal():
    amount = int(input("Enter any amount: \n"))
    amount -= amount
    withdrawal.update_withdrawal(amount)
    for amount in withdrawal :
       if  balance <= amount :
           print("Insufficient balance.")

    print("Withdrawal successful ")
    init()

def deposit():
    amount = int(input("Enter any amount: \n"))
    amount += amount
    deposit.update_deposit(amount)
    print("Cash deposit successful.")
    init()

def update_deposit():
    cash = deposit()
    balance.update(cash)
    print(balance)

def update_withdrawal():
    cash = withdrawal()
    balance.update(cash)
    print(balance)

def check_balance():
    update_withdrawal()
    update_deposit()
    print(f"Your account balance is: str{balance}")

def generate_account_number() :
    return random.randrange(1111111111, 9999999999)

def logout():
    init()

def exit():
    return init()


init()
database_2()