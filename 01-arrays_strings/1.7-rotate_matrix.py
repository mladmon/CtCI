# O(n^2) runtime, O(n^2) space - the Pythonic way to rotate an NxN matrix
def rotate_matrix(matrix):
	#return list(zip(*reversed(matrix)))              # list of tuples
	return [list(x) for x in zip(*reversed(matrix))]  # list of lists


# O(n^2) runtime, O(1) space - rotate an NxN matrix in place
def rotate_matrix_in_place(matrix):
   n = len(matrix)
   if n < 2:
      return;

   num_layers = n // 2
   for i in range(num_layers):
      layer_size = n - 2 * i 
      for j in range(layer_size - 1): 
         # store top
         top = matrix[i][i+j]

         # left --> top
         matrix[i][i+j] = matrix[n-1-i-j][i]

         # bottom --> left
         matrix[n-1-i-j][i] = matrix[n-1-i][n-1-i-j]

         # right --> bottom
         matrix[n-1-i][n-1-i-j] = matrix[i+j][n-1-i]

         # top --> right
         matrix[i+j][n-1-i] = top


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

# rotate_matrix() returns a new rotated matrix
print_matrix(m1)
print_matrix(rotate_matrix(m1))
 
# rotate_matrix_in_place() rotates the original matrix
print_matrix(m1)
rotate_matrix_in_place(m1)
print_matrix(m1)

print_matrix(m2)
rotate_matrix_in_place(m2)
print_matrix(m2)

print_matrix(m3)
rotate_matrix_in_place(m3)
print_matrix(m3)
