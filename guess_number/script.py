import random

play = "y"
while play == "y":
    level = input("Pick a level (1: 1-10, 2: 1-100, 3: 1-1000, 4: 1-1000000): ")
    if level == "1":
        top = 10
    elif level == "2":
        top = 100
    elif level == "3":
        top = 1000
    else:
        top = 1000000

    number = random.randint(1, top)
    attempts = 0
    guessed = 0
    while guessed == 0:
        x = input(f"Guess a number between 1 and {top}: ")
        if not x.isdigit():
            print("That's not a number.")
            continue
        x = int(x)
        elif x < 1 or x > top:
            print(f"Please guess a number between 1 and {top}.")
            attempts += 1
        elif x < number:
            print("Too low")
        elif x > number:
            print("Too high")
        else:
            print("You guessed the correct number.")
            print(f"It took you {attempts} attempts.")
            guessed = 1

    play = input("Play again? (y/n): ")
