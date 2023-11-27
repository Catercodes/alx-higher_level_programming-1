#!/usr/bin/python3


def looks_of_the_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
    print()


def safe_place(board, row, col):
    # check for the vertical and horizontal moves
    for i in range(column):
        if board[row][col] == 1:
            return False

    # check for upper the diagonal movement
    for i, j in zip(range(row - 1, -1), range(col - 1, -1)):
        if board[row][col] == 1:
            return False
    # chaeck for the upper diagonal movemet
    for i, j in zip(range(N, row, 1), range(col, -1, -1)):
        if board[row][col] == 1:
            return False
    return True

def solve_no_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if safe_place(board, col, i):
            board[i][col]=1
        if solve_no_queen(board, col + 1) == True:
            return True
    return False


N=8
looks_of_the_board(n)
