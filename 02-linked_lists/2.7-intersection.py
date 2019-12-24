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

def intersection2(l1, l2):
	size1, size2, n1, n2 = 1, 1, l1, l2
	if n1 is None or n2 is None:
		return None
	while n1.next:
		size1 += 1
		n1 = n1.next
	while n2.next:
		size2 += 1
		n2 = n2.next
	if n1 is not n2:
		return None
	else:
		if size1 >= size2:
			return find_intersect(l1, l2, size1-size2)
		else:
			return find_intersect(l2, l1, size2-size1)

def find_intersect(l1, l2, k):
	n1, n2 = l1, l2
	for i in range(k):
		n1 = n1.next
	while n1 is not n2:
		n1, n2 = n1.next, n2.next
	return n1

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
print_list(l1)
print('3:', l1.next)
print('l2:', end=' ')
print_list(l2)
print('3:', l2.next.next)
print('l3:', end=' ')
print_list(l3)
print('3:', l3.next.next)
print('intersection(l1, l2):', intersection2(l1, l2))
print('intersection(l1, l3):', intersection2(l1, l3))
print('intersection(l2, l3):', intersection2(l2, l3))
