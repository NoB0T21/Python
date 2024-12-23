import random

def spin_row():
    symbols = ['🦋','🍓','🏖️','🚀','🐘']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(bet , row):
    if row[0]==row[1]==row[2]:
        if row[0] == '🦋':
            return bet*3
        
        elif row[0] == '🍓':
            return bet*5
        
        elif row[0] == '🏖️':
            return bet*7
        
        elif row[0] == '🚀':
            return bet*10
        
        elif row[0] == '🐘':
            return bet*15
    
    return 0

def main():
    balance = 100

    print("************ Wellcome to NoB0T's Slot Machine ************")
    print("symbols = 🦋 | 🍓 | 🏖️ | 🚀 | 🐘")
    print("")
    print("######################## Rules ###########################")
    print("If You get all tree symbols same you win ore else you lose")
    print("")
    print(f"Your Balance is {balance:.2f}")
    print("**********************************************************")

    while balance > 0:
        print("")
        bet = input("Enter Bet Amount: ")
        print("")

        if not bet.isdigit():
            print("!!!!!!!!!!!!!!!!!!!!!!!!! ALERT !!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Enter valid input")
            print("")
            continue

        bet = int(bet)

        if bet > balance:
            print("!!!!!!!!!!!!!!!!!!!!!!!!! ALERT !!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Insufficient Balance")
            print("")
            continue
        elif bet <= 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!! ALERT !!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Bet Cannot be Less than 0")
            print("")
            continue
        else:
            balance -= bet
            row = spin_row()
            print("Spinning.......")
            print("")

            print("****************** NoB0T's Slot Machine ******************")
            print_row(row)
            print("**********************************************************")

            payout = get_payout(bet, row)

            if payout > 0:
                print('')
                print("****************** NoB0T's Slot Machine ******************")
                print(f'You win {payout}')
            else:
                print('')
                print("****************** NoB0T's Slot Machine ******************")
                print('You lose')
                
            balance += payout
            print(f"Your Balance is {balance:.2f}")
            print("**********************************************************")
            print("")

if __name__ == '__main__':
    main()