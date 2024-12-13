#python calculator

op = input("Enter operation you want to perform (+, -, *, /) : ")
num1 = float(input("Enter 1st NO.:"))
num2 = float(input("Enter 2st NO.:"))

if op == "+":
    Result=num1+num2
    print(f"{num1} + {num2} = {Result}")
elif op == "-":
    Result=num1-num2
    print(f"{num1} - {num2} = {Result}")
elif op == "*":
    Result=num1*num2
    print(f"{num1} * {num2} = {Result}")
elif op == "/":
    Result=num1/num2
    print(f"{num1} / {num2} = {Result}")

else:
    print(f"{op} is not valid operation")