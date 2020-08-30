import pygame, sys

from pygame.locals import *

from player import *
from level import *

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

FRAME_LIMIT = 144

xPos = 0
yPos = 0

player = Player(WIN_SIZE)

# game loop
while True:
    screen.fill((0,0,0)) # make screen black, dont put any rendering abouve here :):):)
    movePressed = pygame.key.get_pressed()
    if movePressed[pygame.K_a]:
        player.moveLeft()
    if movePressed[pygame.K_d]:
        player.moveRight()
    if movePressed[pygame.K_w]:
        player.setYPos(player.pos[1] - 2)
    if movePressed[pygame.K_s]:
        player.setYPos(player.pos[1] + 2)
    if movePressed[pygame.K_SPACE]:
        player.jump()

    for event in pygame.event.get():
        if event.type == QUIT: # when X clicked on window
            print("Goodbye :(")
            pygame.quit()
            sys.exit()

    # update and render player
    player.doMove()
    screen.blit(player.image, player.pos)

    pygame.display.update()
    clock.tick(FRAME_LIMIT) # frame limit

    ############################################################################
    # DEBUG OUTPUTS
    print("Vel: " + str(player.velocity))
    print("Pos: " + str(player.pos))
    print("Jmp: " + str(player.canJump))
