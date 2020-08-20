class Account():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        print(f'Account Holder: {self.name}\nAccount Balance: {self.balance}')

    def add_balance(self):
        amount=int(input('Enter the amount you want to add: '))
        self.balance=self.balance+amount
        print('INR {} has been successfully added ☺.'.format(amount))
        print(f'Current balance is {self.balance}.')

    def withdrawl(self):
        amount_withdrawl=int(input('Enter amount to withdraw'))
        if self.balance>=amount_withdrawl:
            self.balance=self.balance-amount_withdrawl
            print(f'INR {amount_withdrawl} has been withdrawn successfully ☺')
            print(f'Remaining balance is INR {self.balance}')
        else:
            print('Funds Insufficient')

x=Account('Koushik',2000)
x.__str__()
pin=int(input('Enter your PIN:'))
if pin!=4116:
    print('Invalid pin!,try again')
else:
    ip=int(input('If you want to Deposit , Please press "1" \nIf you want to withdraw, Please press "2" '))
    if ip==1:
        x.add_balance()
    elif ip==2:
        x.withdrawl()
    else:
        print('Invalid choice')


