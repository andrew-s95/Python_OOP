class bankAccount:              #bank account class goes first because user class refers to this 
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest

class User: #creating a class called user
    def __init__(self, username, email, numAcc): 
        self.username = username
        self.email = email
        self.account = []
        for x in range(numAcc):
            self.account.append(bankAccount(int_rate=0.02, balance=0))   #not a parameter because setting default to 0
    
    def accountsel(self, num):
        return self.account[num]

    #def make_deposit(self, amount): #deposit into account function
        #self.account_balance += amount
        #return self

    #def make_withdrawal(self, amount): #deposit into account function
        #self.account_balance -= amount
        #return self

    #def display_user_balance(self):
        #print(self.account_balance)
        #return self

    #bonnus transfer money method (in the works)
    #def transfer_money(self, amount):
        #self.account_balance(username.make_deposit, username.make_withdrawal, amount):
        #return self



#creating 3 instances within User
andrew = User("Andrew Sun", "andrew@gmail.com", 2)
erik = User("Erik P", "ep@gmail.com", 2)
jon = User("Jonathan G", "jg@gmail.com", 2)

#User 1, 3 deposits, 1 withdrawal, deposit display
andrew.accountsel(1).deposit(100).deposit(1000).deposit(100).withdraw(51).display_account_info()

#User 2, 2 deposits, 2 withdrawals, display
erik.accountsel(1).deposit(100).deposit(200).withdraw(50).withdraw(20).display_account_info()

#User 3, 1 deposits, 3 withdrawals, display
jon.accountsel(1).deposit(1000).withdraw(20).withdraw(240).withdraw(2).display_account_info()

