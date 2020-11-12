from tkinter import *
from constants import *
from tkinter.messagebox import showinfo
from square import Quadrado as quadrado
import random

class Game:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, bg=background_color, width=width, heigh=heigh)
        self.canvas.pack()

        s = quadrado(20, 20, snake_color)
        s1 = quadrado(20, 20 ,snake_color)
        s2 = quadrado(20, 20, snake_color)
        s3 = quadrado(20, 20, snake_color)

        f = quadrado(random.randint(grid_size,( width/grid_size))*grid_size - grid_size, random.randint(grid_size, (heigh/grid_size))*grid_size - grid_size, food_color)
        
        self.snake = [s, s1, s2, s3]
        self.food = [f]
        self.vel = [[20,0], [0,0], [0,0], [0,0]]

        self.window.bind("<Up>", self.moveUp)
        self.window.bind("<Down>", self.moveDown)
        self.window.bind("<Right>", self.moveRight)
        self.window.bind("<Left>", self.moveLeft)


    def moveUp(self, event):
        if(self.vel[0] != [0,20]):
            self.vel[0] = [0,-20]
    def moveDown(self, event):
        if(self.vel[0] != [0,-20]):
            self.vel[0] = [0,20]
    def moveRight(self, event):
        if(self.vel[0] != [-20,0]):
            self.vel[0] = [20,0]
    def moveLeft(self, event):
        if(self.vel[0] != [20,0]):
            self.vel[0] = [-20,0]


    def run(self):
        counter = 0
        points = 0
        while(True):
            self.canvas.delete('all')

            for i in range(len(self.vel)-1, 0, -1):
                self.vel[i] = self.vel[i-1]

            for i in range(len(self.vel)):
                self.snake[i].velx = self.vel[i][0]
                self.snake[i].vely = self.vel[i][1]

            if(self.snake[0].pos() == self.food[0].pos()):
                self.food[0].x = random.randint(grid_size, (width/grid_size))*grid_size-grid_size
                self.food[0].y = random.randint(grid_size, (heigh/grid_size))*grid_size-grid_size
                self.vel.append([0,0])
                self.snake.append(quadrado(self.snake[-1].x, self.snake[-1].y, self.snake[0].color))
                points = points + 1
                print(points)

            for s in self.snake:
                s.update()
                self.canvas.create_polygon(s.pos(), fill=s.color)
                
            for f in self.food:
                f.update()
                self.canvas.create_polygon(f.pos(), fill=f.color)
            
            for i in range(2, len(self.snake)  ):
                if(counter < 1):
                    counter += 1
                elif(self.snake[0].pos() == self.snake[i].pos()):
                    msg = "Pontuação: "+str(points)
                    showinfo(title="Game Over",message= msg)
                    exit()


            self.canvas.after(70)
            self.window.update_idletasks()
            self.window.update()
