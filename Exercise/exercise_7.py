principle = 0
rate = 0
years = 0

while True:
    principle=float(input("Enter the principle: "))
    if principle<0:
        print("principle canot be zero")
    else:
        print(f"Principle : {principle}")
        break

while rate <= 0:
    rate=float(input("Enter rate: "))
    if rate<0:
        print("Rate cannot be zero")
    else:
        print(f"Rate : {rate}")

while years <= 0:
    years=float(input("Enter years: "))
    if years <= 0:
        print("years cannot be zero")
    else:
        print(f"years : {years}")

total = principle*pow((1 + (rate/100)),years )
print(f"Balance after {years} is {total}")