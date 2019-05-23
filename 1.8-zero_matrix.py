def zero_matrix(mat):
	m, n = len(mat), len(mat[0])
	rows, cols = [False] * m, [False] * n
	for i, row in enumerate(mat):
		for j, ele in enumerate(row):
			if ele is 0:
				rows[i] = True
				cols[j] = True
	for i in range(len(rows)):
		if rows[i] is True:
			mat[i] = [0] * n
	for j in range(len(cols)):
		if cols[j] is True:
			zero_col(j, mat)

def zero_col(col, mat):
	for row in mat:
		row[col] = 0


# Let's test it!
def print_m(m):
    for row in m:
        for e in row:
            print(e, end=' ')
        print()
    print()

m1 = [[1, 7, 8, 0, 3, 2, 7, 5],
      [2, 0, 0, 1, 7, 8, 9, 3],
      [2, 1, 3, 2, 9, 1, 4, 4],
      [2, 0, 6, 1, 7, 8, 9, 3],
      [3, 2, 5, 2, 8, 9, 6, 0]]
print_m(m1)
zero_matrix(m1)
print_m(m1)
