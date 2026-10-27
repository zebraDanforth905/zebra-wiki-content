import random

number = random.randint(1, 50)
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-50): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it! The number was " + str(number) + ".")
