from collections import deque

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def list_of_depths(root):
	levels = []
	if root is None:
		return levels
	root.d = 0
	queue = deque([root])
	while queue:
		n = queue.popleft()
		add_to_levels(n, levels)
		if n.left is not None:
			n.left.d = n.d + 1
			queue.append(n.left)
		if n.right is not None:
			n.right.d = n.d + 1
			queue.append(n.right)
	return levels

def add_to_levels(n, levels):
	if len(levels) == n.d:
		n.next = None
		levels.append(n)
	else:
		n.next = levels[n.d]
		levels[n.d] = n

# Let's test it!
r = Node(1)
r.left, r.right = Node(2), Node(3)
r.left.left, r.left.right = Node(4), Node(5)
r.right.left, r.right.right = Node(6), Node(7)
r.left.left.left = Node(8)

depths = list_of_depths(r)
for i, d in enumerate(depths):
	print('depth {0}:'.format(i), end=' ')
	while d:
		print(d.key, end=' ')
		d = d.next
	print()
