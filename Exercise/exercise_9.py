import random;

lowest_number = 1;
highest_number = 100;
guesses = 0;
is_running = True;

answer = random.randint(lowest_number,highest_number);

print("Number guessing Game");
print(f"Select no. between {lowest_number} and {highest_number}");

while is_running:
    guess = input("Enter your guess: ");

    if guess.isdigit():
        guess = int(guess);
        guesses += 1;
        if guess < lowest_number or guess > highest_number:
            print("the given input is oute of range")
            print(f"please enter valide input between {lowest_number} and {highest_number}")
        elif guess > answer:
            print("go lower");
        elif guess < answer:
            print("go higher");
        else:
            print("--------------------------------------------")
            print("you guess it right");
            print(f"You guessed in {guesses} guesses");
            print("--------------------------------------------")
            is_running = False;
    else:
        print("--------------------------------------------")
        print("!! Invalid inpute !!")
        print(f"please enter valide input between {lowest_number} and {highest_number}")
        print("--------------------------------------------")