import pygame, sys
from pygame.locals import *

class Player:

    pos = (640, 360)
    momentum = (0, 0)
    image = None
    collisionRect = None
    canJump = True
    screen = (0,0)

    gravity = 9.81
    groundDrag = 0.1
    power = 10
    maxSpeed = 10

    def __init__(self, screenSize, image = "img\player.png", gravity = -9.81, power = 10):

        self.screen = screenSize
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

    def doMove(self, onGround = True):
        if onGround:
            self.pos = (self.pos[0] + self.momentum[0], self.pos[1])
            self.momentum = (self.momentum[0] * self.groundDrag, self.momentum[1])
        else:
            self.pos = (self.pos[0] + self.momentum[0], self.pos[1] - self.gravity)
            self.momentum = (self.momentum[0], self.momentum[1] - 9.81)

        # x axis fix
        if(self.pos[0] < 0):
            self.pos = (0, self.pos[1])
        elif(self.pos[0] > self.screen[0]):
            self.pos = (self.screen[0], self.pos[1])

        # y axis fix
        if(self.pos[1] < 0):
            self.pos = (self.pos[0], 0)
        elif(self.pos[1] >= self.screen[1]):
            self.pos = (self.pos[0], self.screen[1])

    def moveLeft(self):
        newspeed = self.momentum[0] - 3
        if (newspeed < -self.maxSpeed): # correction
            newspeed = -self.maxSpeed
        self.momentum = (newspeed, self.momentum[1])



    def moveRight(self):
        newspeed = self.momentum[0] + 3
        if (newspeed > self.maxSpeed): # correction
            newspeed = self.maxSpeed
        self.momentum = (newspeed, self.momentum[1])

################################################################################

    def setXPos(self, x):
        self.pos = (x, self.pos[1])

    def setYPos(self, y):
        self.pos = (self.pos[0], y)

    def setXMomentum(self, x):
        self.momentum = (x, self.momentum[1])

    def setYMomentum(self, y):
        self.momentum = (self.momentum[0], y)
