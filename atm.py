# ATM machine using OOP

class Atm:

    def __init__(self):
        self.pin = ' '
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()

        elif user_input == '3':
            self.check_balance()

        elif user_input == '4':
            self.withdraw()

        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter your new pin: ')
        self.pin = user_pin

        # ik it is dumb but i am not building it full stack so we are not fetching it from bank hehe
        user_balance = (int(input('Enter your Balance: ')))
        self.balance = user_balance

        print('Pin created succesfully!')
        self.menu()

    def change_pin(self):
        user_oldpin = input('Enter your old pin: ')
        if user_oldpin == self.pin:
            user_newpin = input('Enter your new pin: ')
            self.pin = user_newpin
            print('Pin changed sussesfully!')
            self.menu()
        else:
            print('Nah bro you forgot the pin! you tryna steal? HAHAHA')
            self.menu()

    def check_balance(self):
        user_pin = input('Enter your pin: ')

        if user_pin == self.pin:
            print(f'your balance is {self.balance}')
            self.menu()

        else:
            print('try your pin again buddy! Eat some Almonds!')
            self.menu()

    def withdraw(self):
        user_pin = input('Enter your pin: ')

        if user_pin == self.pin:
            user_amount = (
                int(input('Enter the amount you want to withdraw: ')))

            print(
                f'you withdrawed {user_amount} of money. your new balance will be {self.balance - user_amount}')

            self.menu()

        else:
            print('Buddy you really need to change your pin game and remeber it !')
            self.menu()


Obj = Atm()   # calling the class Atm with the object Obj
