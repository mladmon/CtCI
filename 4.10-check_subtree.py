class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# checks if t2 is a subtree of t1
def is_subtree(t1, t2):
	if t2 is None:
		return True
	set_heights(t1)
	set_heights(t2)
	return search(t1, t2)

def set_heights(t):
	if t is None:
		return -1
	left_h = set_heights(t.left)
	right_h = set_heights(t.right)
	t.height = left_h + 1 if left_h > right_h else right_h + 1
	return t.height

def search(n, subtree):
	if n is None or n.height < subtree.height:
		return False
	elif n.height == subtree.height:
		return check_match(n, subtree)
	else:
		return search(n.left, subtree) or search(n.right, subtree)

def check_match(t1, t2):
	if t1 is None and t2 is None:
		return True
	elif t1 is None or t2 is None or t1.key != t2.key:
		return False
	else:
		return check_match(t1.left, t2.left) and check_match(t1.right, t2.right)

# Let's test it!
r1 = Node(2)
r1.left, r1.right = Node(7), Node(35)
r1.left.right = Node(6)
r1.left.right.left, r1.left.right.right = Node(13), Node(5)
r1.right.right = Node(14)
r1.right.right.left, r1.right.right.right = Node(11), Node(90)
r1.right.right.left.right, r1.right.right.left.right.right = Node(90), Node(16)

r2 = Node(14)
r2.left, r2.right = Node(11), Node(90)
r2.left.right = Node(90)
r2.left.right.right = Node(16)

r3 = Node(14)
r3.left, r3.right = Node(11), Node(90)
r3.left.right = Node(90)

r4 = Node(6)
r4.left, r4.right = Node(13), Node(7)

print(is_subtree(r1, r2))
print(is_subtree(r1, r3))
print(is_subtree(r1, r4))
print(is_subtree(r1, r1))
print(is_subtree(r1, None))
