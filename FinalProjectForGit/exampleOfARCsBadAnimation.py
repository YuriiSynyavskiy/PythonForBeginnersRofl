import pygame as pg, sys, math, time
GREENBACKGROUND = (20 , 189, 172)
WHITE           = (249, 255, 188)
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600), 0, 32)
pg.display.set_caption("Bad arc's animation")
screen.fill(GREENBACKGROUND)
pg.display.update()
EndOfGame = 0
#arc(surface, color, rect, start_angle, stop_angle)
def animation_of_arc():
    for i in range(1,40):
        screen.fill(GREENBACKGROUND) #doesn't matter
        pg.draw.arc(screen, WHITE, [100,100,300,300], math.pi/2,  math.pi/16*i, 10)
        pg.display.update()
        clock.tick(60)
animation_of_arc()
while not EndOfGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            EndOfGame  = 1
        if event.type == pg.MOUSEBUTTONUP:
            animation_of_arc()
pg.quit()
sys.exit()