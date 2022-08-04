
from bank_pkg.bank_account import BankAccount
from bank_pkg import most_useful_func

class User:

    users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self):
        pass
    
    def make_withdrawal(self):
        most_useful_func()

    def display_user_balance(self):
        pass

    def transfer_money(self, amount, recp):
        self.make_withdrawal(amount)
        recp.make_deposit(amount)


user1 = User('Tyler', 'tmax@aol.com')
user1.make_deposit(2000)
user2 = User("Sam", 'sam@email.com')
user1.transefer_money(1000,user2 )