#clac circumference of circle using math module

import math

radius = float(input("Enter Radius of tour circle => "))

C = 2 * math.pi * radius

print(f"circumference = 2 * {round(math.pi, 2) }* {radius}")
print(f"circumference of your circle is {round(C, 2)}")
