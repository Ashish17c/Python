amout = int(input("Enter the amout:"))
pm  = input("payment method (credit,cash,upi):")
if amout>1000:
    amout-=amout*.03
if pm == 'credit':
    amout = amout - 100
amout += amout*.18
print("print the amout:",amout)


