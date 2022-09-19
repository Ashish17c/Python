from unicodedata import name
contacts = {
     'emergency': 101,
     'police':100
}
while True:
    print('# options')
    print("search person")
    print("view all")
    print("Exit")
    ans = input("Enter a number: ") 
if ans == '1':
     name = input("Enter the persons name :")
     if name in contacts:
          print(f" {name} => {contacts[name]}")
     else:
          print("Not found, would, you like to add the {name}s'number?")
          number = input(f'Enter number for {name} =>')
          contacts[name] = number
          print('details added')
elif ans =='2':
     for name, number in contacts.items():
               print(f'{name} => {number}')
elif ans =='3':
     print("BYE")
     break
else:
     print("wrong input ")
