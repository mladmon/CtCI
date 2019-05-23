def rotate_matrix(matrix):
	#return list(zip(*reversed(matrix)))				# list of tuples
	return [list(x) for x in zip(*reversed(matrix))]	# list of lists

# Let's test it!
def print_m(m):
	for row in m:
		for e in row:
			print(e, end=' ')
		print()
	print()

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_m(m1)
print_m(rotate_matrix(m1))
