class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdrawl(self, amount):
        self.account_balance -= amount

    def yield_interest(self):
        newbalance = self.account_balance * .15
        self.account_balance = self.account_balance + newbalance        
        print(self.account_balance)

    def display_account_info(self):
        print(f"{self.name}: Balance {self.account_balance}")    

cameron = User('Cameron', 'cmbisett@gmail.com', 0)
# cameron.account_balance = 0
# cameron.name = 'Cameron'
# cameron.email ='cmbisett@gmail.com'

freddy = User('Freddy', 'fKreuger@murderfist.com', 0)
# freddy.account_balance = 0
# freddy.name = "Freddy"
# freddy.email = "fKrueger@murderfist.com"

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the 
#account's info all in one line of code (i.e. chaining)
cameron.deposit(500)
cameron.deposit(500)
cameron.deposit(100)
cameron.withdrawl(100)
cameron.yield_interest()
cameron.display_account_info()

#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display 
#the account's info all in one line of code (i.e. chaining)

freddy.deposit(500)
freddy.deposit(500)
freddy.withdrawl(100)
freddy.withdrawl(50)
freddy.withdrawl(50)
freddy.withdrawl(100)
freddy.yield_interest()
freddy.display_account_info()