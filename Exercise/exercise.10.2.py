import random

def spin_row():
    symbols = ['❤️','🥗','🎈','🛺','🫅🏻']

    return [ random.choice(symbols) for _ in range(3)]

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100

    print('*********** Wellcome to Slot Machine ***********')
    print('Symbols: ❤️ | 🥗 | 🎈 | 🛺 | 🫅🏻')
    print('')
    print('!!!!!!!!!!!!!!!!!!!! Rules !!!!!!!!!!!!!!!!!!!!!')
    print('You shoule get all 3 Symboles same to win prise')
    print('')
    print('************************************************')

    while balance > 0:
        print(f'Your current balance is {balance}')
        bet = input('Enter a Bet amount: ')

        if not bet.isdigit():
            print('')
            print('!!!!!!!!!! Enter valid Number !!!!!!!!!!')
            print('')
            continue

        bet = int(bet)

        if bet > balance:
            print('')
            print('!!!!!!!!!!!!!!!! Alert !!!!!!!!!!!!!!!!!')
            print('Insufficient balance')
            print('')
            continue
        
        elif bet <= 0:
            print('')
            print('!!!!!!!!!!!!!!!! Alert !!!!!!!!!!!!!!!!!')
            print('Bet canot be zero')
            print('')
            continue

        else:
            balance -= bet

        row = spin_row()

if __name__ == '__main__':
    main() 