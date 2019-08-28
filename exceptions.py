while True:
    try:
        number = int(input('Enter ur number: '))
        if number%2==0:
            print('Your number is even')
        else:
            print('Your number is odd ')
        break
    except ValueError:
        print('Wrong value, try again!')

    finally:
        print('Just a test')

class ValueBelowZero(Exception):
    #Raised when entered number is below than 0
    pass
def checkNumber(number):
    if number < 0:
        raise ValueBelowZero
    else:
        if number % 2 == 0:
            print('Your age is even number')
        else:
            print('Your age is odd  number')
try:
    number = int(input('Inpur ur age: '))
    checkNumber(number)
except ValueError:
    print("It's not 'int' number")
except ValueBelowZero:
    print('Your age is negative LOLLLL. R u okey?')

class NotEnoughElements(Exception):
    pass
class TooMuchElements(Exception):
    pass
string = input('Input ur number')

try:
    if len(string.split(',')) < 2:
        raise NotEnoughElements
    elif len(string.split(',')) >2:
        raise TooMuchElements
    else:
        number1 = int(string.split(',')[0])
        number2 = int(string.split(',')[1])
        number3 = number1/number2
except ValueError:
    print("You entered not 'int' types")
except ZeroDivisionError:
    print('U can not divide by zero')
except SyntaxError as e:
    print(e)
except NotEnoughElements:
    print('You entered less than 2 elements')
except TooMuchElements:
    print('You entered more than 2 elements')
else:
    print(number3)
finally:
    print('Just a end of try/except block')

dayOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
try:
    day = int(input('Input day : '))
    print(dayOfWeek[day-1])
except ValueError:
    print("You didn't enter 'int' type")
except SyntaxError as e:
    print(e)
except IndexError:
    print('Ur number is >7 or <1')
finally:
    print('Just end of try/except block')

