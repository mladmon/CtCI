from linked_list import *

def partition(head, x):
	last_lt, last_gt_eq, n, new_head = None, None, head, head
	while n:
		if n.data < x:
			# move node n
			if last_lt:
				temp = Node(n.data)
				temp.next = last_lt.next
				last_lt.next = temp
				last_lt = temp
			else:
				last_lt = Node(n.data)
				last_lt.next = head
				new_head = last_lt
			# remove old node n
			if n.next:
				n.data = n.next.data
				n.next = n.next.next
			else:
				if last_gt_eq:
					last_gt_eq.next = None
				else:
					last_lt.next = None
				break
		else:
			last_gt_eq = n
			n = n.next
	if new_head:
		return new_head
	else:
		return head

# Let's test it!
l1 = Node(3)
l1.append(5)
l1.append(8)
l1.append(5)
l1.append(10)
l1.append(2)
l1.append(1)

l2 = Node(3)
l2.append(1)

print_l(l1)
head = partition(l1, 5)
print_l(head)

print_l(l2)
head = partition(l2, 5)
print_l(head)
print_l(partition(head, 2))
