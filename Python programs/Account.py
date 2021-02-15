#Account Class

while True:
    n=input("Enter 1 to countinue or press any key to Exit:")
    if n=='1':
        class Bank_Account():
            def __init__(self,name, balance, amount_deposit, amount_withdraw, main_balance):
                self.name = name
                self.balance = balance
                self.amount_deposit = amount_deposit
                self.amount_withdraw = amount_withdraw
                self.main_balance = main_balance
            def withdraw(self,amount_withdraw):
                if (self.main_balance)<amount_withdraw:
                    print("Balance is insufficent")
                else:
                    balance3 = main_balance-amount_withdraw
                    print("After withdraw amount is",balance3)
            def deposit(self, amount_deposit):
                balance2 = self.main_balance
                print("After deposit amount is",balance2)
            def total(self, amount_deposit, amount_withdraw):
                balance4 = (balance)-(amount_withdraw)+(amount_deposit)
                print("Total Amount", balance4)
            def print(self):
                print("Name",self.name)
                print("Balance",self.balance)
                print("Amount deposited",self.amount_deposit)
                print("Amount withdrawn",self.amount_withdraw)
    
        name = input("Enter Name:")
        balance = float(input("Enter Balance"))
        amount_deposit = float(input("Enter amount u deposit:"))
        main_balance = amount_deposit+balance
        amount_withdraw = float(input("Enter amount u withdraw:"))

        B1=Bank_Account(name, balance, amount_deposit, amount_withdraw, main_balance)
        B1.print()
        B1.withdraw(amount_withdraw)
        B1.deposit(amount_deposit)
        B1.total(amount_deposit, amount_withdraw)
    else:
        print("Exited")
        quit()




                   
        
