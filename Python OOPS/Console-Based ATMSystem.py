'''
The ATM Management System is a Python OOPS-based mini project that simulates basic banking operations such as PIN creation, money deposit, withdrawal, and balance checking. 
The program uses a class named `ATM` to represent an ATM account, where the constructor `__init__()` initializes the PIN and account balance for each object.
Methods like `deposit()`, `withdraw()`, and `checkbalance()`perform different banking operations after verifying the user’s PIN for security.
The `check()` method displays a menu repeatedly using a loop and allows users to choose different ATM services until they decide to exit.
Objects such as `SBI` and `PNB` represent different bank accounts, demonstrating important Object-Oriented Programming 
concepts like classes, objects, constructors, methods, encapsulation, and user interaction in Python.

#Class
A class is a blueprint or template used to create objects. It defines the data and functions that an object will have. 
In our program, ATM is a class that contains ATM-related data like PIN and balance along with operations such as deposit, withdrawal, and balance checking.

#Methods
Methods are functions defined inside a class that perform specific tasks. They help objects perform actions.
In your ATM project, methods like deposit(), withdraw(), and checkbalance() are used to perform banking operations.

#Encapsulation
Encapsulation means binding data and methods together inside a single unit called a class and restricting direct access to data. 
In our ATM project, the balance and PIN are stored inside the ATM class, and users can access or modify them only through methods like deposit() and withdraw(). 
This helps protect the data and provides security

'''


class ATM:

    def __init__(self, pin, balance):

        self.pin = pin
        self.balance = balance

    def create_pin(self):

        self.pin = int(input("Enter new PIN: "))
        print("PIN created successfully")

    def deposit(self):

        pin = int(input("Enter PIN: "))

        if self.pin == pin:

            dep_amount = int(input("Enter amount to be deposited: "))

            self.balance += dep_amount

            print("Money deposited successfully")

        else:
            print("Wrong PIN")

    def withdraw(self):

        pin = int(input("Enter PIN: "))

        if self.pin == pin:

            withdraw_amount = int(input("Enter amount to withdraw: "))

            if withdraw_amount <= self.balance:

                self.balance -= withdraw_amount

                print("Withdrawal successful")

            else:
                print("Insufficient balance")

        else:
            print("Wrong PIN")

    def checkbalance(self):

        pin = int(input("Enter PIN: "))

        if self.pin == pin:

            print("Available balance:", self.balance)

        else:
            print("Wrong PIN")

    def check(self):

        while True:

            user_input = input(
            '''
1. Create a PIN
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit

Enter choice: '''
            )

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()

            elif user_input == "3":
                self.withdraw()

            elif user_input == "4":
                self.checkbalance()

            elif user_input == "5":
                print("Thank You")
                break

            else:
                print("Invalid Choice")


SBI = ATM(1234, 89000)
SBI.check()

PNB = ATM(4321, 50000)
PNB.check()
