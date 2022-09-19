from string import ascii_lowercase

msg = "My name is Ashish chauhan "

for char in ascii_lowercase:
    print(f'{char} - {msg.count(char)}')
    