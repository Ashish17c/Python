from argparse import Action
from turtle import pos, speed, screen
import pgzrun
from g import draw

from g2 import HEIGHT, WIDTH

class Player(Action):
    speed = 3
    def move(self):

        if keyboard.left:

            self.x -= self.speed
        if keyboard.right:
            self.x += speed
        if keyboard.up:
            self.y -= speed
        if keyboard.down:
           self.y += self.speed
    # boundary control
    def boundary_check(self):
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
           self.x = WIDTH
        if self.y > HEIGHT:
           self.y = 0
        if self.y < 0:
           self.y = HEIGHT

class Player(Actor):
    pass
class Enemy(Actor):
    pass

p = Player('character_0000',pos = (200,100))

def draw():
    screen.clear()
    p.draw()

def update():
    p.move()
    p.boundary_check()

pgzrun.go()                                                                          

