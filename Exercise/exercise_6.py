username = input("Enter your name: ")

if len(username) > 12:
    print("Name can't be that long")
elif not username.find(" ")==-1 or not username.isalpha():
    print("Name should not containt space or numbers")
else:
    print(f"welcome {username}")