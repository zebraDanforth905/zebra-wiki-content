username = input("Enter a username: ")
password = input("Enter a password: ")

if username.isalpha() and len(password) >= 8:
    print("Account created!")
elif not username.isalpha():
    print("Your username must be all letters.")
else:
    print("Your password must be at least 8 characters long.")
