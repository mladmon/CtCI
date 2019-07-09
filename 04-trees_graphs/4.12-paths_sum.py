class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def count_paths(t, target):
	if t is None:
		return 0
	count = dfs(t, target, 0)
	if t.left is not None:
		count += count_paths(t.left, target)
	if t.right is not None:
		count += count_paths(t.right, target)
	return count

def dfs(n, target, running_sum):
	if n is None:
		return 0
	running_sum += n.data
	num_paths = 0 if running_sum != target else 1
	num_paths += dfs(n.left, target, running_sum)
	num_paths += dfs(n.right, target, running_sum)
	return num_paths

# Let's test it!
r = Node(7)
r.left, r.right = Node(3), Node(4)
r.left.left, r.left.right = Node(2), Node(0)
r.right.right = Node(6)
r.left.left.left, r.left.left.right = Node(-2), Node(1)
r.left.left.right.right = Node(-3)
r.right.right.left, r.right.right.right = Node(-7), Node(3)

print('target 10:', count_paths(r, 10))
print('target 3:', count_paths(r, 3))
print('target 0:', count_paths(r, 0))
