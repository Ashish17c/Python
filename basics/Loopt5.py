from logging import critical
from turtle import *
speed(0)
pensize(2)
pencolor('yellow')
bgcolor('red')
bgcolor('black')

for i in range(12):
    circle(100)
    right(360/12)

    for i in range(6):
       circle(121)
       left(360/21)

mainloop()



