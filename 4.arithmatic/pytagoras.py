#clac hypotanius of rightangle triangle using math module

import math

base = float(input("Enter base of triangle => "))
height = float(input("Enter height of triangle => "))

H = math.sqrt(pow(base, 2)+pow(height, 2))

print(f"hypotanius of rightangle_triangle is {round(H,2)}")
