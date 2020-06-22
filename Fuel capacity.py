
class petrol():
    def fuel(self):
        x=int(input('Enter the number of kms traveled'))
        ft=35
        mil=20
        y=x/mil
        fl=ft-y
        print('Fuel left in tank is {} liters'.format(fl))
        print('Estimated kilometers :{}'.format((fl)*20))
        ft=fl
        x = input('did u refuel?')
        if x == 'y':
            rf = float(input('Enter the amount of petrol '))
            ft = ft + rf
            print('Fuel left in tank: {}'.format(ft))
        else:
            ft=fl
            print(ft)

    def amount(self):
        Distance=int(input('Enter the distance'))
        mileage=20
        fp=78
        x=Distance/mileage
        print(x,'liters')
        print(x*fp,'Rupees')
        print('Happy Journey ☺ ')

ob1=petrol()

try:
    i=int(input('Enter the number'))
    if i==0:
        ob1.fuel()
    elif i==1:
        ob1.amount()
    else:
        print('Enter "0" for kms driven and "1" for estimation')
except ValueError:
            print('Enter only integers')


