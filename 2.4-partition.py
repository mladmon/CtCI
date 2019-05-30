from linked_list import *

def partition(head, x):
	part_node, n, new_head, sec_to_last = None, head, head, None
	while n:
		print(n.data)
		if n.data < x:
			# move node n
			if part_node:
				temp = Node(n.data)
				temp.next = part_node.next
				part_node.next = temp
				part_node = temp
			else:
				part_node = Node(n.data)
				part_node.next = head
				new_head = part_node
			# remove old node n
			if n.next: # n is not the last node
				if n.next.next is None:
					sec_to_last = n
				n.data = n.next.data
				n.next = n.next.next
			else: # n is the last node
				if sec_to_last:
					sec_to_last.next = None	
		else:
			n = n.next
	return new_head

# Let's test it!
l1 = Node(3)
l1.append(5)
l1.append(8)
l1.append(5)
l1.append(10)
l1.append(2)
l1.append(1)

print_l(l1)
head = partition(l1, 5)
print_l(head)
