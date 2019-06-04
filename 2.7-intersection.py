from linked_list import *

def intersection(l1, l2):
	nodes = set()
	n1, n2 = l1, l2
	while n1 is not None:
		nodes.add(n1)
		n1 = n1.next
	while n2 is not None:
		if n2 in nodes:
			return n2
		n2 = n2.next
	return None

# Let's test it!
l1 = Node(7)
l1.append(3)
l1.append(8)
l1.append(9)

l2 = Node(5)
l2.append(11)
l2.append(3)
l2.append(6)

l3 = Node(12)
l3.append(16)
l3.next.next = l1.next

print('l1:', end=' ')
print_l(l1)
print('3:', l1.next)
print('l2:', end=' ')
print_l(l2)
print('3:', l2.next.next)
print('l3:', end=' ')
print_l(l3)
print('3:', l3.next.next)
print('intersection(l1, l2):', intersection(l1, l2))
print('intersection(l1, l3):', intersection(l1, l3))
print('intersection(l2, l3):', intersection(l2, l3))
