#Number Guessing Game

import random
number=random.randint(1,100)
attempts=0


while True:
    
    guess=int(input("Enter your Guess number:"))
    attempts=+1
    if guess<number:
        print("Too low !! Try again")
    elif guess>number:
        print("Too high!! try again")
    else:
        print("You have guessed Correctly !! COngratulations")
        break