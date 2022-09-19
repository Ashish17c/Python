from string import punctuation
msg = 'As@#hi$()sh%&*()*&^%$#@'
for p in punctuation:
    msg = msg.replace(p,'')
print(msg)