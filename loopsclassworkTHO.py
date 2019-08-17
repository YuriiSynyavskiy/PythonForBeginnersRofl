'''print('\n For : ')               #1
for i in range(1,100):
    if i%2==0:
        print(i,end =' ')
print('\n While : ')
j = 1
while j<100:
    if j%2==0:
        print(j,end =' ')
    j+=1                                                    #endOf1'''
'''print('\n For : ')                                             #2
j = 1
while j<100:
    j+=1
    if j%2==0:
        continue
    print(j,end =' ')

print('\n',list(range(1,100,2)))                                 #endOf2 '''
'''print('\n print stop to stop loop')                             # 3
randomList = list()
counter = 1
while True:                                                      
    newElement=input('[{0}] - '.format(counter))
    if newElement == 'stop':
        break
    else:
        randomList.append(int(newElement))
    counter+=1
print(randomList)

for i in randomList:
    if not(i%2==0):
        print('This array has odd element. ')
        break
else:
    print('All elements of this array r even. ')          #endOf3'''
'''counter = 1                                                #4
randomList = list()
while True:                                                   
    newElement=input('[{0}] - '.format(counter))
    if newElement == 'stop':
        break
    else:
        randomList.append(int(newElement))
    counter+=1
print(randomList)
randomList  = [float(a) for a in randomList]
print(randomList)                                               #endOf4'''
'''listOfFib = [0,1]                                               # 5
i=1 
n = int(input('Input n: '))
while listOfFib[i]<n:    
    listOfFib.append(listOfFib[i]+listOfFib[i-1])
    i+=1
print(listOfFib)                                                    #endOf5'''
'''tempList = list()                                                               #6&7 - *emoji
for i in range(4):
    tempString = input('Input {0} string  - '.format(i+1))
    tempList.append(tempString)
print(tempList)
for i in tempList:
    for letter in i:
        print(letter,end='  \U0001F920   ')

                                                                        #endOf6&7'''
'''n = int(input('Input ur number : '))                               #8
for i in range(2, n):
    if n % 2 == 0:
        print('This number r not ...')
        break
else:
    print('This number r diveded only by himself and 1')
                                                                            #endOf8'''
'''import math                                                                 #10

word = input('Input ur word : ')
i = 0
while i < math.floor(len(word) / 2):
    if not (word[i] == word[len(word) - i - 1]):
        print('Word is not a palindrom')
        break
    i += 1
else:
    print('Word is a palindrom')                                             #endOf10'''

import random                                                   #9
randNumber = random.random()
print('    ',randNumber)
strRandNumber = str(randNumber)
max = int(strRandNumber[0])
for item in strRandNumber:
    if item == '.':
        continue
    else:
        if max < int(item):
            max = int(item)
listOfPositions = list()
counter = 0
print('Max: ',end='')
for item in strRandNumber:
    if item == str(max):
        listOfPositions.append(counter + 1)
    counter+=1
for item in range(1,len(strRandNumber)):
    if item in listOfPositions:
        print('\U00002191',end='')
    else:
        print(' ',end='')








