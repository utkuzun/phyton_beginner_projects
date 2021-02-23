import random


def guess(x):

    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:

        guess = int(input(f"Guess the number between 1 and {x} :"))

        if guess > random_number:
            print("Sorry. Too high.")
        elif guess < random_number:
            print("Sorry. Too low.")

    print(f"You guessed correctly the number {random_number}")


def computerGuess(x):
    low = 1
    high = x

    guess = random.randint(low, high)

    feedback = ""

    while feedback != "c":
        if high !=low:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f"Is {guess} correct(C), high(H) or low(L) ??: ").lower()

        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess +1
        
    
    print(f"Yay. Computer guessed correctly to number {guess}!!!")

computerGuess(500)
