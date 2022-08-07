import email


print("Register your details")
Name=input("Enter your name:")
Email=input("Enter your Email:")
Password=input("Enter your Password:")
cpassword=input("Enter your cpassword:")
Gender=input("Enter your Gender(M/F):")
if len(Name) > 4 and len(Name) < 25:
    if '@' in Email:
     if Password ==cpassword:
          print("You are registerd ✔")
     else:
        print("Password do not match")
    else:
        print("Email is invalid")
else:
    print("username must be between 4 and 25 chars")