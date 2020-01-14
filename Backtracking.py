def solve_sudoku(sudoku, square=49):
	row = square // 9
	column = square % 9
	for number in range(1,10):
		if writeable_number(column, row, number, sudoku):
			sudoku[row][column] = number

def writeable_number(column, row, number, sudoku):
	return True
