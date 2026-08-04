import random

secret_number = random.randint(1, 4)

guess = int(input("Guess the secret number: "))
#takes a number and returns whether it's too high or low compared to secret number
while guess != secret_number:
    if guess > secret_number:
          guess = int(input("Too high, guess again: "))
    elif guess < secret_number:
          guess = int(input("Too low, guess again: "))
    
if guess == secret_number:
    print("Well done")
