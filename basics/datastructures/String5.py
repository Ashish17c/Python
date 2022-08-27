from re import T


for i in range(1,6):
    print(i * '#')

# -------------------

for i in range(1,6):
    print((i * ' ❄').rjust(15))

# --------------------------------------------
'''
*****
****
***
**
*
'''
for i in range(7,0,-1):
    print(i* " *")

# ------------------------------------------------
'''    T
      TTT
     TTTTT
    TTTTTTT
   TTTTTTTTT  
'''

for i in range(1,15,2):
    print((i * ' T').center(30))

# ------------------------------------------------
'''  
    TTTTTTTTT
     TTTTTTT
      TTTTT
       TTT
        T
'''
print('\n Print the Pattern \n')
for i in range(15,1,-2):
    print((i * ' T').center(30))


# ------------------------------------------------




