#python weight convertor

temp = float(input("Enter your temperature: "))
unit = input("Is your is in Celsius or Fahrenhit (C/F): ")

if unit == "C":
    temp = (temp*9/5)+32
    unit = "F"

elif unit == "F":
    temp = (temp-32)*5/9
    unit = "C"

else:
    print(f"{unit} is not valid")

print(f"temperature is : {round(temp, 2)} {unit}")