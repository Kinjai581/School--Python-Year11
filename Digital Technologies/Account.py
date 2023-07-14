class Account:
    def __init__(self, name, balance, account_number, password):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        if amount >= 50:
             raise AccountBalanceError('You cannot deposit more than this amount')

        else:
            print('You have deposited', amount)
            print(f'You now have {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise AccountBalanceError('Insuffienct Funds')
        else:
            self.balance -= amount
            print("You have withdrawn", amount)
            print(f"You have {self.balance} remaining")


    def print(self):
        print(self.name, 'has', self.balance, 'available to withdraw')

class AccountBalanceError(Exception):
    pass




account1 = Account("Vejhay",  1000, '123456789', 'i love python')
account2 = Account("Mick", 500, '987654321', 'barbeque bacon burger')