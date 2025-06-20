import random

words = ['apple','pineapple','orange','pear']

hangman = {0: ("   "),
           1: (" 0 "),
           2: (" 0 "
               " | "),
           3: (" 0 "
               "/| "),
           4: (" 0 "
               "/|\\"),
           5: (" 0 "
               "/|\\"
               "/ "),
           6: (" 0 "
               "/|\\"
               "/ \\")}

def display_man(wrong_guess):
    print("*************")
    for line in hangman(wrong_guess)
        print(line)
    print("*************")

def display_hint(hint):
    print("_".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = imput("Enter a leater: ".lower()
        
        if len(guess) != 1 or not guess.isaplha()
        print("Invalid input")
        continue
        
        if guess in guessed_letter:
        print(f"{guess} is already guessed")
        continue
        guessed_letter.add(guess))
