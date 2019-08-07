firstNumber = int(input('Input first number : '))
secondNumber  = int(input('Input second number : '))
if secondNumber==0:
    print("I'm so lazy to do block with exception")
else:
    print('{0} + {1} = {2}'.format(firstNumber,secondNumber,firstNumber+secondNumber))
    print('{0} - {1} = {2}'.format(firstNumber, secondNumber, firstNumber - secondNumber))
    print('{0} * {1} = {2}'.format(firstNumber, secondNumber, firstNumber * secondNumber))
    print('{0} / {1} = {2}'.format(firstNumber, secondNumber, firstNumber / secondNumber))