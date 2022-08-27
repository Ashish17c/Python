from turtle import width
import pgzrun
height = 200
width = 300

aliend = Actor('character_0002',pos =(200,200))
aliend = Actor('character_0024',topleft =(50,50))

def draw():
    screen.fill('white')
    aliend.draw()
    aliend.draw()

def update():
    aliend.y += 1
    if aliend.y > height:
        aliend.y = 0
    
pgzrun.go()
