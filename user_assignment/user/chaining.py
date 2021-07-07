class User:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.account_balance = ''

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        #print(self.account_balance)

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount



#CREATE 3 SEPERATE USER INSTANCES
cameron = User()
cameron.account_balance = 200
cameron.name = 'Cameron'
cameron.email ='cmbisett@gmail.com'

bella = User()
bella.account_balance = 100
bella.name = 'Bella'
bella.email = 'byella@gmail.com'

freddy = User()
freddy.account_balance = 500000
freddy.name = "Freddy"
freddy.email = "fKrueger@murderfist.com"

#FIRST USER 3 DEPOSITS AND 1 WITHDRAWL, DISPLAY BALANCE
cameron.make_deposit(200)
cameron.make_deposit(200)
cameron.make_deposit(600)
cameron.make_withdrawl(200)
cameron.display_user_balance()

#SECOND USER MAKES 2 DEPOSITS AND 2 WITHDRAWLS, AND DISPLAY BALANCE
bella.make_deposit(400)
bella.make_deposit(400)
bella.make_withdrawl(100)
bella.make_withdrawl(600)
bella.display_user_balance()

#THIRD USER MAKE 1 DEPOSIT AND 3 WITHDRAWLS, DISPLAY BALANCE
freddy.make_deposit(5)
# freddy.make_withdrawl(100)
# freddy.make_withdrawl(500)
# freddy.make_withdrawl(100)
# freddy.display_user_balance()

cameron.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


#BONUS CREDIT
cameron.transfer_money(bella, 200)
print(cameron.account_balance)
print(bella.account_balance)

