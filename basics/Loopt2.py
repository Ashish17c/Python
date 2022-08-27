from turtle import *

sides = 6              # int(input('How many sides do you want?:'))
distance = 102            # int(input('How far do you want to go:'))

fillcolor('yellow')
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()