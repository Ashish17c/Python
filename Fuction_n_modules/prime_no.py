from cgi import print_arguments


def primeno():
    x = []

    for num in range(2,200):
        for i in range(2,num):
            if num%i ==0:
                break
        else:
            x.append(num)
            print(num,end=" ")
primeno()