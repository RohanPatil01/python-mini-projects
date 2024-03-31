class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu() # to call the menu() function
    def menu(self):
        user_input = input("""
        Hello, How can I help you today?
            1. Press 1 to Create Pin.
            2. Press 2 to Change Pin.
            3. Press 3 to Check Balance.
            4. Press 4 to Withdraw Money.
            5. Press 5 to Deposit Money.
            6. Press anything else to exit.
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        elif user_input == "5":
            self.deposit()
        else:
            self.exit()

    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input('Enter your balance: ')) #It is logically incorrect but we don't have any data, therefore we are asking from the user.
        self.balance = user_balance

        print('Your pin is created successfully!')
        self.menu()

    def check_pin(self):
        check_pin = input("Enter your pin: ")
        if check_pin == self.pin:
            return True

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
    
        if old_pin == self.pin:
          # let him change the pin
            new_pin = input("Enter your new pin: ")
            check_pin = input("Confirm your new pin: ")
            if new_pin == check_pin:
                self.pin = new_pin
                print('Your pin is changed successfully!')
                self.menu()
            else:
                print("Pins are not matching. Please Try Again!")
                self.change_pin()
        else:
            print("You have entered an incorrect pin! Please try again!")
            self.change_pin()

    def check_balance(self):
        if self.check_pin():
            print(f"Your current balance is: {self.balance}")
            self.menu()
        else:
            print("You have entered an incorrect pin! Please try again!")
            self.check_balance()

    def withdraw(self):
        if self.check_pin():
            amt = int(input("Enter the amount you want to withdraw: "))
        
            if amt <= self.balance:
                self.balance = self.balance - amt
                print("Amount withdrawn successfully!")
                self.menu()
            else:
                print("Your account balance is low!")
                self.withdraw()
                
        else:
            print("You have entered an incorrect pin! Please try again!")
            self.withdraw()

    def deposit(self):
        if self.check_pin():
            amt = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amt
            print("Amount depositted successfully!")
            self.menu()

        else:
            print("You have entered an incorrect pin! Please try again!")
            self.deposit()
            
    def exit(self):
        ask = input("""
        Do you want to exit? 
            1. Press 1 for Yes.
            2. Press 2 for No.
        """)
        if ask == "1":
            print("Thank you for visiting us. Have a Nice day!")
        else:
            self.menu()
