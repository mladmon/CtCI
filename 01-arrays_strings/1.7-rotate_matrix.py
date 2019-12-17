# O(n^2) runtime, O(n^2) space - the Pythonic way to rotate an NxN matrix
def rotate_matrix(matrix):
	#return list(zip(*reversed(matrix)))              # list of tuples
	return [list(x) for x in zip(*reversed(matrix))]  # list of lists


# O(n^2) runtime, O(1) space - rotate an NxN matrix in place
def rotate_matrix2(matrix):
    n = len(matrix)
    for i in range(n // 2): 
        m = n - i * 2 
        for j in range(m - 1): 
            rotate(i, j, m, matrix)


def rotate(origin, col_offset, size, matrix):
    row, col = origin, origin + col_offset
    val = matrix[row][col]
    for i in range(4):
        new_row, new_col = col, origin + size-(row-origin)-1
        val, matrix[new_row][new_col] = matrix[new_row][new_col], val 
        row, col = new_row, new_col


# Let's test it! 
def print_matrix(matrix):
	for row in matrix:
		for elem in row:
			print(elem, end=' ')
		print()
	print()


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'a', 'b'], ['c', 'd', 'e', 'f']]
m3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 'a'], ['b', 'c', 'd', 'e', 'f'],
      ['g', 'h', 'i', 'j', 'k'], ['l', 'm', 'n', 'o', 'p']]

# rotate_matrix() returns a new matrix
print_matrix(m1)
print_matrix(rotate_matrix(m1))
 
# rotate_matrix2() modifies the original matrix
print_matrix(m1)
rotate_matrix3(m1)
print_matrix(m1)

print_matrix(m2)
rotate_matrix3(m2)
print_matrix(m2)

print_matrix(m3)
rotate_matrix3(m3)
print_matrix(m3)
