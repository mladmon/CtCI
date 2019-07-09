import random

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

class BinaryTree:
	def __init__(self):
		self.nodes = {}

	def insert(self, node):
		self.nodes[node.key] = node
		# TODO: insert node into tree

	def delete(self, key):
		n = self.nodes.pop(key)
		# TODO: delete node from tree

	def find(self, key):
		return self.nodes[key]

	def get_random_node(self):
		return self.nodes[random.choice(list(self.nodes.keys()))]


# Let's test it!
if __name__ == "__main__":
	b = BinaryTree()
	for i in range(1, 21):
		b.insert(Node(i))
	
	print(b.find(7).key)
	b.delete(7)
	for i in range(5):
		print(b.get_random_node().key)
