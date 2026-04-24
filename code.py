class HDFC_ATM:

    def __init__(self, balance=0):
        self.balance = balance
        print("Welcome to ATM Machine")

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("please enter your choice: "))

            if choice == 1:
                self.check_balance()

            elif choice == 2:
                amount = int(input("please enter deposit amount: "))
                self.deposit(amount)

            elif choice == 3:
                amount = int(input("please enter withdraw amount: "))
                self.withdraw(amount)

            elif choice == 4:
                print("Thank you for using ATM ")
                print("Have a nice Day")
                break

            else:
                print("Invalid choice")


# Create object
a1 = HDFC_ATM(10000)

# Call menu
a1.menu()