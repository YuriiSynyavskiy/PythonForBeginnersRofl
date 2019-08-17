import pygame as pg, sys, math
k=0
mainList = [['q','x','z'],                  #for values
            ['t','g','r'],
            ['h','y','n']]
listOfSquares =  [[None, None, None],                   #for coordinates of squares
                  [None, None, None],
                  [None, None, None]]
listOfMovingSquares = [[[1,1],[0,1],[-1,1]],
                       [[1,0],[0,0],[-1,0]],
                       [[1,-1],[0,-1],[-1,-1]]]
pg.init()
clock = pg.time.Clock()
def hash():
    for i in range(1,17):
        #pg.draw.line(screen, (13, 161, 146), (232, 60), (232,432),5)
        pg.draw.line(screen, (13, 161, 146), (232,240), (232,240-i*11.2), 5)
        pg.draw.line(screen, (13, 161, 146), (232,250), (232,250+i*11.2), 5)
        #pg.draw.line(screen, (13, 161, 146), (360, 60), (360, 432),5)
        pg.draw.line(screen, (13, 161, 146), (360, 240), (360, 240 - i * 11.2), 5)   #animation
        pg.draw.line(screen, (13, 161, 146), (360, 250), (360, 250 + i * 11.2), 5)

        #pg.draw.line(screen, (13, 161, 146), (110, 182), (482, 182) ,5 )
        pg.draw.line(screen, (13, 161, 146), (290, 182), (290-11.4*i, 182), 5)
        pg.draw.line(screen, (13, 161, 146), (300, 182), (300+11.4*i, 182), 5)

        #pg.draw.line(screen, (13, 161, 146), (110, 308), (482, 308), 5)
        pg.draw.line(screen, (13, 161, 146), (290, 308), (290 - 11.4 * i, 308), 5)
        pg.draw.line(screen, (13, 161, 146), (300, 308), (300 + 11.4 * i, 308), 5)
        pg.display.update()
        clock.tick(60)
def hashWithOutAnimation():
    pg.draw.line(screen, (13, 161, 146), (232, 240), (232, 60), 5)
    pg.draw.line(screen, (13, 161, 146), (232, 250), (232, 432), 5)

    pg.draw.line(screen, (13, 161, 146), (360, 240), (360, 60), 5)  # animation
    pg.draw.line(screen, (13, 161, 146), (360, 250), (360, 432), 5)

    pg.draw.line(screen, (13, 161, 146), (290, 182), (110, 182), 5)
    pg.draw.line(screen, (13, 161, 146), (300, 182), (482, 182), 5)

    pg.draw.line(screen, (13, 161, 146), (290, 308), (110, 308), 5)
    pg.draw.line(screen, (13, 161, 146), (300, 308), (482, 308), 5)
def drawX(coordinatesOfSquare):
    for i in range(1,10):
        print(coordinatesOfSquare)
        pg.draw.line(screen, (128, 128, 128), (coordinatesOfSquare[0]+20, coordinatesOfSquare[1] + 20), (coordinatesOfSquare[0]+20 + 9*i, coordinatesOfSquare[1] + 20 + 9*i), 8)
        pg.draw.line(screen, (128, 128, 128), (coordinatesOfSquare[0]+20, coordinatesOfSquare[1] + 10 + 9*10), (coordinatesOfSquare[0]+20 + 9*i , coordinatesOfSquare[1] + 10  + 9*10 - 9*i ), 8)
        pg.display.update()
        clock.tick(60)
def drawXWithOutAnimation(coordinatesOfSquare):
    pg.draw.line(screen, (128, 128, 128), (coordinatesOfSquare[0] + 20, coordinatesOfSquare[1] + 20),
                 (coordinatesOfSquare[0] + 20 + 9 * 9, coordinatesOfSquare[1] + 20 + 9 * 9), 8)
    pg.draw.line(screen, (128, 128, 128), (coordinatesOfSquare[0] + 20, coordinatesOfSquare[1] + 10 + 9 * 10),
                 (coordinatesOfSquare[0] + 20 + 9 * 9, coordinatesOfSquare[1] + 10 + 9 * 10 - 9 * 9), 8)
    pg.display.update()
def drawO(coordinatesOfSquare):
    ''''(242, 235, 211)'''
    pg.draw.circle(screen,(249, 255, 188),(int((coordinatesOfSquare[0]+coordinatesOfSquare[2])/2), int((coordinatesOfSquare[1]+coordinatesOfSquare[3]) /2)), 45, 4)
    pg.display.update()
def drawWinLine(color, x1,y1,x2,y2, ticksX, ticksY):
    #pg.draw.line(screen, color, x1,x2)
    global k
    tempVarX = 0
    tempVarY = 0
    if ticksX == 0:
        tempVarX  = x2 - x1
    if ticksY == 0:
        tempVarY = y2 - y1
    for i in range(1,15):
        pg.draw.line(screen, color , (x1, y1), (x1+i*ticksX + tempVarX, y1 + i*ticksY + tempVarY), 5 + k)
        pg.display.update()
        clock.tick(60)
        '''Animations of end of the game '''
def checkTheEndOfGame():
    global mainList, countForCells, EndOfGame, k, postAnimation, winLine
    if mainList[0][0] == mainList[0][1] and mainList[0][1] == mainList[0][2]:
        postAnimation = True
        winLine = [[0,0],[0,1],[0,2]]
        if mainList[0][0] == 1:
            drawWinLine((128,128,128), 90, 120, 502, 120, 29, 0)
        else:
            drawWinLine((249, 255, 188), 90, 120, 502, 120, 29, 0)
        postAnimate()
    elif mainList[1][0] == mainList[1][1] and mainList[1][1] == mainList[1][2]:
        postAnimation = True
        winLine = [[1, 0], [1, 1], [1, 2]]
        if mainList[1][0] == 1:
            drawWinLine((128, 128, 128), 90, 246, 502, 246, 29, 0)
        else:
            drawWinLine((249, 255, 188), 90, 246, 502, 246, 29, 0)
    elif mainList[2][0] == mainList[2][1] and mainList[2][1] == mainList[2][2]:
        postAnimation = True
        winLine = [[2, 0], [2, 1], [2, 2]]
        if mainList[2][0] == 1:
            drawWinLine((128, 128, 128), 90, 373, 502, 373, 29, 0)
        else:
            drawWinLine((249, 255, 188), 90, 373, 502, 373, 29, 0)
    elif mainList[0][0] == mainList[1][0] and mainList[1][0] == mainList[2][0]:
        postAnimation = True
        winLine = [[0, 0], [1, 0], [2, 0]]
        if mainList[0][0] == 1:
            drawWinLine((128, 128, 128), 170, 40, 170, 452, 0, 29)
        else:
            drawWinLine((249, 255, 188), 170, 40, 170, 452, 0, 29)
    elif mainList[0][1] == mainList[1][1] and mainList[1][1] == mainList[2][1]:
        postAnimation = True
        winLine = [[0, 1], [1, 1], [2, 1]]
        if mainList[0][1] == 1:
            drawWinLine((128, 128, 128), 296, 40, 296, 452, 0, 29)
        else:
            drawWinLine((249, 255, 188), 296, 40, 296, 452, 0, 29)
    elif mainList[0][2] == mainList[1][2] and mainList[1][2] == mainList[2][2]:
        postAnimation = True
        winLine = [[0, 2], [1, 2], [2, 2]]
        if mainList[0][2] == 1:
            drawWinLine((128, 128, 128), 422, 40, 422, 452, 0, 29)
        else:
            drawWinLine((249, 255, 188), 422, 40, 422, 452, 0, 29)
    elif mainList[0][0] == mainList[1][1] and mainList[1][1] == mainList[2][2]:
        k = 3
        postAnimation = True
        winLine = [[0, 0], [1, 1], [2, 2]]
        if mainList[0][0] == 1:
            drawWinLine((128, 128, 128), 90, 40, 502, 452, 29, 29)
        else:
            drawWinLine((249, 255, 188), 90, 40, 502, 452, 29, 29)
        k = 0
    elif mainList[0][2] == mainList[1][1] and mainList[1][1] == mainList[2][0]:
        k = 3
        postAnimation = True
        winLine = [[0, 2], [1, 1], [2, 0]]
        if mainList[0][2] == 1:
            drawWinLine((128, 128, 128), 502, 40, 90, 452, -29, 29)
        else:
            drawWinLine((249, 255, 188), 502, 40, 90, 452, -29, 29)

        k=0

    pg.display.update()
def postAnimate():
    global mainList, listOfSquares, winLinem, listOfMovingSquares

    for animation in range(1,13):
        screen.fill((20, 189, 172))
        hashWithOutAnimation()
        print(listOfSquares)
        counterI = 0
        counterJ = 0
        for i in mainList:
            for j in i:
                if not ([counterI,counterJ] in winLine):
                    if mainList[counterI][counterJ] == 1:
                        drawXWithOutAnimation(listOfSquares[counterI][counterJ])
                    if mainList[counterI][counterJ] == 2:
                        drawO(listOfSquares[counterI][counterJ])
                counterJ+=1
            counterJ=0
            counterI+=1
        if mainList[winLine[0][0]][winLine[0][1]] == 1:

           drawXWithOutAnimation([listOfSquares[winLine[0][0]][winLine[0][1]][0] + animation * 10 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][1] + animation * 10 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][2] + animation * 10 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][3] + animation * 10 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1]])
           pg.display.update()
           drawXWithOutAnimation([listOfSquares[winLine[1][0]][winLine[1][1]][0] + animation * 10 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][1] + animation * 10 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][2] + animation * 10 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][3] + animation * 10 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1]])
           pg.display.update()
           drawXWithOutAnimation([listOfSquares[winLine[2][0]][winLine[2][1]][0] + animation * 10 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][1] + animation * 10 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][2] + animation * 10 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][3] + animation * 10 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1]])
           pg.display.update()
        if mainList[winLine[0][0]][winLine[0][1]] == 2:
            drawO()
        clock.tick(60)
        pg.display.update()
screen = pg.display.set_mode((600, 600), 0, 32)
pg.display.set_caption("Tic tac toe")
screen.fill((20, 189, 172))
hash()
EndOfGame = 0
indexOfCell = []
winLine = list()
flag = 0

postAnimation = False
while not EndOfGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            EndOfGame  = 1
        if event.type == pg.MOUSEBUTTONUP:
            posOfClick = pg.mouse.get_pos()
            if (postAnimation == True) and not ( posOfClick[0] > 500 and posOfClick[0] < 600 and posOfClick[1] < 600 and posOfClick[1] > 500 ):
                posOfClick = (800,800)
            print(posOfClick)
            if posOfClick[0] < 230 and posOfClick[0] > 110:
                if posOfClick[1] < 180 and posOfClick[1] > 60:
                    indexOfCell = [0, 0]
                    square = [110,60,230,180]
                elif posOfClick[1] < 306 and posOfClick[1] >186 :
                    indexOfCell = [1,0]
                    square = [110, 186, 230, 306]
                elif posOfClick[1] < 432 and posOfClick[1] > 312:
                    indexOfCell = [2,0]
                    square = [110, 312, 230, 432]
            elif posOfClick[0] < 356 and posOfClick[0] > 236:
                if posOfClick[1] > 60 and posOfClick[1] < 180:
                    indexOfCell = [0, 1]
                    square = [236, 60, 356, 180]
                elif posOfClick[1] > 186 and posOfClick[1] < 306:
                    indexOfCell = [1, 1]
                    square = [236, 186, 356, 306]
                elif posOfClick[1] > 312 and posOfClick[1] < 432:
                    indexOfCell = [2, 1]
                    square = [236, 312, 356, 432]
            elif posOfClick[0] < 482 and posOfClick[0] > 362:
                if posOfClick[1] > 60 and posOfClick[1] < 180:
                    indexOfCell = [0, 2]
                    square = [362, 60, 482, 180]
                elif posOfClick[1] > 186 and posOfClick[1] < 306:
                    indexOfCell = [1, 2]
                    square = [362, 186, 482, 306]
                elif posOfClick[1] > 312 and posOfClick[1] < 432:
                    indexOfCell = [2, 2]
                    square = [362, 312, 482, 432]
            elif posOfClick[0] > 500 and posOfClick[0] < 600 and posOfClick[1] < 600 and posOfClick[1] > 500:
                indexOfCell=[]
                screen.fill((20, 189, 172))
                mainList = [['q', 'x', 'z'],
                            ['t', 'g', 'r'],
                            ['h', 'y', 'n']]
                hash()
                flag = 0
                postAnimation = False
            else:
                indexOfCell=[]
            if not(len(indexOfCell)==0) and (not(mainList[indexOfCell[0]][indexOfCell[1]] == 1 or mainList[indexOfCell[0]][indexOfCell[1]] == 2)):
                if flag == 0:
                    mainList[indexOfCell[0]][indexOfCell[1]] = 1
                    drawX(square)
                    listOfSquares[indexOfCell[0]][indexOfCell[1]] = square
                    flag = 1

                else:
                    mainList[indexOfCell[0]][indexOfCell[1]] = 2
                    listOfSquares[indexOfCell[0]][indexOfCell[1]] = square
                    drawO(square)
                    flag = 0
            if postAnimation == False:
                checkTheEndOfGame()
pg.quit()
sys.exit()