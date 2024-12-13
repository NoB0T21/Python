age = int(input("Enter your age: "))

if age >= 80:
    print(f"You are {age}yr old")
    print("Just Die old gramp")

elif age >= 18:
    print(f"You are {age}yr old")
    print("You are welcome")

elif age < 0:
    print(f"You are {age}yr old")
    print("You should be born first")

else:
    print(f"You are {age}yr old")
    print("You should be 18+yr old")