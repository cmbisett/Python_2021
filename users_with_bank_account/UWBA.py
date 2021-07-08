class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.15, balance=0)

    def display_account_info(self):
        print(f"{self.name}: Balance {self.account.balance}") 

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)

    def interest(self, amount):
        self.account.yield_interest(amount)


class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)    

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdrawl(self, amount):
        if self.balance - amount <= 0:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - amount
        return self

    def yield_interest(self):
        newbalance = self.balance * self.int_rate
        self.account_balance = self.account_balance + newbalance        
        print(self.account_balance)
        return self.account_balance

    @classmethod
    def sum_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance 
        return sum

    @staticmethod
    def can_withdrawl(balance, amount):
        if balance - amount >= 0:
            return True
        else:
            return False


       


cameron = User('Cameron', 'cmbisett@gmail.com'); BankAccount(0.15, 0)
cameron.make_deposit(200)
cameron.make_deposit(200)
cameron.make_deposit(200)
cameron.make_withdrawl(700)
cameron.display_account_info()
