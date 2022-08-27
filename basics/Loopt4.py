from turtle import *
speed(0)
pencolor('red')
bgcolor('yellow')
val = 1
while True:
    forward(3 * val)
    left(360/6)
    dot(1)
    circle(3,112)
    val += 1