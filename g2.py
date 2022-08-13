from lib2to3 import pgen2
from turtle import Screen
import pgzrun
HEIGHT = 500
WIDTH = 800
box = Rect((50,50),(100,100))
box = Rect((450,50), (100,100))
def draw():
    Screen.fill('white')
    Screen.draw.rect(box, 'red')
def update():
    box.x += 3
    if box.x > WIDTH:
       box.x = 0

    box2.x -= 3
    if box2.x < 0:
        box2.x = WIDTH

    if box2.colliderect(box):
        print("Collision")
        box.x -= 1
        box2.x -= -2
pgzrun.go()