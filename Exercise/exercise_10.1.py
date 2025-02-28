def show_balance(balance):
    print(" ")
    print("**************** Nobot bank ****************")
    print(f"Your Balance is: {balance:.2f}")
    print("********************************************")

def deposite(balance):
    print(" ")
    print("**************** Nobot bank ****************")
    amount = float(input("Enter Amount to deposit: "))
    print(" ")
    print("********************************************")

    if amount < 0:
        print("!!!!!! Please enter valide Amount !!!!!!")
    else:
        return amount

def withdraw(balance):
    print(" ")
    print("**************** Nobot bank ****************")
    print(f"Your Balance is: {balance:.2f}")
    print(" ")
    amount = float(input("Enter Amount to deposit: "))
    print("********************************************")

    if amount > balance:
        print("!!!!!!!!! Insufficient Balance !!!!!!!!!")
    else:
        return amount

<<<<<<< Updated upstream
def main():
    balance = 0
    is_running = True

    while is_running:
        print(" ")
        print("********** Wellcome to Nobot bank **********")
        print("1.Show Balance")
        print("2.deposite")
        print("3.withdraw")
        print("4.exit")
        print("********************************************")

        choice = input("Enter your choice: ")

        print(" ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposite()
            show_balance(balance)

        elif choice == '3':
            balance -= withdraw(balance)
            show_balance(balance)
        
        elif choice == '4':
            is_running = False
        
        else:
            print("!!!!!!!!!!! Enter valid Answer !!!!!!!!!!!")
=======
>>>>>>> Stashed changes

balance = 0
is_running = True
while is_running:
    print(" ")
    print("********** Wellcome to Nobot bank **********")
    print("1.Show Balance")
    print("2.deposite")
    print("3.withdraw")
    print("4.exit")
    print("********************************************")

    choice = input("Enter your choice: ")

    print(" ")

    if choice == '1':
        show_balance(balance)

    elif choice == '2':
        balance += deposite()
        show_balance()  

    elif choice == '3':
        balance -= withdraw(balance)
        show_balance()
        
    elif choice == '4':
        is_running = False
        
    else:
        print("!!!!!!!!!!! Enter valid Answer !!!!!!!!!!!")

print(" ")
print("**************** Nobot bank ****************")
print("Thank You for using Nobot bank please visite again")
print("********************************************")
