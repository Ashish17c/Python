from turtle import width
import pgzrun

HEIGHT = 500
WIDTH = 800
#Rect=0
#Screen=0
#box=0
box = Actor('character_0005',(50,50),(100,100))
box = Actor((450,50), (100,100))
def draw():
    screen.fill('white')
    sun.draw()
    #screen.draw.(box,'red')
def update():
    box.x += 3
    if box.x > width:
       box.x = 0

    box.x -= 3
    if box.x < 0:
        box.x = width

    if box2.colliderect(box):
        print("Collision")
        box.x -= 1
        box2.x -= -2
pgzrun.go()
