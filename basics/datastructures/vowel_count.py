#Task. count the occurence of all vawels in a string
# output:
# a - 1 
# e - 4

msg = "ashish"

count=msg.count('a')
print("a :", count)

count= msg.count('e')
print("e :", count)

count= msg.count('i')
print("i :", count)

count= msg.count('o')
print("o :", count)

count= msg.count('u')
print("u :", count)

sentence = ''

for vowel in 'aeiou':
    print(vowel,sentence.lower().count(vowel))