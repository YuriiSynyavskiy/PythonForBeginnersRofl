import pygame


class Car:
    carWidth = 30
    carHeight = 60

    def __init__(self, color, surface):
        self.Color = color
        self.Surface = surface
        self.x = surface.get_width() / 2 - Car.carWidth / 2
        self.y = 600

    def moveCar(self):
        pygame.draw.rect(self.Surface, self.Color, (self.x, self.y,
                                                    Car.carWidth, Car.carHeight))
        self.y -= 3
        if self.y < -Car.carHeight:
            self.y = windowHeight


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
windowWidth = 800
windowHeight = 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('not my first game')
done = False

leftSurface = pygame.Surface((windowWidth / 2, windowHeight))
leftSurface.fill(WHITE)
rightSurface = pygame.Surface((windowWidth / 2, windowHeight))
rightSurface.fill(BLACK)

leftCar = Car(BLACK, leftSurface)
rightCar = Car(WHITE, rightSurface)
screen.blit(leftSurface, (0, 0))
screen.blit(rightSurface, (windowWidth / 2, 0))
activeLeftSurface = 0
activeRightSurface = 0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.pos[0] < windowWidth / 2:
                activeLeftSurface = 1
                activeRightSurface = 0
            if event.pos[0] > windowWidth / 2:
                activeRightSurface = 1
                activeLeftSurface = 0
    if activeLeftSurface:
        leftSurface.fill(WHITE)
        leftCar.moveCar()
        screen.blit(leftSurface, (0, 0))
    elif activeRightSurface:
        rightSurface.fill(BLACK)
        rightCar.moveCar()
        screen.blit(rightSurface, (windowWidth / 2, 0))
    pygame.display.update()
    pygame.time.delay(20)
pygame.quit()

