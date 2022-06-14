from tkinter import *
import random
import numpy as np

def stop_game(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 3

class Board:
    def __init__(self):
        self.current_board = np.array([[5, 5, 0],
                                       [0, 0, 0],
                                       [0, 0, 0]])
        self.current_player = 1

    def move(self, x, y):
        if self.current_board[x][y] != 0:
            print("illegal move")
        else:
            if self.current_player == 1:
                self.current_board[x][y] = 1
                self.current_player = 5
            else:
                self.current_board[x][y] = 5
                self.current_player = 1

            win = self.check_victory(x, y)
            if not win:
                if 0 not in self.current_board:
                    print("Draw")
                else:
                    print("game continues")
            else:
                if self.current_player == 1:
                    print("player o has won")
                else:
                    print("player x has won")
                stop_game(self.current_board)

    def check_victory(self, x, y):
        if self.current_board[0][y] == self.current_board[1][y] == self.current_board[2][y]:
            return True

        if self.current_board[x][0] == self.current_board[x][1] == self.current_board[x][2]:
            return True

        if x == y and self.current_board[0][0] == self.current_board[1][1] == self.current_board[2][2]:
            return True

        if x + y == 2 and self.current_board[0][2] == self.current_board[1][1] == self.current_board[2][0]:
            return True

        return False

    def print_board(self):
        print(self.current_board)

    def curr_player(self):
        if self.current_player == 1:
            return "x"
        else:
            return "o"

    def ai_move(self):

        if self.check_win():
            return

        return

    def check_win(self):
        ai_ind = []
        for i in range(3):
            if sum(self.current_board[i]) == 10:
                ai_ind = [i, list(self.current_board[i]).index(0)]

        for i in range(3):
            if sum(self.current_board[:, i]) == 10:
                ai_ind = [list(self.current_board[i]).index(0), i]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True



if __name__ == '__main__':
    b = Board()
    counter = 0

    while counter != 9:
        b.print_board()
        # b.ai_move()
        # b.print_board()
        player_move = input()
        b.move(int(player_move[0]), int(player_move[2]))
        b.ai_move()

