username=str(input("Enter username: "))
password=str(input("Enter password: "))

username1="admin"
password1="1234"

if username==username1 and password==password1:
    print("login successful")
elif username !=username1:
    print("invalid username")
elif password !=password1:
    print("invalid password")
else:
    print("login failed")



