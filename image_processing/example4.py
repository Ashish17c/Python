from tkinter import font
from PIL import Image, ImageFilter, ImageEnhance

im = Image.open('aaa.jpg')
im2 = Image.open('laptop wallpaper.jpg')

font = ImageFilter.truetype(r"C:\Users\Lenovo\miniconda3\Lib\site-packages\pygame\tests\fixtures\fonts\PyGameMono.otf",140)
font2 = ImageFilter.truetype(r"C:\Users\Lenovo\miniconda3\Lib\site-packages\pygame\tests\fixtures\fonts\PyGameMono.otf",40)

imd = ImageDrow.Drow(im)