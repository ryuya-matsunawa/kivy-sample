from itertools import product

def main(problem):
    """
    Solve the sudoku problem.

    Parameters
    ----------
    problem : list
        The sudoku problem.
    """
    if solve(problem, 0, 0):
        return problem

def solve(problem, row, col):
    """
    Solve the sudoku problem.

    Parameters
    ----------
    problem : list
        The sudoku problem.
    row : int
        The row index.
    col : int
        The column index.
    """
    if row == 9:
        return True
    if col == 9:
        return solve(problem, row + 1, 0)
    if problem[row][col] != 0:
        return solve(problem, row, col + 1)
    for i in range(1, 10):
        if is_valid(problem, row, col, i):
            problem[row][col] = i
            if solve(problem, row, col + 1):
                return True
            problem[row][col] = 0
    return False

def is_valid(problem, row, col, num):
    """
    Check if num is valid in the row, column and 3x3 box.

    Parameters
    ----------
    problem : list
        The sudoku problem.
    row : int
        The row index.
    col : int
        The column index.
    num : int
        The number to check.
    """
    for i in range(9):
        if problem[row][i] == num:
            return False
        if problem[i][col] == num:
            return False
    for (i, j) in product(range(3), repeat=2):
        if problem[row//3*3 + i][col//3*3 + j] == num:
            return False
    return True
