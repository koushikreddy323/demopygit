# Miles to kilometers
def miles():
    m=int(input('Enter the number of miles'))
    k=m*1.6
    print(k,' kilometers')
#miles()
#------------------------------------------------------------------
# Celsius to Fahrenheit
def temp():
    c=int(input('enter the celsius'))
    f=(c*1.8)+32
    print('{} celsius in fahrenheit is {} '.format(c,f))
#temp()
#------------------------------------------------------------------
# Calender month
import calendar
def calender():
    y=int(input('Enter year'))
    m=int(input('Enter month'))
    print(calendar.month(y,m))
#calender()
#------------------------------------------------------------------
# Prime numbers
def prime():
    n=int(input('Enter a number'))
    if n>1:
        for x in range(2,n):
            if (n%x)==0:
                print('not a prime number')
                break
        else:
                print('prime number')
    else:
        print('not a prime')
#prime()
#------------------------------------------------------------------
#prime numbers btw the interval

def prmint():
    l=int(input('Enter the lower number'))
    u=int(input('Enter the upper number'))
    for x in range(l,u+1):
        if x>1:
            for i in range(2,x):
                if (x%i)==0:
                    break
            else:
                print(x)

#prmint()
#------------------------------------------------------------------
# Factorial
def facto():
    n=int(input('Enter the number'))
    factorial=1
    if n<0:
        print('Factorial does not exist for negative numbers')
    elif n==0:
        print('Factorial is 1')
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        print(factorial)
#facto()
#------------------------------------------------------------------
#Multiplication table
def multiTab():
    n=int(input('Enter the multiplication table'))
    for x in range(1,11):
        print(n,'x',x,'=',n*x)
#multiTab()
#------------------------------------------------------------------
#Fibonacci
def fib():
    a=0
    b=1
    print(0,1)
    for x in range(10):
        c=a+b
        a=b
        b=c
        print(c)
#fib()
#------------------------------------------------------------------
#
