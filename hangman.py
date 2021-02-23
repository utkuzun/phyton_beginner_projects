import random
import string
words=["mali","yaren","merve","burak","dilan","goken","ut ku","ut-ku"]

def get_random_word():
    word = random.choice(words)
    

    while " " in word or "-" in word:
        word = random.choice(words) 
    print(word)
    return word


def hangman():
    lives = 6


    word = get_random_word().upper()
    word_letters = set(word)

    used_letters = set("")
    letters = set(string.ascii_uppercase)

    while len(word_letters) >0 and lives > 0:

        print(f"You have {lives} lives and you used these letters: {' '.join(used_letters)}.")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        guess = input("Type a letter: ").upper()

        if guess in letters - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            
            else: 
                lives -=1
                print(f"\n your letter {guess} is not in the world list")

        elif guess in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        

    if lives == 0:
        print(f"You died. The word was {word}")
    else:
        print( f"Yay!! You guessed the word {word}")
        

hangman()      


