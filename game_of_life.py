import pandas as pd


def create_board(x, y):
    return [[0 for i in range(x)] for j in range(y)]


def living_cells(board):
    cells = []

    for i, val in enumerate(board):
        print("Index: {}, Value: {}".format(i, val))
        for j, value in enumerate(val):
            if board[j][i] == 1:
                cells.append([j, i])
                #print("X index: {}, Y index: {}".format(j, i))

    return cells


def start_game():
    board_size_x = 5
    board_size_y = 5
    board = create_board(board_size_x, board_size_y)

    board[3][3] = 1
    board[2][3] = 1
    board[1][3] = 1

    print(pd.DataFrame(board))

    return living_cells(board)


print(start_game())
