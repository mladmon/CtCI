class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

	def append(self, d):
		n = self
		while n.next is not None:
			n = n.next
		n.next = Node(d)


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
	print_l(head)
