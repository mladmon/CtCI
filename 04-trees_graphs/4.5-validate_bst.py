import sys

class Node:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None


# O(n) runtime, O(n) space - recursion depth is O(n) if not balanced
def check_valid_bst(root):
	return check_bst_helper(root, -sys.maxsize - 1, sys.maxsize)


# BST definition: left subtree <= n < right subtree
def check_bst_helper(n, low, high):
	if n is None:
		return True

	print(n.key, f'[{low}, {high}]')
	if n.key <= low or n.key > high:
		return False

	if check_bst_helper(n.left, low, n.key):
		return check_bst_helper(n.right, n.key, high)

	return False

def in_order_traversal(n):
	if n is not None:
		in_order_traversal(n.left)
		print(n.key, end=' ')
		in_order_traversal(n.right)


# Let's test it!
foo = Node(6)
foo.left, foo.right = Node(5), Node(7)
foo.left.left, foo.left.right = Node(2), Node(5)
foo.right.right = Node(8)

print('foo:', end=' ')
in_order_traversal(foo)
print()
print(check_valid_bst(foo))
print()

foo.left.right.key = 6
print('foo.left.right.key = 6')
print('foo:', end=' ')
in_order_traversal(foo)
print()
print(check_valid_bst(foo))
print()

foo.left.right.key = 7
print('foo.left.right.key = 7')
print('foo:', end=' ')
in_order_traversal(foo)
print()
print(check_valid_bst(foo))

