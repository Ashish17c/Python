'''T= tuple(("Apple","Banana","cherry"))

print(len(T))'''

# Armstrong Number  , 

num = int(input("Enter the three number:"))
sum = 0
temp = num

while temp > 0:
    digit = temp%10
    cube = digit**3
    sum = sum  + cube
    temp //= 10

if sum == num:
    print('it is an armstrong number')
else:
    print('It is not an armstrong number')
