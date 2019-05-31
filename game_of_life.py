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

    for x in range(-1, 2):
        for y in range(-1, 2):
            if board[living_cell_y + y][living_cell_x + x] == 1 and [y, x] != [0, 0]:
                num_neighbours += 1

    return num_neighbours


def advance_game(board, cells):
    new_board = create_board(len(board), len(board[0]))

    return new_board


# Runs the game of life
def run_game():
    board_size_x = 10
    board_size_y = 10
    board = create_board(board_size_x, board_size_y)

    board[1][5] = 1
    board[2][5] = 1
    board[3][5] = 1

    print(pd.DataFrame(board))

    living_cells = get_living_cells(board)

    print(living_cells)

    #for cell in living_cells:
    get_num_neighbours(living_cells[0], board)


run_game()
