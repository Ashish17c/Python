def word_counter(s):
    words = s.split()
    return len(words)

def area(l,b):
    return l * b

def circmuference(r):
    return 2 * 3.14 * r

print(word_counter('this is an example:'))
print(word_counter('Welcome to the code of python:'))
print(word_counter('screenshot se kuch nhi hota:'))
print(word_counter('rules and covention likh lo!!!:'))

# call area and circumference

# 1. direct
print(area(10,10))

# 2. user input

a = int(input('Enter length: '))
b = int(input('Enter breadth: '))
out = area(a,b)
print(out)


