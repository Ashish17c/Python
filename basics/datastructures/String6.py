name  = 'Ashish chauhan'
fname = name[:6]
lname = name[6:]
mname = name[6:13]
print(fname, mname, lname)

rev_name = name[6:][::-1]
print(rev_name)

even_name = name[::2]

odd_name = name[1::2]
print(even_name, odd_name)