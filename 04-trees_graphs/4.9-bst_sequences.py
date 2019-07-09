from collections import deque

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def all_sequences(n):
	result = []
	if n is None:
		result.append(deque())
		return result

	prefix = deque([n.key])
	left_sequences = all_sequences(n.left)
	right_sequences = all_sequences(n.right)
	for l_seq in left_sequences:
		for r_seq in right_sequences:
			perms = []
			weave_lists(prefix, l_seq, r_seq, perms)
			result.extend(perms)
	return result

def weave_lists(prefix, first, second, perms):
	if len(first) == 0 or len(second) == 0:
		perm = prefix.copy()
		perm.extend(first)
		perm.extend(second)
		perms.append(perm)
		return

	prefix.append(first.popleft())
	weave_lists(prefix, first, second, perms)
	first.appendleft(prefix.pop())

	prefix.append(second.popleft())
	weave_lists(prefix, first, second, perms)
	second.appendleft(prefix.pop())

def print_sequences(tree):
	count = 0
	for sequence in all_sequences(tree):
		count += 1
		for num in sequence:
			print(num, end=' ')
		print()
	print('number of sequences:', count)

# Let's test it!
l = Node(20)
l.left, l.right = Node(10), Node(25)
l.left.left, l.left.right = Node(5), Node(15)

r = Node(60)
r.right = Node(70)
r.right.left, r.right.right = Node(65), Node(80)

root = Node(50)
root.left, root.right = l, r

print_sequences(l)
print_sequences(r)
print_sequences(root)
