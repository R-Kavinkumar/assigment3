class BANK_ACCOUNT:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def deposit(self,ammount):
        self.balance+=ammount
    def withdraw(self,ammount):
        self.balance-=ammount
    def display(self):
        print("******************************************************************\nHEY! ",self.name.upper())
        print("WITH ACCOUNT NUMBER: ",self.account_number)
        print("YOUR ACCOUNT HOLDS: RS.",self.balance)
        print("\nDON\'T SHARE YOUR ACCOUNT DETAILS TO ANY ONE\n******************************************************************\n\n")
accno=int(input("ENTER THE ACCOUNT NUMBER: "))
name=input("ENTER YOUR NAME: ")
acc=BANK_ACCOUNT(account_number=accno,name=name,balance=1000.00)
while True:
    print("ENTER 1 TO WITHDRAW")
    print("ENTER 2 TO DEPOSIT")
    print("ENTER 3 TO DISPLAY ACCOUNT DETAILS")
    print("ENTER 0 TO EXIT")
    entry=int(input("-> "))
    if entry==1:
        taken=int(input("ENTER THE AMMOUNT YOU WITHDRAW->"))
        acc.withdraw(taken)
    elif entry==2:
        given=int(input("ENTER THE AMMOUNT YOU DEPOSIT->"))
        acc.deposit(given)
    elif entry==3:
        acc.display()
    elif entry==0:
        print("HAVE A NICE DAY!")
        break
    else:
        print("ENTER THE VALID INPUT\n\n")


