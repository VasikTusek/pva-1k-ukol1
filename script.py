import random

number = random.randint(1, 100)
attempts = 0
guessed = 0
while guessed == 0:
    x = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if x < 1 or x > 100:
        print("Please guess a number between 1 and 100.")
        attempts += 1
    elif x < number:
        print("Too low")
    elif x > number:
        print("Too high")
    else:
        print("You guessed the correct number.")
        print(f"It took you {attempts} attempts.")
        guessed = 1