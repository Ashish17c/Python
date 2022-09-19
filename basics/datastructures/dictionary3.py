from pprint import pprint
movies = {}
# add
movies['sholay'] = '2 frds fight with a dacoit'
movies['inception'] = 'no summary avaialable'
print(movies)


movies.update(
    ironman='man builds a suit that is not iron',
    hulk = 'story about a man that is not hulka',
    batman = 'hero drssed as a bat')

movies.pop('sholay')

# update
movies['inception'] = 'dream whithin dream with recursion logic'

# update
movies['batman'] += 'and fights crimes at nights'
pprint(movies)