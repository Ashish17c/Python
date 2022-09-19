from PIL import Image

im = Image.open('aaa.jpg')
im2 = Image.open('aaa.jpg')

print(im)
print(im2)

print('resolution',im.size)
print('height',im.height)
print('width', im.width)
print('mode', im.mode)
print('format', im.format)
print('info', im.info)

im.convert('L').show()

im.resize((100,100).show)

#im.resize((2000,2000).show)

im.resize((im.width *5, im.height *5)).save('aaa.jpg')

