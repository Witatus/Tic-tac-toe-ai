import random
import numpy as np


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
                self.current_player = 2
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

        if self.check_win(): #done
            return
        if self.check_block(): #done tutaj sie cos jebie
            return
        if self.check_fork(): #done
            return
        if self.check_player_fork(): #done
            return 
        if self.check_center(): #done
            return 
        if self.opposite_corner(): #done
            return
        if self.empty_corner(): #done
            return 
        if self.empty_side(): #done
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

                    self.current_board[i][j] = 5    #robie ruch

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


if __name__ == '__main__':
    b = Board()
    counter = 0

    while counter != 9:
        b.print_board()
        player_move = list(map(int, input().split()))
        b.move(int(player_move[0]), int(player_move[1]))
        b.print_board()
        b.ai_move()
        counter = counter + 1
