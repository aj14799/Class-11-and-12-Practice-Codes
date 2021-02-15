#Account Class Inheritance
class Bank_Account():
    def __init__(self,name, balance, Acc_no):
        self.name = name
        self.balance = balance
        self.Acc_no = Acc_no
        
    def show(self):
        print ('\n\nAccount Details Are---')
        print('Customer Name: ' ,self.name)
        print('Account No. : ' , self.Acc_no)
        print('Balance: ' ,self.balance)
    def deposit(self, amount_deposit):
        self.balance+= amount_deposit
        print("\nAmount Deposited")
    def withdraw(self, amount_deposit):
        if self.balance<amount_deposit:
            print ('\nInsufficient Balance')
            return
        self.balance-=amount_deposit
        print('\nAmount Withdrawn')

class Current(Bank_Account):
    def __init__(self, name, balance, Acc_no):
        Bank_Account.__init__(self, name, balance, Acc_no)

    def check(self, minb):
        if self.balance<=minb:
            print('\nLow balance, Penalty imposed')
            self.balance+=250

class Savings(Bank_Account):
    def __init__(self, name, balance, Acc_no):
        Bank_Account.__init__(self, name, balance, Acc_no)
    def intrest(self, rate):
        self.intrest = self.balance*rate/100
        self.balance+=self.intrest
        print("Intrest Added")            

B1=Savings('Rakesh', 4234567890,567890)
B2=Current('Suresh', 1785445467, 434344)
B1.show()
B2.show()
B1.deposit(43000)
B1.intrest(5)
B2.withdraw(82098)
B2.check(1000)
B1.show()
B2.show()





           

