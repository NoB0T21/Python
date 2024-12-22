age=int(input("Enter no. from 1-100: "))

while age < 1 or age >100:
    print(f"{age} is not valid")
    age=int(input("Enter no. from 1-100: "))

print(f"Your age is {age}")