def bill(name, due_date, price):
    print("-------------------------------------------------")
    print(f"Hello {name} :)")
    print(f"Your bill is {price} and due date is {due_date}")
    print("-------------------------------------------------")
    
def calculate(pric_1, pric_2):  
    pric = pric_1+pric_2
    return pric;

print("Enter name, price, due_date")
nam = input("Name: ")
pric_1 = int(input("Price-1: "))
pric_2 = int(input("Price-2: "))
date = input("Due_date: ")

price = calculate(pric_1, pric_2)

bill(nam, date, price)