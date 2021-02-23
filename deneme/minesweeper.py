
import random


class minesweeper():

    def __init__(self, dim_size, num_bombs):

        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_board()
        self.dug = set()

    def make_board(self):

        return [[" " for i in range(self.dim_size)] for i in range(self.dim_size)]

    def place_bombs(self):

        for _ in range(self.num_bombs):

            place = random.randint(0, self.dim_size ** 2 -1)        # select a random place

            row = place // self.dim_size                            # find first indice of this place
            col = place % self.dim_size                             # find second indice of this place

            if not self.board[row][col] == "*":                     # check if there is a bomb 
                self.board[row][col] = "*"                          #place bomb

    def num_bombs_around(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):

                cell_number = 0
            
                if not self.board[row][col] == "*":

                    for r in range(max(0, row - 1 ), min(row +1, self.dim_size-1) + 1):
                        for c in range(max(0, col - 1 ), min(col +1, self.dim_size-1) + 1):

                            if self.board[r][c] == "*": 
                                cell_number += 1

                    self.board[row][col] = str(cell_number)

    def dig_board(self, row, col):
        
        if not (row, col) in self.dug:
            self.dug.add((row, col))
        else: 
            return

        if self.board[row][col] == "0":
            for r in range(max(0, row - 1 ), min(row +1, self.dim_size-1) + 1):
                for c in range(max(0, col - 1 ), min(col +1, self.dim_size-1) + 1):

                    if r == row and c == col:
                        continue
                    self.dig_board(r, c)

        elif not self.board[row][col] == "*": 
            self.dig_board(row, col)
            return 

        return


    def print_board(self):

        empty_board = [[" " for i in range(self.dim_size)] for i in range(self.dim_size)]

        for r in range(self.dim_size):
            for c in range(self.dim_size):

                if (r, c) in self.dug:
                    empty_board[r][c] = self.board[r][c]

        for row in range(self.dim_size):
            print(empty_board[row])
                

            
def play(game, dim_size, num_bombs):

    game.make_board()
    game.place_bombs()
    game.num_bombs_around()
    game.print_board()


    while len(game.dug) < dim_size**2 - num_bombs:

        row = int(input("Type row of your move: "))
        col = int(input("Type column of your move: "))

        if (row, col) in game.dug:
            print("Invalid place. Try again !!")
            continue

        elif not row in range(game.dim_size) and not col in range(game.dim_size):
            print("Invalid place. Try again !!")
            continue

        if game.board[row][col] == "*":

            for row in range(game.dim_size):
                for col in range(game.dim_size):
                    game.dig_board(row, col)
        
        game.dig_board(row, col)

        game.print_board()
            
    if len(game.dug) == dim_size**2 - num_bombs:
        print("You won the game!!")
        for row in range(game.dim_size):
            for col in range(game.dim_size):
                game.dig_board(row, col)
        
        game.print_board()

    else: 
        print("You bombed :(")
                

dim_size = 4
num_bombs = 4
game = minesweeper(dim_size, num_bombs)
play(game, dim_size, num_bombs)




