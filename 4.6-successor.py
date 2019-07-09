class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

def successor(n):
	if n is None:
		return None
	if n.right is not None:
		return minimum(n.right)
	p = n.parent
	while p is not None and n is p.right:
		n, p = p, p.parent
	return p

def minimum(n):
	p = n
	while n is not None:
		p, n = n, n.left
	return p

# Let's test it!
# BST from CLRS pg. 290
r = Node(15)
r.left, r.right = Node(6), Node(18)
r.left.parent, r.right.parent = r, r
r.left.left, r.left.right = Node(3), Node(7)
r.left.left.parent, r.left.right.parent = r.left, r.left
r.right.left, r.right.right = Node(17), Node(20)
r.right.left.parent, r.right.right.parent = r.right, r.right
r.left.left.left, r.left.left.right = Node(2), Node(4)
r.left.left.left.parent, r.left.left.right.parent = r.left.left, r.left.left
r.left.right.right = Node(13)
r.left.right.right.parent = r.left.right
r.left.right.right.left = Node(9)
r.left.right.right.left.parent = r.left.right.right

print('6:', successor(r.left).key)
print('7:', successor(r.left.right).key)
print('4:', successor(r.left.left.right).key)
print('13:', successor(r.left.right.right).key)
print('15:', successor(r).key)
print('20:', successor(r.right.right))
