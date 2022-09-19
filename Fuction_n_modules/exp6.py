

from unicodedata import name

x= [1,2,4,5,8,7,3,8]
o= list(map(lambda i: i**2,x))
print(o)

y=[2,3,1,2,3,5,6,3,3,1,2]

xy=list(map(lambda a,b: a+b, x, y))
print(xy)

y3= list(filter(lambda i: i>3, x))
print(y3)

name_singh = list(filter(lambda i: i>3, x))
print(y3)

name =['Raj Singh', 'Vijay Sing','Ravi Kumar','Ajay Singh','Raja Kumar','Vijay Pandey']

name_singh = list(filter(lambda n: n.endswith('r'),name))
print(name_singh)

name_r = list(filter(lambda i: i>3, x))
print(name_r)

print(range(1,10))