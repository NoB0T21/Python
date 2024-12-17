import random;

option = ("rock", "paper" , "scissors")

player = None;

while player not in option:
    running = True;
    while running:
        computer = random.choice(option);
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        print(f"computer: {computer}");
        print(f"player: {player}");
        if player == "rock" and computer == "scissors":
            print("you win");
        elif player == "paper" and computer == "rock":
            print("you win");
        elif player == "scissors" and computer == "paper":
            print("you win");
        elif player == computer:
            print("Tie");
        else:
            print("you loss");

        is_true = True;
        while is_true:
            play_again = input("Do you want to play again (Y or N): ").lower();
            if play_again not in ["y", "n"]:
                print("please enter Y or N");
            else:
                if play_again == "y":
                    running = True;
                    is_true = False;
                else:
                    running = False;
                    is_true = False;
