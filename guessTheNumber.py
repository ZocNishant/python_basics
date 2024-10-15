import random

def guessNumber(guess):
    secret_number = random.randint(0, 9)
    print(secret_number)
    guess = 0

    while secret_number != guess:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Think Higher")
        elif guess > secret_number:
            print("Think Lower")
    print("you won")




guessNumber(20)


