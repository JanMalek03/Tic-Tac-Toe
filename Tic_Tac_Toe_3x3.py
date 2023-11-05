import os

BOARD_SIZE = 3


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')        


class TicTacToe_3x3:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, BOARD_SIZE):
            print(' | '.join(self.board[i]))

    def is_valid(self, x, y):
        if x < 0 or x > (BOARD_SIZE - 1) or y < 0 or y > (BOARD_SIZE - 1):
            return False

        return self.board[x][y] == '.'

    def get_result(self):
        # TEST ROWS
        for row in self.board:
            if (row == ['X','X','X']):
                return 'X'
            if (row == ['O','O','O']):
                return 'O'

        # TEST COLS
        for col in range(BOARD_SIZE):
            block = self.board[0][col] + self.board[1][col] + self.board[2][col]
            if (block == "XXX"):
                return 'X'
            if (block == "OOO"):
                return 'O'

        # TEST FIRST DIAGONAL
        block = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if (block == "XXX"):
            return 'X'
        if (block == "OOO"):
            return 'O'

        # TEST SECOND DIAGONAL
        block = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if (block == "XXX"):
            return 'X'
        if (block == "OOO"):
            return 'O'

        # TEST IF BOARD IS FULL
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                if (self.board[i][j] == '.'):
                    return None

        return '.'


def maxi(game, alpha, beta):
    maxv = -2
    x = None
    y = None

    result = game.get_result()
    if result == 'X':
        return (-1, None, None)
    elif result == 'O':
        return (1, None, None)
    elif result == '.':
        return (0, None, None)


    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if game.board[i][j] == '.':
                game.board[i][j] = 'O'
                (m, _, _) = mini(game, alpha, beta)
                if m > maxv:
                    maxv = m
                    x = i
                    y = j
                game.board[i][j] = '.'

                if maxv > alpha:
                    alpha = maxv
                if beta <= alpha:
                    return (maxv, x, y)

    return (maxv, x, y)


def mini(game, alpha, beta):
    minv = 2
    x = None
    y = None

    result = game.get_result()
    if result == 'X':
        return (-1, None, None)
    elif result == 'O':
        return (1, None, None)
    elif result == '.':
        return (0, None, None)

    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if game.board[i][j] == '.':
                game.board[i][j] = 'X'
                (m, _, _) = maxi(game, alpha, beta)
                if m < minv:
                    minv = m
                    x = i
                    y = j
                game.board[i][j] = '.'

                if minv < beta:
                    beta = minv
                if beta <= alpha:
                    return (minv, x, y)

    return (minv, x, y)


def play_game(game):
    while(True):
        clear_terminal()
        game.draw_board()

        result = game.get_result()
        if result != None:
            if (result == 'X'):
                print("THE WINNER IS X!")
            elif (result == 'O'):
                print("THE WINNER IS O!")
            else:
                print("DRAW!")

            game.initialize_game()
            return

        if game.player_turn == 'O':     # AI plays
            (_, x, y) = maxi(game, -2, 2)
            game.board[x][y] = 'O'
            game.player_turn = 'X'

        else:       # Player plays
            while True:
                correct_format, x, y = False, -1, -1
                while not correct_format:
                    try:
                        x = int(input(f"Enter the ROW coordinate (1 - {BOARD_SIZE}): ")) - 1
                        y = int(input(f"Enter the COL coordinate (1 - {BOARD_SIZE}): ")) - 1
                        correct_format = True
                    except ValueError:
                        print("Invalid format, please repeat!")
                        correct_format = False

                if game.is_valid(x, y):
                    game.board[x][y] = 'X'
                    game.player_turn = 'O'
                    break
                else:
                    print("Invalid move, please repeat!")


if __name__ == "__main__":
    play_game(TicTacToe_3x3())
