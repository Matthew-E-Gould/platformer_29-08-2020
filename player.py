import pygame, sys
from pygame.locals import *

class Player:

    pos = (640, 360)
    momentum = (0, 0)
    image = None
    collisionRect = None
    canJump = True

    gravity = 9.81
    groundDrag = 0.5
    power = 10

    def __init__(self, image = "img\player.png", gravity = -9.81, power = 10):

        self.image = pygame.image.load(image)
        self.collisionRect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

        self.gravity = gravity

    def jump(self):
        if self.canJump:
            print("player Jump")
            self.canJump = False
            self.momentum = (self.momentum[0], self.momentum[1] - self.power)

    def land(self):
        print("player Landed")
        self.canJump = True
        self.momentum = (self.momentum[0], 0)

    def setXPos(self, x):
        self.pos = (x, self.pos[1])

    def setYPos(self, y):
        self.pos = (self.pos[0], y)

    def doMove(self, onGround):
        if onGround:
            self.pos = (self.pos[0] + self.momentum[0], self.pos[1] + gravity)
            self.momentum = (self.momentum[0] * groundDrag, self.momentum[1])
        else:
            self.pos = (self.pos[0] + self.momentum[0], self.pos[1] + gravity)
            self.momentum = (self.momentum[0], self.momentum[1] * 9.81)



    # jump
    # move?
    #
