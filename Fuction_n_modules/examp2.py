# return value
from audioop import minmax
from multiprocessing.dummy import Value
from optparse import Values


def area():
    l = int(input('Enter the lenght:'))
    b = int(input('Enter the breadth:'))
    area = l * b
    return area

# calling 
#print("Area=>", area())

#ans = area()
#print('Area=>',ans)

#ans = area() + area() - area()
#print('Total area=>',ans)


def minmax():
    x = [23,3,4,5,4,34,65,76,23]
    return min(x),max(x)

Values = minmax()
x,y = minmax() 

print(Values)
print(x,y)
print(minmax())

