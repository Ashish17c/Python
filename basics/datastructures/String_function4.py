# String Validation function

file = input("Enter file name:")

if file.endswith('.png'):
    print('its a png file')
elif file.endswith('.jpg.file'):
    print('its.a.word.file')
elif file.endswith('.py') or file.endswith('.ipynb'):
    print('its a python file')
else:
    print("Un identified file, destroy ur computer")