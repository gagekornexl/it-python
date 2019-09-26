import random

print("==========================")
print("        Guess my number   ")
print("        By Gage           ")
print("==========================")
print("")

name = input("What is your name? ")
the_number = random.randint(0, 100)

print("")
print("I'm thinking of an integer between 0 and 100. Can you guess it?")

guess = -1
while guess != the_number:
    guess_text = input("What is your guess? ")
    guess = int(guess_text)

    if guess < the_number:
        print(f"Sorry, {name}, but your guess is too LOW. Try again.")
    elif guess> the_number:
        print(f"Sorry, {name}, but your guess is too HIGH. Try again.")
    else:
        print(f"You guessed it! Congratuations, {name}!")