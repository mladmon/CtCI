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

# Let's test it!
l1 = Node('A')
l1.append('B')
l1.append('C')
l1.append('D')
l1.append('E')
l1.next.next.next.next.next = l1.next.next
print('A B C D E C ', 'C', l1.next.next)
print('loop_detect:', loop_detect(l1).data, loop_detect(l1))
