import pandas as pd


# Creates a board with the given x and y dimensions.
def create_board(x, y):
    return [[0 for i in range(x)] for j in range(y)]


# Finds all living cells on the board.
def get_living_cells(board):
    cells = []

    for i, val in enumerate(board):
        for j, value in enumerate(val):
            if board[j][i] == 1:
                cells.append([j, i])
                # print("Y index: {}, X index: {}".format(j, i))

    return cells


# Finds the number of direct neighbours to a given cell.
def get_num_neighbours(cell, board):
    num_neighbours = 0

    living_cell_y = cell[0]
    living_cell_x = cell[1]

    for x in range(0 if living_cell_x == 0 else - 1, 1 if living_cell_x == len(board) - 1 else 2):
        for y in range(0 if living_cell_y == 0 else - 1, 1 if living_cell_y == len(board[0]) - 1 else 2):
            if board[living_cell_y + y][living_cell_x + x] == 1 and [y, x] != [0, 0]:
                num_neighbours += 1

    return num_neighbours


# Checks if the given cell lives in the next iteration or not
def new_value(cell, num_neighbours):
    if cell == 1:
        if num_neighbours < 2:
            return 0
        elif num_neighbours == 2 or num_neighbours == 3:
            return 1
        elif num_neighbours > 3:
            return 0
    elif cell == 0:
        if num_neighbours == 3:
            return 1
    return 0


def advance_game(board):
    new_board = create_board(len(board), len(board[0]))

    for i, y in enumerate(board):
        for j, x in enumerate(y):
            num_neighbours = get_num_neighbours([i, j], board)

            # print("Y: {}, X: {}".format(i, j))

            new_board[i][j] = new_value(board[i][j], num_neighbours)

    return new_board


# Runs the game of life
def run_game():
    board_size_x = 10
    board_size_y = 10
    board = create_board(board_size_x, board_size_y)

    board[4][3] = 1
    board[3][5] = 1
    board[4][5] = 1
    board[5][5] = 1
    board[5][4] = 1

    # print(pd.DataFrame(board))

    while get_living_cells(board):
        print(pd.DataFrame(board))
        print("")
        board = advance_game(board)
        input("Press Enter to continue...")


run_game()

# Endless life
# board[3][2] = 1
# board[2][2] = 1
# board[2][3] = 1

# board[4][5] = 1
# board[5][5] = 1
# board[5][4] = 1
