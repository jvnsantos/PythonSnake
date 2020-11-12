from constants import *

class Quadrado:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
        self.velx = 0
        self.vely = 0
        self.dim = [0,0, 0,grid_size, grid_size, grid_size,grid_size, 0]


    def setVel(self, newx, newy):
        self.velx = newx
        self.vely = newy

    def pos(self):
        return [self.dim[0] + self.x, self.dim[1] + self.y, self.dim[2] + self.x, self.dim[3] + self.y, self.dim[4] + self.x, self.dim[5] + self.y, self.dim[6] + self.x, self.dim[7] + self.y]

    def update(self):
        if(self.x>0 and self.x<width-grid_size):
            self.x += self.velx
        if(self.y>0 and self.y<heigh-grid_size):
            self.y += self.vely
        if(self.x==0 and self.velx>0):
            self.x += self.velx
        if(self.x==width-grid_size and self.velx<0):
            self.x += self.velx
        if(self.y==0 and self.vely >0):
            self.y += self.vely
        if(self.y==heigh-grid_size and self.vely <0):
            self.y += self.vely
