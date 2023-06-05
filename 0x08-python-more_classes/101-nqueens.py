#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position without attacking other queens

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Recursive function to solve the N queens problem

    # If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from the current position
            board[i][col] = 0

def print_solution(board):
    # Print the board configuration
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [[0] * N for _ in range(N)]

# Solve the N queens problem
solve_nqueens(board, 0)
