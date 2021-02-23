import random


def guess(x):

    random_number = random.randint(0, x)

    guess = 0

    while not random_number == guess:

        guess = int(input("Guess a number between 0-100: "))

        if guess < random_number:
            print("Too low!!")
        elif guess > random_number:
            print("Too high!!")

    print(f"Yay!! You guessed the number {random_number}")


def computerGuess(x):

    comment = ""

    high = x
    low = 0

    while not comment == "c":

        trueComment = False
        print(low,high)

        if high != low:
            try:
                guess = random.randint(low, high)
            except ValueError:
                guess = high
                comment = "c"
                guess = low
        else:
            trueComment = True
            comment = "c"
            guess = low



        while not trueComment:
            comment = input(
                f"Is the number {guess}. Or it is high (H), low(L) or correct(C): ").lower()

            if comment in set(["h", "l", "c"]):
                trueComment = True
            else: 
                print("Invalid input")


        if comment == "h":
            high = guess - 1
        elif comment == "l":
            low = guess + 1
 

    print(f"Yay!! You computer guessed the number {guess}")


computerGuess(100)
