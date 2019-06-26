class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def check_balanced(n):
	if n is None:
		return True
	h, balanced = check_helper(n)
	return balanced

def check_helper(n):
	if n is None:
		return (0, True)
	h_left, balanced = check_helper(n.left)
	if balanced:
		h_right, balanced = check_helper(n.right)
		print(n.key, h_left, h_right)
		if balanced:
			diff = h_left - h_right
			if diff < -1 or diff > 1:
				return (-1, False)
			else:
				largest = h_left if h_left > h_right else h_right
				return (largest + 1, True)
	return (-1, False) # don't care about height

# Let's test it!
r = Node(1)
r.left, r.right = Node(2), Node(3)
r.left.left, r.left.right = Node(4), Node(5)
r.right.left, r.right.right = Node(6), Node(7)
r.left.left.left = Node(8)
print(check_balanced(r))

r.left.left.right = Node(9)
print(check_balanced(r))

r.left.left.right.left = Node(10)
print(check_balanced(r))
