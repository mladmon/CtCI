class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

	def append(self, d):
		n = self
		while n.next is not None:
			n = n.next
		n.next = Node(d)

	def search(self, k):
		n = self
		while n is not None:
			if n.data == k:
				return n
			n = n.next
		return None

def print_l(head):
	n = head
	while n is not None:
		print(n.data, end=' ')
		n = n.next
	print()


# Let's test it!
if __name__ == '__main__':
	head = Node(2)
	head.append(3)
	head.append(7)
	head.append(2)
	head.append(3)
	head.append(5)
	head.append(1)
	head.append(2)

	n1 = head.search(7)
	n2 = n1.search(5)
	n3 = head.search(99)

	print_l(head)
	print_l(n1)
	print_l(n2)
	print(repr(n3))
