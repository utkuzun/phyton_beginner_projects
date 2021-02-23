import random
import string
words=["mali","yaren","merve","burak","dilan","goken","ut ku","ut-ku"]

def get_valid_word():
    word = random.choice(words).upper()

    while ' ' in word or '-' in word:
        word = random.choice(words).upper()

    return word

def hangman():

    lives=6

    word = get_valid_word()
    word_letters = set(word)
    used_letters = set("")
    letters = set(string.ascii_uppercase)


    while lives > 0 and len(word_letters) > 0:

        print(f"You have {lives} lives and You've guessed {' '.join(used_letters)} letters.")

        screen = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(screen)}")

        guess = input("Type a letter: ").upper()

        if guess in letters - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1

        elif guess in used_letters:
            print(f"You already guessed the letter {guess}. Type another letter.")

        else: 
            print("Invalid letter. Try again.")

    if lives == 0:
        print(f"You died:( The word was {word}.")

    if len(word_letters) == 0:
        print(f"You guessed the word correct") 


hangman()