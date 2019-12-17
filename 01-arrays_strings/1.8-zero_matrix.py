# O(m*n) runtime, O(m+n) space 
def zero_matrix(matrix):
	zero_rows = [False] * len(matrix)    # m
	zero_cols = [False] * len(matrix[0]) # n
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				zero_rows[i] = True
				zero_cols[j] = True

	for i in range(len(zero_rows)):
		if zero_rows[i]:
			matrix[i] = [0] * len(matrix[0])
	for j in range(len(zero_cols)):
		if zero_cols[j]:
			for row in matrix:
				row[j] = 0


# Let's test it!
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()
    print()

foo = [[1, 7, 8, 0, 3, 2, 7, 5],
      [2, 0, 0, 1, 7, 8, 9, 3],
      [2, 1, 3, 2, 9, 1, 4, 4],
      [2, 0, 6, 1, 7, 8, 9, 3],
      [3, 2, 5, 2, 8, 9, 6, 0]]

print_matrix(foo)
zero_matrix(foo)
print_matrix(foo)
