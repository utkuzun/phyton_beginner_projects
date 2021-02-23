import math
import random

class Player:

    def __init__(self, letter):
        self.letter = letter

    def player_move(self):
        pass


class HumanPlayer(Player):

    def __init__(self,letter):
        super().__init__(letter)

    def player_move(self,game):
        move = int(input("Make your move! Type board place(0-8): "))

        while not move in game.available_moves():
            move = input("Invalid move. Try again: ")

        return move

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def player_move(self,game):
        return random.choice(game.available_moves())

class SmartCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def player_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.avaiable_moves())
        else:
            square = self.minimax(game, self.letter)["position"]

        return square


    def minimax(self, state, player):
        max_player = self.letter

        other_player = "X" if player == "O" else "O"

        # first we want to check if the previous move is a winner

        if state.current_winner == other_player:
            return {"position": None, "score" : state.num_empty_squares() + 1 if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
            
        elif state.num_empty_squares() == 0:
            return {'position': None, 'score': 0}



        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
            

        for possible_move in state.available_moves():
            state.make_move(player, possible_move)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move
            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

class TicTacToe:
    def __init__(self):

        self.board = self.make_board()
        self.current_winner = False


    @staticmethod
    def make_board():
        return [" " for i in range(9)]


    def print_board(self):  
        for row in [self.board[3*i:(i+1)*3] for i in range(3)]:
            print("| "+ " | ".join(row) + " |")

    def print_board_nums(self):

        number_board = [[str(i) for i in range(3*j, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row)+ " |")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def make_move(self, letter, move):

        self.board[move] = letter

        if self.winner():
            self.current_winner = letter

    def winner(self):

        #  rows check

        rows = [[self.board[i] for i in range(3*j,(j+1)*3)] for j in range(3)]

        for row in rows:
            if all(s == "X" for s in row) or all(s == "O" for s in row):
                return True

        #  columns check

        columns = [[self.board[i] for i in range(j,j+9,3)] for j in range(3)]

        for column in columns:
            if all(s == "X" for s in column) or all(s == "O" for s in column):
                return True

        #  diagonal check

        dioganal1 = [self.board[i] for i in [2,4,6]]
        dioganal2 = [self.board[i] for i in [0,4,8]]

        if all(s == "X" for s in dioganal1) or all(s == "O" for s in dioganal1):
            return True

        if all(s == "X" for s in dioganal2) or all(s == "O" for s in dioganal2):
            return True

    def num_empty_squares(self):
        return self.board.count(" ")


def play(game, x_player, o_player, print_game = True):

    if print_game:
        game.print_board_nums()

    letter = "X"

    while not game.current_winner and not game.num_empty_squares() == 0:

        if print_game:
            game.print_board()

        if letter == "X":
            move = x_player.player_move(game)
        else: 
            move = o_player.player_move(game)

        game.make_move(letter, move)

        print(f"{letter} made move!!")
        letter = "X" if letter == "O" else "O"


    if print_game:
        game.print_board()
        if game.num_empty_squares() == 0:
            print("It\'s tie")
        else: 
            print(f"{game.current_winner} wins the game")


t = TicTacToe()
x_player = HumanPlayer("X")
o_player = SmartCompPlayer("O")

play(t,x_player, o_player, print_game=True)



