class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# O(n) runtime, O(n) space - depth of recursion is O(n) if not balanced
def check_balanced(root):
	height, balanced = check_helper(root)
	return balanced


def check_helper(n):
	if n is None:
		return (-1, True)

	left_height, balanced = check_helper(n.left)
	if not balanced:
		return (0, False)

	right_height, balanced = check_helper(n.right)
	if not balanced:
		return (0, False)

	print(n.key, left_height, right_height, sep='\t')
	diff = abs(left_height - right_height)
	if diff > 1:
		return (0, False)
		
	max_height = left_height if left_height > right_height else right_height
	return (max_height + 1, True)


# Let's test it!
foo = Node(1)
foo.left, foo.right = Node(2), Node(3)
foo.left.left, foo.left.right = Node(4), Node(5)
foo.right.left, foo.right.right = Node(6), Node(7)
foo.left.left.left = Node(8)
print('node\tleft\tright')
print(check_balanced(foo))
print()

foo.left.left.right = Node(9)
print('node\tleft\tright')
print(check_balanced(foo))
print()

foo.left.left.right.left = Node(10)
print('node\tleft\tright')
print(check_balanced(foo))
