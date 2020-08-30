import pygame, sys
from pygame.locals import *

class Player:

    pos = (640, 360)
    velocity = (0, 0)
    image = None
    collisionRect = None
    screen = (0,0)
    canJump = True
    inAir = False

    gravity = 9.81
    groundDrag = 0.05
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
            self.velocity = (self.velocity[0], self.velocity[1] - 30)

    def land(self):
        print("player Landed")
        self.canJump = True
        self.velocity = (self.velocity[0], 0)

    def doMove(self):
        if self.inAir:
            self.pos = (self.pos[0] + self.velocity[0], self.pos[1] - self.gravity)
            self.velocity = (self.velocity[0], self.velocity[1] - 9.81)
        else:
            self.pos = (self.pos[0] + self.velocity[0], self.pos[1])
            self.velocity = (self.velocity[0] * (1-self.groundDrag), self.velocity[1])

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
        newspeed = self.velocity[0] - 1
        if (newspeed < -self.maxSpeed): # correction
            newspeed = -self.maxSpeed
        self.velocity = (newspeed, self.velocity[1])



    def moveRight(self):
        newspeed = self.velocity[0] + 1
        if (newspeed > self.maxSpeed): # correction
            newspeed = self.maxSpeed
        self.velocity = (newspeed, self.velocity[1])

################################################################################

    def setXPos(self, x):
        self.pos = (x, self.pos[1])

    def setYPos(self, y):
        self.pos = (self.pos[0], y)

    def setXvelocity(self, x):
        self.velocity = (x, self.velocity[1])

    def setYvelocity(self, y):
        self.velocity = (self.velocity[0], y)
