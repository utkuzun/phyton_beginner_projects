import random


def play():
    player = input(
        " What is your choice, rock[r], scissors[s] or paper[p]: ").lower()

    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return print("its a tie")

    if is_win(player, computer):
        return print("You win !!")

    print("You lost :\\")


def is_win(player, component):

    if (player == "r" and component == "s") or (player == "p" and component == "r") or (player == "s" and component == "p"):
        return True

play()
