# Python program to Calculte the Area of a Triangle 
a=input("Enter the no1:")
b=input("Enter the no2:")
c=input("Enter the no3:")

s=(a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is a' %area)