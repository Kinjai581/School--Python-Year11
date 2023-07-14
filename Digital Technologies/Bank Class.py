from Account.py import*


class Bank:
    def __init__(self, accounts, trading_hours, address, telephone):
        self.accounts = {}
        self.trading_hours = trading_hours
        self.address = address
        self.telephone = telephone


    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.balance
        else:
            raise ValueError("Account not found")


    def get_all_accounts(self):
        return self.accounts.values()
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            try:
                account.deposit(amount)
            except ValueError as e:
                raise ValueError(str(e))
        else:
            raise ValueError("Account not found")
        
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            try:
                account.withdraw(amount)
            except ValueError as e:
                raise ValueError(str(e))
        else:
            raise ValueError("Account not found")





bnk = Bank("9:00 AM to 5:00 PM", "123 Sesame Street", "612-558")
account1 = Account("Vejhay",  1000, '123456789', 'i love python')
account2 = Account("Mick", 500, '987654321', 'barbeque bacon burger')
bnk.get_account(account1)
bnk.get_account(account2)


