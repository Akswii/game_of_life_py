import pandas as pd


def create_board(x, y):
    return [[0 for i in range(x)] for j in range(y)]


def update_board(board, cell):
    # for i in board:
    #    print(i)
    #    for j in i:
    #        print(j)

    return board


def start_game():
    board_size_x = 5  # int(input("Horizontal size(X): "))
    board_size_y = 5  # int(input("Vertical size(Y): "))
    board = create_board(board_size_x, board_size_y)

    board[3][3] = 1
    board[3][2] = 1
    board[3][1] = 1

    return update_board(board)


print(pd.DataFrame(start_game()))
