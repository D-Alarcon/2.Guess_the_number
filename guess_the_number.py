#This is the 2nd of 12 beginner projects presented by Kylie Ying.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Type your guess number: "))
        if guess < random_number:
            print("Sorry, your guess was too low")
        elif guess > random_number:
            print("Sorry, your guess was too high")
    print("Congrats! You guessed the correct number")
