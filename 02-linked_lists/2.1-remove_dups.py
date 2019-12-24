from linked_list import *

# O(n) runtime, O(n) space
def remove_dups(head):
   nodes = set()
   prev, n = None, head
   while n is not None:
      if n.data in nodes:
         prev.next = n.next
      else:
         nodes.add(n.data)
         prev = n 
      n = n.next


# O(n^2) runtime, O(1) space - temporary buffer not allowed
def remove_dups2(head):
	if head is None or head.next is None:
		return

	n1 = head
	while n1 is not None:
		prev, n2 = n1, n1.next
		while n2 is not None:
			if n2.data == n1.data:
				prev.next = n2.next
			else:
				prev = n2
			n2 = n2.next
		n1 = n1.next


# Let's test it!
if __name__ == '__main__':
	foo = Node(2)
	foo.append(2)
	foo.append(2)
	foo.append(3)
	foo.append(7)
	foo.append(2)
	foo.append(3)
	foo.append(5)
	foo.append(1)
	foo.append(2)

	print_list(foo)
	remove_dups(foo)
	#remove_dups2(foo)
	print_list(foo)
