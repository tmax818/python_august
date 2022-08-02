class BankAccount:
    # don't forget to add some default values for these parameters!

    accounts = []

    def __init__(self, data, name='checking') -> None: 
        self.name = name
        self.int_rate = data['int_rate']
        self.balance = data['balance']
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        pass
        # your code here
    def withdraw(self, amount:int)-> None:
        """this function is for taking some money!!!"""
        pass
        # your code here
    def display_account_info(self):
        print("balance: ", self.balance)
        pass
        # your code here
    def yield_interest(self):
        pass
        # your code here

    @classmethod
    def print_instances(cls, balance):
        for account in cls.accounts:
            if account.balance == balance:
                print(account)

acct1 = {'int_rate': .01, 'balance': 100}
acct2 = {'int_rate': .02, 'balance': 200}

print(help(BankAccount.withdraw))