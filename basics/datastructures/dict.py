info = ['Mistborn','The Final Empire', 'Brandon Sanderson','tor.com',2099,2002]

info_dict ={
    'series':'Mistborn',
    'title' :'The Final Empire',
    'author':'Brandon Sanderson',
    'publisher':'tor.com',
    'price':2099,
    'year':2002
}

print(info_dict)
print(info_dict.keys())
print(info_dict.values())
print(info_dict['series'])
print(info_dict['title'])
print(info_dict.get('author'))

# update existing key

info_dict['price'] = 599
print(info_dict)
