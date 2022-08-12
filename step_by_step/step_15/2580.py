lst = []
for i in range(9):
	lst.append(list(map(int, input().split())))

def check(row, column, i):
	if i in lst[row]:
		return False
	for j in range(9):
		if lst[j][column] == i:
			return False
	for j in range(row // 3 * 3, row // 3 * 3 + 3):
		for k in range(column // 3 * 3, column // 3 * 3 + 3):
			if lst[j][k] == i:
				return False
	return True

def sudoku(row, column):
	if row == 9:
		for i in range(9):
			print(" ".join(map(str,lst[i])))
		exit(0)
	elif column == 9:
		sudoku(row + 1, 0)
	else:
		if lst[row][column] == 0:
			for j in range(1, 10):
				if check(row, column, j):
					lst[row][column] = j
					sudoku(row, column + 1)
					lst[row][column] = 0
		else:
			sudoku(row, column + 1)

sudoku(0, 0)
