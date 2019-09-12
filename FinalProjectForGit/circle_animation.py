import pygame as pg, sys, math, time
'''CONSTANTS'''
k=0
GREY            = (128, 128, 128)
GREENOFHASH     = (13 , 161, 146)
GREENBACKGROUND = (20 , 189, 172)
WHITE           = (249, 255, 188)
FOREVERWHITE = (249, 255, 188)
coordinatesOfVerticalLines =   {'upPartOfFirstVerticalLine':{'startPos':(232, 240), 'endPos':(232, 60)}, 'downPartOfFirstVerticalLine':{'startPos':(232, 250), 'endPos':(232, 432)}, 'upPartOfSecondVerticalLine':{'startPos':(360, 240), 'endPos':(360, 60)}, 'downPartOfSecondVerticalLine':{'startPos':(360, 250), 'endPos':(360, 432)}}
coordinatesOfHorizontalLines = {'upPartOfFirstHorizontalLine': {'startPos':(290, 182), 'endPos':(110, 182)}, 'downPartOfFirstHorizontalLine':{'startPos':(300, 182), 'endPos':(482, 182)}, 'upPartOfSecondHorizontalLine':{'startPos':(290, 308), 'endPos':(110, 308)}, 'downPartOfSecondHorizontalLine':{'startPos':(300, 308), 'endPos':(482, 308)}}
squareOfWinLineForAnimation = [None, None, None, None]
x1TicksOfWinLineForAnimation = 0
x2TicksOfWinLineForAnimation = 0
y1TicksOfWinLineForAnimation = 0
y2TicksOfWinLineForAnimation = 0
coordinatesOfPallete={ (0,0,24,24):(0,0,0),(25,0,49,24):(128,64,0),(50,0,74,24):(254,0,0),(75,0,99,24):(254,106,0),(100,0,124,24):(255,216,0),(125,0,149,24):(0,255,1),
                       (0,25,24,49):(84,84,84),(25,25,49,49):(64,31,0),(50,25,74,49):(128,0,1),(75,25,99,49):(128,52,0),(100,25,124,49):(128,107,0),(125,25,149,49):(1,127,1),
                       (0,50,24,74):(168,168,168),(25,50,49,74):(1,255,255),(50,50,74,74):(0,148,254),(75,50,99,74):(0,38,255),(100,50,124,74):(177,0,254),(125,50,149,74):(255,0,110),
                       (0,75,24,99):(255,255,255),(25,75,49,99):(1,127,126),(50,75,74,99):(0,73,126),(75,75,99,99):(0,18,128),(100,75,124,99):(89,0,128),(125,75,149,99):(127,0,55)}

mainList = [['q','x','z'],                  #for values
            ['t','g','r'],
            ['h','y','n']]
listOfSquares =  [[None, None, None],                   #for coordinates of squares
                  [None, [236, 186, 356, 306], None],
                  [None, None, None]]
listOfMovingSquares = [[[1,1],[0,1],[-1,1]],
                       [[1,0],[0,0],[-1,0]],
                       [[1,-1],[0,-1],[-1,-1]]]
restartPicture = pg.image.load(r'C:\Users\yura\Desktop\finalProject\restartIcon2.png')        # restartIcon image
adminToolsPicture = pg.image.load(r'C:\Users\yura\Desktop\finalProject\adminTools.png')
colorChart = pg.image.load(r'C:\Users\yura\Desktop\finalProject\pallete.png')
acceptIcon = pg.image.load(r'C:\Users\yura\Desktop\finalProject\accept.png')

'''END OF CONSTANTS'''



'''FUNCTIONS'''
def restartGame():
    global counterForDraw, indexOfCell, mainList, flag, postAnimation
    counterForDraw = 0
    indexOfCell = []
    screen.fill(GREENBACKGROUND)
    mainList = [['q', 'x', 'z'],
                ['t', 'g', 'r'],
                ['h', 'y', 'n']]
    hash()
    screen.blit(restartPicture, (500, 500))
    screen.blit(adminToolsPicture, (430,515))
    flag = 0
    postAnimation = False
def hash():
    for i in range(1,17):
        #pg.draw.line(screen, (13, 161, 146), (232, 60), (232,432),5)
        pg.draw.line(screen, GREENOFHASH, (232,240), (232,240-i*11.2), 5)
        pg.draw.line(screen, GREENOFHASH, (232,250), (232,250+i*11.2), 5)
        #pg.draw.line(screen, (13, 161, 146), (360, 60), (360, 432),5)
        pg.draw.line(screen, GREENOFHASH, (360, 240), (360, 240 - i * 11.2), 5)   #animation
        pg.draw.line(screen, GREENOFHASH, (360, 250), (360, 250 + i * 11.2), 5)

        #pg.draw.line(screen, (13, 161, 146), (110, 182), (482, 182) ,5 )
        pg.draw.line(screen, GREENOFHASH, (290, 182), (290-11.4*i, 182), 5)
        pg.draw.line(screen, GREENOFHASH, (300, 182), (300+11.4*i, 182), 5)

        #pg.draw.line(screen, (13, 161, 146), (110, 308), (482, 308), 5)
        pg.draw.line(screen, GREENOFHASH, (290, 308), (290 - 11.4 * i, 308), 5)
        pg.draw.line(screen, GREENOFHASH, (300, 308), (300 + 11.4 * i, 308), 5)
        pg.display.update()
        clock.tick(60)


'''def hashWithOutAnimation():
    pg.draw.line(screen, (13, 161, 146), (232, 240), (232, 60), 5)
    pg.draw.line(screen, (13, 161, 146), (232, 250), (232, 432), 5)

    pg.draw.line(screen, (13, 161, 146), (360, 240), (360, 60), 5)
    pg.draw.line(screen, (13, 161, 146), (360, 250), (360, 432), 5)

    pg.draw.line(screen, (13, 161, 146), (290, 182), (110, 182), 5)
    pg.draw.line(screen, (13, 161, 146), (300, 182), (482, 182), 5)

    pg.draw.line(screen, (13, 161, 146), (290, 308), (110, 308), 5)
    pg.draw.line(screen, (13, 161, 146), (300, 308), (482, 308), 5)'''
def hashWithOutAnimation(variableForDecreasingHash = 0, WIDTH = 5):
    pg.draw.line(screen, GREENOFHASH, coordinatesOfVerticalLines['upPartOfFirstVerticalLine']['startPos'], (coordinatesOfVerticalLines['upPartOfFirstVerticalLine']['endPos'][0], coordinatesOfVerticalLines['upPartOfFirstVerticalLine']['endPos'][1]+variableForDecreasingHash), WIDTH)
    pg.draw.line(screen, GREENOFHASH, coordinatesOfVerticalLines['downPartOfFirstVerticalLine']['startPos'], (coordinatesOfVerticalLines['downPartOfFirstVerticalLine']['endPos'][0], coordinatesOfVerticalLines['downPartOfFirstVerticalLine']['endPos'][1] - variableForDecreasingHash), WIDTH)

    pg.draw.line(screen, GREENOFHASH, coordinatesOfVerticalLines['upPartOfSecondVerticalLine']['startPos'],(coordinatesOfVerticalLines['upPartOfSecondVerticalLine']['endPos'][0], coordinatesOfVerticalLines['upPartOfSecondVerticalLine']['endPos'][1]+variableForDecreasingHash), WIDTH)
    pg.draw.line(screen, GREENOFHASH, coordinatesOfVerticalLines['downPartOfSecondVerticalLine']['startPos'], (coordinatesOfVerticalLines['downPartOfSecondVerticalLine']['endPos'][0], coordinatesOfVerticalLines['downPartOfSecondVerticalLine']['endPos'][1] - variableForDecreasingHash), WIDTH)

    pg.draw.line(screen, GREENOFHASH, coordinatesOfHorizontalLines['upPartOfFirstHorizontalLine']['startPos'], (coordinatesOfHorizontalLines['upPartOfFirstHorizontalLine']['endPos'][0] + variableForDecreasingHash, coordinatesOfHorizontalLines['upPartOfFirstHorizontalLine']['endPos'][1]), WIDTH)
    pg.draw.line(screen, GREENOFHASH, coordinatesOfHorizontalLines['downPartOfFirstHorizontalLine']['startPos'], (coordinatesOfHorizontalLines['downPartOfFirstHorizontalLine']['endPos'][0] - variableForDecreasingHash, coordinatesOfHorizontalLines['downPartOfFirstHorizontalLine']['endPos'][1]), WIDTH)

    pg.draw.line(screen, GREENOFHASH, coordinatesOfHorizontalLines['upPartOfSecondHorizontalLine']['startPos'], (coordinatesOfHorizontalLines['upPartOfSecondHorizontalLine']['endPos'][0] + variableForDecreasingHash, coordinatesOfHorizontalLines['upPartOfSecondHorizontalLine']['endPos'][1]), WIDTH)
    pg.draw.line(screen, GREENOFHASH, coordinatesOfHorizontalLines['downPartOfSecondHorizontalLine']['startPos'], (coordinatesOfHorizontalLines['downPartOfSecondHorizontalLine']['endPos'][0] - variableForDecreasingHash, coordinatesOfHorizontalLines['downPartOfSecondHorizontalLine']['endPos'][1]), WIDTH)
def drawX(coordinatesOfSquare):
    for i in range(1,10):
        pg.draw.line(screen, GREY, (coordinatesOfSquare[0]+20, coordinatesOfSquare[1] + 20), (coordinatesOfSquare[0]+20 + 9*i, coordinatesOfSquare[1] + 20 + 9*i), 8)
        pg.draw.line(screen, GREY, (coordinatesOfSquare[0]+20, coordinatesOfSquare[1] + 10 + 9*10), (coordinatesOfSquare[0]+20 + 9*i , coordinatesOfSquare[1] + 10  + 9*10 - 9*i ), 8)
        pg.display.update()
        clock.tick(60)

def drawXWithOutAnimation(coordinatesOfSquare):
    pg.draw.line(screen, GREY, (coordinatesOfSquare[0] + 20, coordinatesOfSquare[1] + 20),
                 (coordinatesOfSquare[0] + 20 + 9 * 9, coordinatesOfSquare[1] + 20 + 9 * 9), 8)
    pg.draw.line(screen, GREY, (coordinatesOfSquare[0] + 20, coordinatesOfSquare[1] + 10 + 9 * 10),
                 (coordinatesOfSquare[0] + 20 + 9 * 9, coordinatesOfSquare[1] + 10 + 9 * 10 - 9 * 9), 8)
    pg.display.update()
def drawXForWinningAnimation(coordinatesOfSquare,i,width):
    pg.draw.line(screen, GREY, (coordinatesOfSquare[0] + 20 -i, coordinatesOfSquare[1] + 20-i),
                 (coordinatesOfSquare[0] + 20 + 9 * 9 +i, coordinatesOfSquare[1] + 20 + 9 * 9 +i ), 8+width)
    pg.draw.line(screen, GREY, (coordinatesOfSquare[0] + 20 -i, coordinatesOfSquare[1] + 10 + 9 * 10+i),
                 (coordinatesOfSquare[0] + 20 + 9 * 9+i, coordinatesOfSquare[1] + 10 + 9 * 10 - 9 * 9-i), 8+width)
def drawO(coordinatesOfSquare, color = WHITE, radius = 0, width = 4):
    ''''(242, 235, 211)'''
    pg.draw.circle(screen, WHITE, (int((coordinatesOfSquare[0]+coordinatesOfSquare[2])/2), int((coordinatesOfSquare[1]+coordinatesOfSquare[3]) /2)), radius + 45, width)
    pg.display.update()
def renderText(color, surfaceCoordinates, text = 'You Won!!!', size = 80):
    pg.font.init()
    myfont = pg.font.Font(r'C:\Users\yura\Desktop\finalProject\Righteous\Righteous-Regular.ttf', size)  #way_to_font
    if text == 'DRAW':
        textsurface1 = myfont.render('DR', False, GREY)
        textsurface2 = myfont.render('AW', False, WHITE)
        screen.blit(textsurface1, (surfaceCoordinates[0]+100,  surfaceCoordinates[1] ))
        screen.blit(textsurface2, (surfaceCoordinates[0]+200, surfaceCoordinates[1] ))
    else:
        textsurface = myfont.render(text, False, color)
        screen.blit(textsurface, surfaceCoordinates)
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
def checkTheEndOfGame():
    global mainList, countForCells, EndOfGame, k, postAnimation, winLine, squareOfWinLineForAnimation, x1TicksOfWinLineForAnimation,x2TicksOfWinLineForAnimation, y1TicksOfWinLineForAnimation, y2TicksOfWinLineForAnimation, counterForDraw
    if mainList[0][0] == mainList[0][1] and mainList[0][1] == mainList[0][2]:
        postAnimation = True
        winLine = [[0,0],[0,1],[0,2]]
        if mainList[0][0] == 1:
            drawWinLine(GREY, 90, 120, 502, 120, 29, 0)
        else:
            drawWinLine(WHITE, 90, 120, 502, 120, 29, 0)
        # for animation of win Line
        squareOfWinLineForAnimation = [90, 120, 502, 120]
        x1TicksOfWinLineForAnimation = 1
        x2TicksOfWinLineForAnimation = -1
        y1TicksOfWinLineForAnimation = 1
        y2TicksOfWinLineForAnimation = 1        #
        postAnimate()
    elif mainList[1][0] == mainList[1][1] and mainList[1][1] == mainList[1][2]:
        postAnimation = True
        winLine = [[1, 0], [1, 1], [1, 2]]
        if mainList[1][0] == 1:
            drawWinLine(GREY, 90, 246, 502, 246, 29, 0)
        else:
            drawWinLine(WHITE, 90, 246, 502, 246, 29, 0)
     # for animation of WIn Line
        squareOfWinLineForAnimation = [ 90, 246, 502, 246]
        x1TicksOfWinLineForAnimation = 1
        x2TicksOfWinLineForAnimation = -1
        y1TicksOfWinLineForAnimation = 0
        y2TicksOfWinLineForAnimation = 0         #
        postAnimate()
    elif mainList[2][0] == mainList[2][1] and mainList[2][1] == mainList[2][2]:
        postAnimation = True
        winLine = [[2, 0], [2, 1], [2, 2]]
        if mainList[2][0] == 1:
            drawWinLine(GREY, 90, 373, 502, 373, 29, 0)
        else:
            drawWinLine(WHITE, 90, 373, 502, 373, 29, 0)
        # for animation of WIn Line
        squareOfWinLineForAnimation = [90, 373, 502, 373]
        x1TicksOfWinLineForAnimation = 1
        x2TicksOfWinLineForAnimation = -1
        y1TicksOfWinLineForAnimation = -1
        y2TicksOfWinLineForAnimation = -1           #
        postAnimate()
    elif mainList[0][0] == mainList[1][0] and mainList[1][0] == mainList[2][0]:
        postAnimation = True
        winLine = [[0, 0], [1, 0], [2, 0]]
        if mainList[0][0] == 1:
            drawWinLine(GREY, 170, 40, 170, 452, 0, 29)
        else:
            drawWinLine(WHITE, 170, 40, 170, 452, 0, 29)
        squareOfWinLineForAnimation = [170, 40, 170, 452]
        # for animation of WIn Line
        x1TicksOfWinLineForAnimation = 1
        x2TicksOfWinLineForAnimation = 1
        y1TicksOfWinLineForAnimation = -1
        y2TicksOfWinLineForAnimation = -1  #
        postAnimate()
    elif mainList[0][1] == mainList[1][1] and mainList[1][1] == mainList[2][1]:
        postAnimation = True
        winLine = [[0, 1], [1, 1], [2, 1]]
        if mainList[0][1] == 1:
            drawWinLine(GREY, 296, 40, 296, 452, 0, 29)
        else:
            drawWinLine(WHITE, 296, 40, 296, 452, 0, 29)
        squareOfWinLineForAnimation = [296, 40, 296, 452]
        postAnimate()
    elif mainList[0][2] == mainList[1][2] and mainList[1][2] == mainList[2][2]:
        postAnimation = True
        winLine = [[0, 2], [1, 2], [2, 2]]
        if mainList[0][2] == 1:
            drawWinLine(GREY, 422, 40, 422, 452, 0, 29)
        else:
            drawWinLine(WHITE, 422, 40, 422, 452, 0, 29)
        squareOfWinLineForAnimation = [422, 40, 422, 452]
        postAnimate()
    elif mainList[0][0] == mainList[1][1] and mainList[1][1] == mainList[2][2]:
        k = 3
        postAnimation = True
        winLine = [[0, 0], [1, 1], [2, 2]]
        if mainList[0][0] == 1:
            drawWinLine(GREY, 90, 40, 502, 452, 29, 29)
        else:
            drawWinLine(WHITE, 90, 40, 502, 452, 29, 29)
        squareOfWinLineForAnimation = [90, 40, 502, 452]
        k = 0
        postAnimate()
    elif mainList[0][2] == mainList[1][1] and mainList[1][1] == mainList[2][0]:
        k = 3
        postAnimation = True
        winLine = [[0, 2], [1, 1], [2, 0]]
        if mainList[0][2] == 1:
            drawWinLine(GREY, 502, 40, 90, 452, -29, 29)
        else:
            drawWinLine(WHITE, 502, 40, 90, 452, -29, 29)
        squareOfWinLineForAnimation = [502, 40, 90, 452]
        k=0
        postAnimate()

    pg.display.update()
    if postAnimation == True:
        counterForDraw=0
'''for post animation'''
def postAnimate():
    global mainList, listOfSquares, winLine, listOfMovingSquares
    time.sleep(0.6)
    for animation in range(1,16):
        screen.fill(GREENBACKGROUND)
        hashWithOutAnimation()
        counterI = 0
        counterJ = 0
        ''' redrawing all values in hash without win combination'''
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
        '''moving win X's in center block of hash'''
        if mainList[winLine[0][0]][winLine[0][1]] == 1:

           drawXWithOutAnimation([listOfSquares[winLine[0][0]][winLine[0][1]][0] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][1] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][2] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][3] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1]])
           pg.display.update()
           drawXWithOutAnimation([listOfSquares[winLine[1][0]][winLine[1][1]][0] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][1] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][2] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][3] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1]])
           pg.display.update()
           drawXWithOutAnimation([listOfSquares[winLine[2][0]][winLine[2][1]][0] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][1] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][2] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][3] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1]])
           pg.display.update()
        '''moving win O's in center block of hash'''
        if mainList[winLine[0][0]][winLine[0][1]] == 2:
            drawO([listOfSquares[winLine[0][0]][winLine[0][1]][0] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][1] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][2] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][0],
                                  listOfSquares[winLine[0][0]][winLine[0][1]][3] + animation * 8 * listOfMovingSquares[winLine[0][0]][winLine[0][1]][1]])
            pg.display.update()
            drawO([listOfSquares[winLine[1][0]][winLine[1][1]][0] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][1] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][2] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][0],
                                  listOfSquares[winLine[1][0]][winLine[1][1]][3] + animation * 8 * listOfMovingSquares[winLine[1][0]][winLine[1][1]][1]])
            pg.display.update()
            drawO([listOfSquares[winLine[2][0]][winLine[2][1]][0] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][1] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][2] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][0],
                                  listOfSquares[winLine[2][0]][winLine[2][1]][3] + animation * 8 * listOfMovingSquares[winLine[2][0]][winLine[2][1]][1]])
            pg.display.update()
        clock.tick(59)
        pg.display.update()
    screen.fill(GREENBACKGROUND)
    hashWithOutAnimation()
    counterI = 0
    counterJ = 0
    ''' redrawing all values in hash without win combination'''
    for i in mainList:
        for j in i:
            if not ([counterI, counterJ] in winLine):
                if mainList[counterI][counterJ] == 1:
                    drawXWithOutAnimation(listOfSquares[counterI][counterJ])
                if mainList[counterI][counterJ] == 2:
                    drawO(listOfSquares[counterI][counterJ])
            counterJ += 1
        counterJ = 0
        counterI += 1
    '''last frame of animation in center block of hash'''
    if mainList[winLine[0][0]][winLine[0][1]] == 1:
        drawXWithOutAnimation(listOfSquares[1][1])
    elif mainList[winLine[0][0]][winLine[0][1]] == 2:
        drawO(listOfSquares[1][1])
    pg.display.update()
    screen.fill(GREENBACKGROUND)
    hashWithOutAnimation()
    pg.display.update()
    width = 5
    '''object's increasing animation from center cell of hash'''
    for height in range(10,100,3):
        screen.fill(GREENBACKGROUND)
        if height<97:
            hashWithOutAnimation((height-10)*2, 5)
        if mainList[winLine[0][0]][winLine[0][1]] == 1:
            drawXForWinningAnimation(listOfSquares[1][1], height, width)
        elif mainList[winLine[0][0]][winLine[0][1]] == 2:
            drawO(listOfSquares[1][1], WHITE, height, width)

        width+=1  #increasing width of object
        pg.display.update()
        clock.tick(59)
    '''animation of text'''
    for move in range(0,150,10):
        screen.fill(GREENBACKGROUND)
        if mainList[winLine[0][0]][winLine[0][1]] == 1:
            drawXForWinningAnimation(listOfSquares[1][1], 100, width)
        elif mainList[winLine[0][0]][winLine[0][1]] == 2:
            drawO(listOfSquares[1][1], WHITE, 100, width)
        renderText(GREY, (125,550-move)) if mainList[winLine[0][0]][winLine[0][1]] == 1 else renderText(WHITE, (125,550-move))
        pg.display.update()
        clock.tick(59)
    time.sleep(2)
    restartGame()
'''function for draw animation'''
def draw_condition_animation():
    global mainList, listOfSquares, winLine, listOfMovingSquares
    width = 5
    for height in range(10, 100, 3):
        screen.fill(GREENBACKGROUND)
        if height < 97:
            hashWithOutAnimation((height - 10) * 2, 5)
            drawXForWinningAnimation([listOfSquares[1][1][0] -150,listOfSquares[1][1][1], listOfSquares[1][1][2] -150, listOfSquares[1][1][3]] , height, width)   # 150 just value for animation
            drawO([listOfSquares[1][1][0] +150,listOfSquares[1][1][1], listOfSquares[1][1][2] +150, listOfSquares[1][1][3]], WHITE, height, width)                # same situation

        width += 1    # increasing width of object
        pg.display.update()
        clock.tick(59)
    for move in range(0, 150, 10):
        screen.fill(GREENBACKGROUND)
        drawXForWinningAnimation([listOfSquares[1][1][0] - 150, listOfSquares[1][1][1], listOfSquares[1][1][2] - 150, listOfSquares[1][1][3]], 100, width)      # 150 just value for animation
        drawO([listOfSquares[1][1][0] + 150, listOfSquares[1][1][1], listOfSquares[1][1][2] + 150, listOfSquares[1][1][3]], WHITE, 100, width)                  # same situation
        renderText(WHITE, ( 125, 550 - move), 'DRAW')
        pg.display.update()
        clock.tick(59)
    time.sleep(2)
    restartGame()
def blit_charts():
    screen.fill(GREENBACKGROUND)
    drawXWithOutAnimation([50,40,150,140])
    screen.blit(colorChart, (300, 50))
    drawO([50,190,150,290])
    screen.blit(colorChart, (300, 200))
    renderText(FOREVERWHITE,[0,340], 'B-G', 100)
    screen.blit(colorChart, (300, 350))
    renderText(GREENOFHASH,[0,490], 'Hash', 100)
    screen.blit(colorChart, (300, 500))
    screen.blit(acceptIcon, (530,530))
def checkColor(position):
    for key in coordinatesOfPallete:
        if position[0]>=key[0] and position[0]<= key[2] and position[1]>=key[1] and position[1]<= key[3]:
            return coordinatesOfPallete[key]
'''END OF FUNCTIONS'''

                                                                                        # MAIN/ START OF PROGRAMM



pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600), 0, 32)
pg.display.set_caption("Tic tac toe")
screen.fill(GREENBACKGROUND)
hash()
screen.blit(restartPicture, (500, 500))
screen.blit(adminToolsPicture, (430, 515))
pg.display.update()
EndOfGame = 0
indexOfCell = []
winLine = list()
flag = 0
valueForPallete = 0
counterForDraw = 0
postAnimation = False
choosingColors = 1
while not EndOfGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            EndOfGame  = 1
        if event.type == pg.MOUSEBUTTONUP:
            posOfClick = pg.mouse.get_pos()
            '''Analyse position of click and record coordinates of this square  '''
            if (postAnimation == True) and not ( posOfClick[0] > 500 and posOfClick[0] < 600 and posOfClick[1] < 600 and posOfClick[1] > 500 ):
                posOfClick = (800,800)
            if counterForDraw == 9 and not ( posOfClick[0] > 500 and posOfClick[0] < 600 and posOfClick[1] < 600 and posOfClick[1] > 500 ):
                posOfClick = (800,800)
            if not choosingColors:
                if posOfClick[1]>=50 and posOfClick[1]<=150 and posOfClick[0]>=300 and posOfClick[0]<=450:
                    valueForPallete = (posOfClick[0]-300, posOfClick[1]-50)
                    color = checkColor(valueForPallete)
                    GREY = color
                    blit_charts()
                elif posOfClick[1]>=200 and posOfClick[1]<=300 and posOfClick[0]>=300 and posOfClick[0]<=450:
                    valueForPallete = (posOfClick[0]-300, posOfClick[1]-200)
                    color = checkColor(valueForPallete)
                    WHITE = color
                    blit_charts()
                elif posOfClick[1]>=350 and posOfClick[1]<=450 and posOfClick[0]>=300 and posOfClick[0]<=450:
                    valueForPallete = (posOfClick[0]-300, posOfClick[1]-350)
                    color = checkColor(valueForPallete)
                    GREENBACKGROUND = color
                    blit_charts()
                elif posOfClick[1]>=500 and posOfClick[1]<=600 and posOfClick[0]>=300 and posOfClick[0]<=450:
                    valueForPallete = (posOfClick[0]-300, posOfClick[1]-500)
                    color = checkColor(valueForPallete)
                    GREENOFHASH = color
                    blit_charts()
                elif posOfClick[0]>500 and posOfClick[0]<600 and posOfClick[1]>500 and posOfClick[1]<600:
                    choosingColors = 1
                    restartGame()
            elif posOfClick[0]>400 and posOfClick[0]<500 and posOfClick[1]>500 and  posOfClick[1] < 600:
                choosingColors = 0
                blit_charts()
            elif posOfClick[0] < 230 and posOfClick[0] > 110:
                if posOfClick[1] < 180 and posOfClick[1] > 60 :
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
                restartGame()
            else:
                indexOfCell=[]
            if not(len(indexOfCell)==0) and (not(mainList[indexOfCell[0]][indexOfCell[1]] == 1 or mainList[indexOfCell[0]][indexOfCell[1]] == 2) )and choosingColors:
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
                counterForDraw+=1
            if postAnimation == False:
                checkTheEndOfGame()
            if counterForDraw == 9 and not posOfClick==(800,800):
                draw_condition_animation()
pg.quit()
sys.exit()