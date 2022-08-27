
msg = 'This is a place to find the answers related to coding.'

print(msg.find('place'))
print("place:",msg.find('palace')) # -1 means not found

val = msg.find('answer')
if val == -1:
    print('word not at{val} index')

print('is:', msg.find('is'))
print('is:', msg.index('is'))

print('is:', msg.find('is',3))

print('to:', msg.rfind('to'))
print('to:', msg.rfind('to'))