import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Platformy Boi')
clock = pygame.time.Clock()

# setting up window
X_SIZE = 400
Y_SIZE = 400
WIN_SIZE = (X_SIZE, Y_SIZE)
screen = pygame.display.set_mode(WIN_SIZE,0,32)

FRAME_LIMIT = 1000;

player = pygame.image.load('img\player.png')

xPos = 0
yPos = 0

# game loop
while True:
    screen.fill((0,0,0))

    xPos += 1
    if(xPos >= X_SIZE):
        xPos = 0
        yPos += 1
        if(yPos >= Y_SIZE):
            xPos = 0
            yPos = 0


    for event in pygame.event.get():
        if event.type == QUIT: # when X clicked on window
            print("Goodbye :(")
            pygame.quit()
            sys.exit()

    screen.blit(player, (xPos, yPos))

    pygame.display.update()
    clock.tick(FRAME_LIMIT) # frame limit
