#clac area of circle using math module
import math

radius = float(input("Enter Radius of your circle => "))

Area = math.pi * pow(radius, 2)

print(f"Area of circle is {round(Area, 2)}")
