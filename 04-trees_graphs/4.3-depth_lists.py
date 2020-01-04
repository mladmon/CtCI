from collections import deque

# a tree node class - we add 'depth' and 'next' attributes on the fly below
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# O(n) runtime, O(n) space - use BFS to traverse the tree level-by-level
def list_of_depths(root):
	levels = []
	if root is None:
		return levels

	root.depth = 0
	queue = deque([root])
	while queue:
		n = queue.popleft()
		add_to_list(n, levels)

		if n.left is not None:
			n.left.depth = n.depth + 1
			queue.append(n.left)
		if n.right is not None:
			n.right.depth = n.depth + 1
			queue.append(n.right)

	return levels


def add_to_list(n, levels):
	if len(levels) == n.depth:
		n.next = None
		levels.append(n)
	else:
		n.next = levels[n.depth]
		levels[n.depth] = n


# Let's test it!
foo = Node(1)
foo.left, foo.right = Node(2), Node(3)
foo.left.left, foo.left.right = Node(4), Node(5)
foo.right.left, foo.right.right = Node(6), Node(7)
foo.left.left.left = Node(8)

foo_depths = list_of_depths(foo)
for depth, head in enumerate(foo_depths):
	print(f'depth {depth}:', end=' ')
	while head is not None:
		print(head.key, end=' ')
		head = head.next
	print()
