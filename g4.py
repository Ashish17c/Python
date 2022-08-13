from ast import alias, keyword
from ssl import ALERT_DESCRIPTION_DECODE_ERROR
from turtle import Screen, speed
import pgzrun

HEIGHT = 500
WIDTH = 500

alieng = Actor('character_0000',topleft=(50,50))
alieng = Actor('character_0002',topleft=(300,50))

def draw():
    Screen.file('black')
    alieng.drow()
    aliend.draw()

def update():
    alieng.x += 1
    if alieng.x > WIDTH:
        alienb.x = 0
    if Keyboard.left:
        alienb.x -= speed
    if Keyboard.up:
        alienb.y -= speed
    if keyboard.down:
        alienb.y += speed
    if alienb.colliderect(alieng):
        sounds.sound1.play()
pgzrun.go()