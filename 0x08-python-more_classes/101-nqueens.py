#!/usr/bin/python3

class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if a queen can be placed at the given position without attacking other queens

        # Check the row on the left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check the upper diagonal on the left side
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal on the left side
        i = row
        j = col
        while i < self.N and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solve_nqueens(self, col):
        # Recursive function to solve the N queens problem

        # If all queens are placed, add the solution to the list
        if col >= self.N:
            self.add_solution()
            return True

        # Try placing a queen in each row of the current column
        for i in range(self.N):
            if self.is_safe(i, col):
                # Place the queen
                self.board[i][col] = 1

                # Recur to place the rest of the queens
                self.solve_nqueens(col + 1)

                # Backtrack and remove the queen from the current position
                self.board[i][col] = 0

    def add_solution(self):
        # Add the current board configuration as a solution
        solution = []
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1:
                    solution.append([i, j])
        self.solutions.append(solution)

    def find_solutions(self):
        # Solve the N queens problem and return the solutions
        self.solve_nqueens(0)
        return self.solutions
