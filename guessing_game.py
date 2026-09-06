import random

secret_number = random.randint(1, 100)

guess = int(input("Guess the secret number: "))
#list to track numbers that have already been guessed and forces user to choose different number
past_guesses = []
#takes a number and returns whether it's too high or low compared to secret number
while guess != secret_number:
    if guess in past_guesses:
        guess = int(input("You've already guessed that, try again: "))
    elif guess not in past_guesses:
        past_guesses.append(guess)
        if guess > secret_number:
          guess = int(input("Too high, guess again: "))
        elif guess < secret_number:
          guess = int(input("Too low, guess again: "))
    

if guess == secret_number:
    print("Well done")