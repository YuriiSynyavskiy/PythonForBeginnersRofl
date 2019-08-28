class Figure:
    def __init__(self, color, type):
        self.color = color
        self.type = type
    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor
    def info(self):
        print('Figure -  '+ str(self.type)+ ' Color -  '+str(self.color))
class Rectangle(Figure):
    def __init__(self, weight, height, color = 'Unknown', type = 'Rectangle' ):
        Figure.__init__(color, type)
        self.weight = weight
        self.height = height
    def calculateSquare(self):
        return self.weight*self.height
    def getWeigth(self):
        return self.weigth
    def setWeigth(self, newWeigth):
        self.weigth = newWeigth
    def getHeigth(self):
        return self.height
    def setHeigth(self, newHeigth):
        self.height = newHeigth
class Square(Figure):
    def __init__(self, side, color='Unknown' , type = 'Square'):
        Figure.__init__(self, color, type)
        self.side = side
    def calculateSquare(self):
        return self.side*self.side
    def setSide(self, newSide):
        self.side=newSide
    def getSide(self):
        return self.side

square1= Square(5)
square1.info()

square1.setColor('Green')
square1.info()


print(' Square = {0}'.format(square1.calculateSquare()))
square1.setSide(8)


print(' Square = {0}'.format(square1.calculateSquare()))
