# shopping cart program

item = str(input("What item would you like to buy? :"))
price = float(input("Price? :"))
quantity = int(input("How many would you like? :"))

total = price * quantity

print(f"item   |price   |quantity   |total")
print("")
print(f"{item}   |{price}   |{quantity}   |{total}$")