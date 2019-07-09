class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

#def common_ancestor(root, n1, n2):
#	if n1 is root or n2 is root:
#		return root
#	if dfs(n1, n2):
#		return n1
#	elif dfs(n2, n1):
#		return n2
#	else:
#		return root

def common_ancestor(root, n1, n2):
	if root is None:
		return (None, False, False)
	if root is n1:
		return (n1, True, dfs(n1, n2))
	ancestor, found_n1, found_n2 = common_ancestor(root.left, n1, n2)
	if found_n1:
		if found_n2:
			return (ancestor, True, True)
		return (root, True, dfs(root, n2))
	ancestor, found_n1, found_n2 = common_ancestor(root.right, n1, n2)
	if found_n1:
		if found_n2:
			return (ancestor, True, True)
		return (root, True, dfs(root, n2))
	return (None, False, False)

def dfs(root, n):
	if root is None:
		return False
	if root is n:
		return True
	if not dfs(root.left, n):
		return dfs(root.right, n)
	return True

# Let's test it!
r = Node(13)
r.left, r.right = Node(6), Node(7)
r.left.left = Node(8)
r.right.left, r.right.right = Node(1), Node(17)
r.left.left.right = Node(2)
r.right.right.left, r.right.right.right = Node(4), Node(3)
r.right.right.left.left = Node(9)

ancestor, f1, f2 = common_ancestor(r, r.right.left, r.right.right.right)
print(1, 3, ancestor.key)
ancestor, f1, f2 = common_ancestor(r, r.right.right.right, r.right.left)
print(3, 1, ancestor.key)
ancestor, f1, f2 = common_ancestor(r, r.left.left, r.right.right.left)
print(8, 4, ancestor.key)
ancestor, f1, f2 = common_ancestor(r, r.left.left.right, r.left)
print(2, 6, ancestor.key)
ancestor, f1, f2 = common_ancestor(r, r.left.left, r.left.left)
print(8, 8, ancestor.key, f1, f2)
ancestor, f1, f2 = common_ancestor(r, r.left, None)
print(6, None, ancestor.key, f1, f2)

