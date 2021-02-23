import random
import string


words=["mali","yaren","merve","burak","dilan","goken","ut ku","ut-ku"]


def get_word(words):

    word = random.choice(words)
    print(word)

    while "-" in word or " " in word:
        word = random.choice(words)
        print(word)

    return word


def hangman():

    word = get_word(words).upper()

    lives = 6

    word_letters = set(word)
    letters = set(string.ascii_uppercase)
    used_letters = set()

    while lives > 0 and len(word_letters) > 0:

        screen = [lett if lett in used_letters else "-" for lett in word]
        print(f" ".join(screen), end="            ")

        

        print(f" ".join(used_letters))
        print(f"You have {lives} lives")


        guess = input("Type a letter: ").upper()

        

        if guess in letters:

            if not guess in used_letters:
                used_letters.add(guess)
            else: 
                print("This letter already typed.")
                continue

            if guess in word_letters:
                word_letters.remove(guess)
            
            elif not guess in word_letters:
                lives-=1

        else: 
            print("Invalid input.")

    if lives > 0:
        screen = [letter if letter in used_letters else "-" for letter in word_letters]
        print(f" ".join(screen))
        print(f"You won!! The word was {word}")
    else: 
        print(f"You died!! The word was {word}")


hangman()
