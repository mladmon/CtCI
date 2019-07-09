from linked_list import *

def remove_dups(head):
	nodes = {head.data}
	n = head
	while n.next is not None:
		if n.next.data in nodes:
			n.next = n.next.next
		else:
			nodes.add(n.next.data)
			n = n.next

def remove_dups2(head):
	if head is None or head.next is None:
		return
	n1 = head
	while n1.next is not None:
		n2 = n1
		while n2.next is not None:
			if n2.next.data == n1.data:
				n2.next = n2.next.next
			else:
				n2 = n2.next
		n1 = n1.next

# Let's test it!
if __name__ == '__main__':
	head = Node(2)
	head.append(2)
	head.append(2)
	head.append(3)
	head.append(7)
	head.append(2)
	head.append(3)
	head.append(5)
	head.append(1)
	head.append(2)

	print_l(head)
	remove_dups2(head)
	print_l(head)
