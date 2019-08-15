

'''
#1
def sered(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum/len(args)
print(sered(10,20,30))
#2
def myAbs(number):
    return number if number>0 else number*(-1)
print(myAbs(-2))
print(myAbs(-4))
print(myAbs(2))
#3
def max(var_1, var_2):'''
    #docstring
'''
    return var_1 if var_1>=var_2 else var_2
print(max.__doc__, end=' ')
print(max(8,-2))
#4
from math import sqrt
from math import pi
def rectangleSquare(side_1, side_2):
    return side_1*side_2
def triangleSquare(side_1,side_2,side_3):
    p = (side_1+side_2+side_3)/2
    return sqrt(p*(side_1-p)*(side_2-p)*(side_3-p))
def circleSquare(r):
    return 4*pi*r*r
square = int(input('Input object - 1:rectanle 2:triangle  3:circle'))
if square == 1:
    side_1  = int(input('Input 1 side of rectangle : '))
    side_2  = int(input('Input 2 side of rectangle : '))
    print('S = {0} * {1} = {2}'.format(side_1,side_2,rectangleSquare(side_1,side_2)))
elif square == 2:
    side_1 =  int(input('Input 1 side of triangle : '))
    side_2 =  int(input('Input 2 side of triangle : '))
    side_3 =  int(input('Input 3 side of triangle : '))
    print('S = {0}'.format(triangleSquare(side_1,side_2,side_3)))
elif square == 3:
    r = int(input('Input R of circle : '))
    print('S = 4*\u03C0*{0}\U000000B2 =  {1}'.format(r,circleSquare(r)))
else:
    print('Unknown symbol')'''
#5
def sum(number):
    sum=0
    for i in number:
        sum+=int(i)
    return sum
print(sum(input('Input ur number : ')))

#6
def sum(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiplicate(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ZeroDivisionError
    else:
        return a/b

def calc_main():
    operation = input('* / - + :')

    if operation == '*':
        firstNumber = int(input('Input first number : '))
        secondNumber = int(input('Input second number : '))
        print('{0} * {1} = {2}'.format(firstNumber,secondNumber,multiplicate(firstNumber,secondNumber)))
    elif operation =='/':
        firstNumber = int(input('Input first number : '))
        secondNumber = int(input('Input second number : '))
        try:
            print('{0} / {1} = {2}'.format(firstNumber, secondNumber, divide(firstNumber, secondNumber)))
        except ZeroDivisionError:
            print('Can not divide by 0')
    elif operation =='+':
        firstNumber = int(input('Input first number : '))
        secondNumber = int(input('Input second number : '))
        print('{0} + {1} = {2}'.format(firstNumber, secondNumber, sum(firstNumber, secondNumber)))
    elif operation =='-':
        firstNumber = int(input('Input first number : '))
        secondNumber = int(input('Input second number : '))
        print('{0} - {1} = {2}'.format(firstNumber, secondNumber, substract(firstNumber, secondNumber)))
    else:
        print('Unknown operation')
calc_main()

#7
from math import sqrt
def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


for i in range(20):
    print(fib(i), end=' ')
#8
def quadraticEquation(a,b,c):
    return b*b-4*a*c

randomVar = input('\n Input like this a*x2+b*x1+c=d :')
a = int(randomVar[0])
b = int(randomVar[5])
c = int(randomVar[10]) - int(randomVar[12])
D  = quadraticEquation(a,b,c)
print('\U0000221A D =  ',sqrt(D))
if D >= 0:
    print('x1 = {0} \n x2 = {1}'.format((-b + sqrt(D))/(2*a),(-b - sqrt(D))/(2*a)))
else:
    print("D<0 this equation havan't roots")

