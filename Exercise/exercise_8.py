menu = {"pizza": 200,
        "burger": 90,
        "fries": 50,
        "wings": 150,
        "coke": 70,
        "soda": 40,
        "lemonade": 60}

cart = []
total = 0

print("------ menu ------")
for key, value in menu.items():
    print(f"{key:10}: {value}")
print("------------------")

while True:
    food =input("select an item (q to quit): ").lower()
    if food == "q":
        break;
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print("------------------")
print(f"your total is {total}")