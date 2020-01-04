class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def inorder_tree_walk(node):
	if node is not None:
		inorder_tree_walk(node.left)
		print(node.key, end=' ')
		inorder_tree_walk(node.right)


# O(n) runtime, O(log n) space - not including the BST we're creating,
# depth of recursion is O(log n); use binary search to recursively
# construct the BST
def create_bst(arr):
	return create_bst_helper(arr, 0, len(arr)-1)


def create_bst_helper(arr, left, right):
	if right < left:
		return None

	mid = (left + right) // 2
	print('mid:', mid)
	n = Node(arr[mid])
	n.left = create_bst_helper(arr, left, mid-1)
	n.right = create_bst_helper(arr, mid+1, right)

	return n


# Let's test it!
foo = [0, 2, 5, 9, 11, 12, 17, 20, 23]
print('foo:', foo)
foo_tree = create_bst(foo)
print('foo_tree:', end=' ')
inorder_tree_walk(foo_tree)
print()
