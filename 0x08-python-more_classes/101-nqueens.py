#!/usr/bin/python3
import sys


class NQueens:

    def __init__(self, n):
        """
        Constructor for the NQueens class.

        Parameters:
        n (int): The size of the chessboard.
        """
        self.n = n
        self.columns = []
        self.solutions = []

    def solve(self):
        """
        Finds all possible solutions
        to the N Queens puzzle.

        Returns:
        solutions (list): A list of all possible solutions,
        where each solution is a list of tuples
        representing the position of the queens.
        """
        self.columns = []
        self._solve(0)
        return self.solutions

    def _solve(self, row):
        """
        Helper method to recursively find
        all possible solutions to the N Queens puzzle.

        Parameters:
        row (int): The current row being checked.
        """
        # If we've placed a queen in every row, we've found a solution!
        if row == self.n:
            solution = []
            for i in range(self.n):
                solution.append([i, self.columns[i]])
            self.solutions.append(solution)
            return

        # Try placing a queen in every column of the current row
        for col in range(self.n):
            if self._is_valid(row, col):
                self.columns.append(col)
                self._solve(row+1)
                self.columns.pop()

    def _is_valid(self, row, col):
        """
        Helper method to check if a queen
        can be placed in a given row and column.

        Parameters:
        row (int): The row being checked.
        col (int): The column being checked.

        Returns:
        valid (bool): True if the queen can be placed
        in the given row and column, False otherwise.
        """
        for r, c in enumerate(self.columns):
            # Check if there's already a queen in this column or diagonal
            if c == col or r+c == row+col or r-c == row-col:
                return False
        return True


if __name__ == '__main__':
    # Check arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the puzzle
    nqueens = NQueens(n)
    solutions = nqueens.solve()

    # Print solutions
    for solution in solutions:
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(solution[i][0], solution[i][1]), end="")
            if i != n-1:
                print(", ", end="")
        print("]")
