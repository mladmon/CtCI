class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def inorder_tree_walk(n):
	if n is not None:
		inorder_tree_walk(n.left)
		print(n.key, end=' ')
		inorder_tree_walk(n.right)

def min_height_bst(keys):
	return create_bst(keys, 0, len(keys)-1)

def create_bst(arr, start, end):
	if end < start:
		return None
	mid = (start + end) // 2
	print('mid:', mid)
	n = Node(arr[mid])
	n.left = create_bst(arr, start, mid-1)
	n.right = create_bst(arr, mid+1, end)
	return n

# Let's test it!
keys = [0, 2, 5, 9, 11, 12, 17, 20, 23]
print('keys:', keys)
tree = min_height_bst(keys)
print('bst:', end=' ')
inorder_tree_walk(tree)
print()
