import numpy
number = input('Input ur number: ')
listOfNumbers = [int(a) for a in number ]
multiplications = numpy.prod(listOfNumbers)
print('Multiplication of digits = ', multiplications)
print("Reversed number: ", number[::-1])
print("Sorted digits: ", sorted(number))