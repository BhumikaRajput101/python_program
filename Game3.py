##Hangman (Basic Version)
import random
words=["python", "computer", "programming", "hangman", "developer"]
secret=random.choice(words)
letter=[]
attempt= 6  
print(" Welcome to Hangman!")
print("_ " * len(secret))
while attempt>0:
    guess=input("Guess a letter: ").lower()
    if guess in letter:
        print("You already guessed that letter.")
        continue
    letter.append(guess)

    if guess in secret:
        print("Good guess!")
    else:
        attempt-= 1
        print(f"Wrong guess! Attempts left: {attempt}")
    display_word = ""
    for a in secret:
        if a in letter:
            display_word += a + " "
        else:
            display_word += "_ "

    print(display_word)
    if all(a in letter for a in secret):
        print(" Congratulations! You won!")
        break
if attempt==0:
    print("You lost!")
    print("The word was:", secret)