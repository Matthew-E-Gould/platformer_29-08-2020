import pygame, sys
from player import *
from pygame.locals import *
#
import os
print(os.getcwd())

pygame.init()
pygame.display.set_caption('Platformy Boi')
clock = pygame.time.Clock()

# setting up window
X_SIZE = 1280
Y_SIZE = 720
WIN_SIZE = (X_SIZE, Y_SIZE)
screen = pygame.display.set_mode(WIN_SIZE,0,32)

FRAME_LIMIT = 1000;

xPos = 0
yPos = 0

player = Player()

# game loop
while True:
    screen.fill((0,0,0))

    player.pos = (player.pos[0] + 1, player.pos[1])
    if(player.pos[0] >= X_SIZE):
        player.pos = (0, player.pos[1] + 1)
        if(player.pos[1] >= Y_SIZE):
            player.pos = (0, 1)


    for event in pygame.event.get():
        if event.type == QUIT: # when X clicked on window
            print("Goodbye :(")
            pygame.quit()
            sys.exit()

    screen.blit(player.image, player.pos)

    pygame.display.update()
    clock.tick(FRAME_LIMIT) # frame limit
