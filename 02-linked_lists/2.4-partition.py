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
foo = Node(3)
foo.append(5)
foo.append(8)
foo.append(5)
foo.append(10)
foo.append(2)
foo.append(1)

bar = Node(3)
bar.append(1)

print_list(foo)
head = partition(foo, 5)
print_list(head)

print_list(bar)
head = partition(bar, 5)
print_list(head)
print_list(partition(head, 2))
