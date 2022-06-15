import random
import numpy as np
from tkinter import *


def stop_game(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 3


class Board:
    def __init__(self):
        self.current_board = np.array([[0, 0, 0],
                                       [0, 0, 0],
                                       [0, 0, 0]])
        self.current_player = 1

    def move(self, x, y):
        if self.current_board[x][y] != 0:
            print("illegal move")
        else:
            if self.current_player == 1:
                self.current_board[x][y] = 1
                btn_list[x][y].configure(text="x")
                self.current_player = 2
            else:
                self.current_board[x][y] = 5
                btn_list[x][y].configure(text="o")
                self.current_player = 1

            label_info.configure(text=f"player: {b.curr_player()}")
            win = self.check_victory(x, y)
            if not win:
                if 0 not in self.current_board:
                    print("Draw")
                else:
                    print("game continues")
            else:
                if self.current_player == 1:
                    print("player o has won")
                    label_info.configure(text="Player o has won!!")
                else:
                    print("player x has won")
                    label_info.configure(text="Player x has won!!")

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
        if self.check_block():
            return
        if self.check_fork():
            return
        if self.check_player_fork():
            return
        if self.check_center():
            return
        if self.opposite_corner():
            return
        if self.empty_corner():
            return
        if self.empty_side():
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

        if (self.current_board[0][0] + self.current_board[1][1]) == 10 and self.current_board[2][2] == 0:
            ai_ind = [2, 2]
        if (self.current_board[0][0] + self.current_board[2][2]) == 10 and self.current_board[1][1] == 0:
            ai_ind = [1, 1]
        if (self.current_board[1][1] + self.current_board[2][2]) == 10 and self.current_board[0][0] == 0:
            ai_ind = [0, 0]
        if (self.current_board[2][0] + self.current_board[1][1]) == 10 and self.current_board[0][2] == 0:
            ai_ind = [0, 2]
        if (self.current_board[2][0] + self.current_board[0][2]) == 10 and self.current_board[1][1] == 0:
            ai_ind = [1, 1]
        if (self.current_board[1][1] + self.current_board[0][2]) == 10 and self.current_board[2][0] == 0:
            ai_ind = [2, 0]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def check_win_without_move(self):
        wins = 0
        for i in range(3):
            if sum(self.current_board[i]) == 10:
                wins = wins + 1

        for i in range(3):
            if sum(self.current_board[:, i]) == 10:
                wins = wins + 1

        if (self.current_board[0][0] + self.current_board[1][1]) == 10 and self.current_board[2][2] == 0:
            wins = wins + 1
        if (self.current_board[0][0] + self.current_board[2][2]) == 10 and self.current_board[1][1] == 0:
            wins = wins + 1
        if (self.current_board[1][1] + self.current_board[2][2]) == 10 and self.current_board[0][0] == 0:
            wins = wins + 1
        if (self.current_board[2][0] + self.current_board[1][1]) == 10 and self.current_board[0][2] == 0:
            wins = wins + 1
        if (self.current_board[2][0] + self.current_board[0][2]) == 10 and self.current_board[1][1] == 0:
            wins = wins + 1
        if (self.current_board[1][1] + self.current_board[0][2]) == 10 and self.current_board[2][0] == 0:
            wins = wins + 1

        return wins

    def check_block(self):
        # check if player can win in next move
        ai_ind = []
        for i in range(3):
            if sum(self.current_board[i]) == 2:
                ai_ind = [i, list(self.current_board[i]).index(0)]

        for i in range(3):
            if sum(self.current_board[:, i]) == 2:
                ai_ind = [list(self.current_board[:, i]).index(0), i]

        if (self.current_board[0][0] + self.current_board[1][1]) == 2 and self.current_board[2][2] == 0:
            ai_ind = [2, 2]
        if (self.current_board[0][0] + self.current_board[2][2]) == 2 and self.current_board[1][1] == 0:
            ai_ind = [1, 1]
        if (self.current_board[1][1] + self.current_board[2][2]) == 2 and self.current_board[0][0] == 0:
            ai_ind = [0, 0]
        if (self.current_board[2][0] + self.current_board[1][1]) == 2 and self.current_board[0][2] == 0:
            ai_ind = [0, 2]
        if (self.current_board[2][0] + self.current_board[0][2]) == 2 and self.current_board[1][1] == 0:
            ai_ind = [1, 1]
        if (self.current_board[1][1] + self.current_board[0][2]) == 2 and self.current_board[2][0] == 0:
            ai_ind = [2, 0]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def check_fork(self):
        ai_ind = []
        for i in range(3):
            for j in range(3):
                if self.current_board[i][j] == 0:

                    self.current_board[i][j] = 5  # robie ruch

                    # sprawdzam czy po ruchu mam wiecej niz 1 opcje na wygreanie
                    wins = self.check_win_without_move()

                    if wins >= 2:
                        ai_ind = [i, j]

                    self.current_board[i][j] = 0

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def check_player_fork(self):
        ai_ind = []
        for i in range(3):
            for j in range(3):
                if self.current_board[i][j] == 0:

                    self.current_board[i][j] = 1  # robie ruch

                    # sprawdzam czy po ruchu mam wiecej niz 1 opcje na wygranie
                    wins = self.check_win_without_move()

                    if wins >= 2:
                        ai_ind = [i, j]

                    self.current_board[i][j] = 0

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def check_center(self):
        if self.current_board[1][1] == 0:
            self.move(1, 1)
            return True
        else:
            return False

    def opposite_corner(self):
        ai_ind = []
        if self.current_board[0][0] == 1 and self.current_board[2][2] == 0:
            ai_ind = [2, 2]
        elif self.current_board[2][2] == 1 and self.current_board[0][0] == 0:
            ai_ind = [0, 0]
        elif self.current_board[0][2] == 1 and self.current_board[2][0] == 0:
            ai_ind = [2, 0]
        elif self.current_board[2][0] == 1 and self.current_board[0][2] == 0:
            ai_ind = [0, 2]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def empty_corner(self):
        ai_ind = []
        if self.current_board[0][0] == 0:
            ai_ind = [0, 0]
        elif self.current_board[2][2] == 0:
            ai_ind = [2, 2]
        elif self.current_board[2][0] == 0:
            ai_ind = [2, 0]
        elif self.current_board[0][2] == 0:
            ai_ind = [0, 2]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True

    def empty_side(self):
        ai_ind = []
        if self.current_board[1][0] == 0:
            ai_ind = [1, 0]
        elif self.current_board[0][1] == 0:
            ai_ind = [0, 1]
        elif self.current_board[1][2] == 0:
            ai_ind = [1, 2]
        elif self.current_board[2][1] == 0:
            ai_ind = [2, 1]

        if len(ai_ind) == 0:
            return False
        else:
            self.move(ai_ind[0], ai_ind[1])
            return True


def on_click(ind, board):
    # if player_starts:
    board.move(ind[0], ind[1])
    board.ai_move()
    # else:
    #     board.ai_move()
    #     board.move(ind[0], ind[1])



def init_board():
    b.current_board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # player_starts = random.choice([True, False])

    # print(player_starts)
    btn_list.clear()
    for x in range(3):
        tmp_list = []
        for y in range(3):
            btn = Button(frame, command=lambda ind=(x, y): on_click(ind, b), text="", font=("Arial", 20))
            btn.grid(column=x, row=y, sticky="nesw")
            tmp_list.append(btn)
        btn_list.append(tmp_list)

    frame.columnconfigure(tuple(range(3)), weight=1)
    frame.rowconfigure(tuple(range(3)), weight=1)


if __name__ == '__main__':
    b = Board()
    # player_starts = random.choice([True, False])

    root = Tk()
    frame = Frame(root)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.geometry("600x600")
    frame.grid(row=0, column=0, sticky="news")
    grid = Frame(frame)

    btn_list = []

    init_board()

    btn = Button(frame, command=init_board, text="new game", font=("Arial", 30), bg="#FBC944")
    btn.grid(column=0, row=4, columnspan=3, sticky="nesw", pady=5, padx=5)

    label_info = Label(frame, text=f"player: {b.curr_player()}", font=("Arial", 30), bg="#FBC944")
    label_info.grid(column=0, row=3, columnspan=3, sticky="nesw", pady=5, padx=5)

    root.mainloop()
