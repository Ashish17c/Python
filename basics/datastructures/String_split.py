msg = input("Enter a senence:")

words = msg.split()
print(words, len(words),'words found')

words = msg.split(',')
print(words, len(words),'words found')

words = msg.split('is')
print(words, len(words),'words found')

words = msg.split()[-3:]
print(msg.split()[-3:])

