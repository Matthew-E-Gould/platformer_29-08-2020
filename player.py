import pygame, sys
from pygame.locals import *

class Player:

    pos = (0, 0)
    momentum = (0, 0)
    image = None
    collisionRect = None
    canJump = True

    gravity = -9.81

    def __init__(self, image = "img\player.png", gravity = -9.81):

        self.image = pygame.image.load(image)
        self.collisionRect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

        self.gravity = gravity
