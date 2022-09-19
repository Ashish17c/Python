from ctypes import sizeof
from turtle import color
from unicodedata import name


class Fruit:
    def__init__(self,name,color):
        self.name = name
        self.color = color


    def__info

class Mango(Fruit):
    def_init_(self,name, color, taste, size):
    super()._inif_(name,color)
    self.size = size

f = Fruit('orange','orange')
m = Mango('Daseri mango','greenish yellow','sweet','medium')

f.info()
m.info()
