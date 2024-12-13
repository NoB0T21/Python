#python weight convertor

weight = float(input("Enter your weight: "))
unit = input("Is your is in Kilogram or Pounds (k ro L): ")

if unit == "k":
    weight *= 2.205
    unit = "LBS"

elif unit == "l":
    weight /= 2.205
    unit = "KG"

else:
    print(f"{unit} is not valid")

print(f"Your Weight is in: {round(weight, 2)} {unit}")