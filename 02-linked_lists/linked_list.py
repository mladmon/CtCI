class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

	def append(self, d):
		n = self
		while n.next is not None:
			n = n.next
		n.next = Node(d)

	def search(self, d):
		n = self
		while n is not None:
			if n.data == d:
				return n
			n = n.next
		return None


def print_list(head):
	n = head
	while n is not None:
		print(n.data, end=' ')
		n = n.next
	print()


# Let's test it!
if __name__ == '__main__':
	foo = Node(2)
	foo.append(3)
	foo.append(7)
	foo.append(2)
	foo.append(3)
	foo.append(5)
	foo.append(1)
	foo.append(2)

	n1 = foo.search(7)
	n2 = n1.search(5)
	n3 = foo.search(99)

	print_list(foo)
	print_list(n1)
	print_list(n2)
	print(n3)
