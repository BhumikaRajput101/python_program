import random
choices=['rock','paper','scissor']
print("Welcome to Game of ROCk ,PAPER And SCISSOR!!!")
user=(input("Enter your choice:")).lower()
computer=random.choice(choices)

print("Computer choice is:",computer)
if user not in choices:
    print("Envalid input Try again")
  
elif computer==user:
    print("That's a Tie.... ")
elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You win! 🎉")
else:
    print("You lose! 😢")


