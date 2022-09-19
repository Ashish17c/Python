from PIL import Image

im = Image.open('laptop wallpaper.jpg')
im2 = Image.open('laptop wallpaper.jpg')

print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()
