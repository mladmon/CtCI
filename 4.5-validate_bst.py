class Node:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None

# First attempt wrong (need to verify all nodes in a subtree <= or >= n.key)
def validate_bst(n):
	if n is None:
		return True
	if validate_bst(n.left):
		if n.left is not None:
			if n.left.key > n.key:
				return False
		if validate_bst(n.right):
			if n.right is not None:
				if n.right.key < n.key:
					return False
			return True
	return False

def validate_bst2(n):
	if n is None:
		return True
	keys = []
	inorder_walk(n, keys)
	print(keys)
	k = keys[0]
	for i in range(1, len(keys)):
		if keys[i] < k:
			return False
		k = keys[i]
	return True

def inorder_walk(n, keys):
	if n is not None:
		inorder_walk(n.left, keys)
		keys.append(n.key)
		inorder_walk(n.right, keys)

def validate_bst3(n):
	return bst_helper(n, None, None)

def bst_helper(n, low, high):
	if n is None:
		return True
	print(n.key, low, high)
	if low is not None and n.key <= low or high is not None and n.key > high:
		return False
	if not bst_helper(n.left, low, n.key) or not bst_helper(n.right, n.key, high):
		return False
	return True

# Let's test it!
r = Node(6)
r.left, r.right = Node(5), Node(7)
r.left.left, r.left.right = Node(2), Node(5)
r.right.right = Node(8)

r2 = Node(6)
r2.left, r2.right = Node(5), Node(7)
r2.left.left, r2.left.right = Node(2), Node(7)
r2.right.right = Node(8)

print('CLRS: left subtree <= n.key <= right subtree')
print(validate_bst2(r))
print(validate_bst2(r2))
print()
print('CtCI: left subtree <= n.key < right subtree')
print(validate_bst3(r))
print(validate_bst3(r2))
