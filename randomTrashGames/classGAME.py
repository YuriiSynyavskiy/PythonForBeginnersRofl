import pygame

pygame.init()
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first game")
# clock = pygame.time.Clock()

x = 50
y = 50
width = 40
height = 60
vol = 5

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if x>WINDOW_WIDTH-width - 15:
        x=WINDOW_WIDTH-width
    if x<0:
        x=0+10
    if y>WINDOW_HEIGHT - height - 15:
        y=WINDOW_HEIGHT-height
    if y<0:
        y=0+10


    if keys[pygame.K_LEFT]:
        x = x - vol
    if keys[pygame.K_RIGHT]:
        x = x + vol
    if keys[pygame.K_UP]:
        y = y - vol
    if keys[pygame.K_DOWN]:
        y = y + vol

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), [x, y, width, height])
    pygame.display.update()
    clock.tick(60)