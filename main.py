"""Backtracking Sudoku Solver.

Solves a 9x9 Sudoku puzzle using a recursive backtracking algorithm.
"""

from __future__ import annotations

from typing import Optional

EMPTY = 0
SIZE = 9

EXAMPLE_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(board: list[list[int]]) -> None:
    """Print the board in a human-readable grid format."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        line = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                line += "| "
            line += f"{val if val != EMPTY else '.'} "
        print(line.rstrip())


def find_empty(board: list[list[int]]) -> Optional[tuple[int, int]]:
    """Return the (row, col) of the first empty cell, or None if full."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == EMPTY:
                return (r, c)
    return None


def is_valid(board: list[list[int]], row: int, col: int, num: int) -> bool:
    """Check whether placing `num` at (row, col) is valid."""
    if num in board[row]:
        return False
    if any(board[r][col] == num for r in range(SIZE)):
        return False
    box_r, box_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if board[r][c] == num:
                return False
    return True


def solve(board: list[list[int]]) -> bool:
    """Solve the board in-place using backtracking. Return True if solved."""
    cell = find_empty(board)
    if cell is None:
        return True
    row, col = cell
    for num in range(1, SIZE + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = EMPTY
    return False


def main() -> None:
    """Run the solver on the example board."""
    board = [row[:] for row in EXAMPLE_BOARD]
    print("Puzzle:")
    print_board(board)
    print()
    if solve(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
