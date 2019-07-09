from linked_list import *

def loop_detect(head):
	n, nodes = head, set()
	while n is not None:
		if n in nodes:
			return n
		else:
			nodes.add(n)
			n = n.next
	return None

def loop_detect2(head):
	n1, n2 = head, head
	while n2 is not None and n2.next is not None:
		n2 = n2.next.next
		n1 = n1.next
		if n1 is n2:
			break
	if n2 is None or n2.next is None:
		return None
	# loop exists and n1, n2 (and head) are k steps away from loop beginning
	n1 = head
	while n1 is not n2:
		n1, n2 = n1.next, n2.next
	return n1

# Let's test it!
l1 = Node('A')
l1.append('B')
l1.append('C')
l1.append('D')
l1.append('E')
l1.next.next.next.next.next = l1.next.next
print('A B C D E C ...')
n = loop_detect2(l1)
print('loop_detect:', n.data, n)

l2 = Node(5)
l2.append(1)
l2.append(3)
l2.append(7)
print_l(l2)
print('loop_detect:', loop_detect2(l2))

l3 = Node(6)
l3.append(5)
l3.append(1)
l3.append(3)
l3.append(7)

print_l(l3)
print('loop_detect:', loop_detect2(l3))

l4 = Node(5)
l4.next = l4
print('5 5 ...')
n = loop_detect2(l4)
print('loop_detect:', n.data, n)

l6 = Node(5)
print_l(l6)
print('loop_detect:', loop_detect2(l6))

l5 = Node(30)
l5.append(35)
l5.next.next = l5
print('30 35 30 ...')
n = loop_detect2(l5)
print('loop_detect:', n.data, n)

l7 = Node(30)
l7.append(35)
print_l(l7)
print('loop_detect:', loop_detect2(l7))
