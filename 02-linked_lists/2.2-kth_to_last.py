from linked_list import *

# Definition: k = 0, 1 --> 'last', k = 2 --> '2nd to last', etc.
# O(n) runtime, O(1) space - makes 2 passes: calc. size, advance
def kth_to_last(head, k):
	if k == 0:
		k = 1

	size = 0
	n = head
	while n is not None:
		size += 1
		n = n.next

	if size < k:
		return None
	else:
		n = head
		for i in range(size - k):
			n = n.next
		return n


# O(n) runtime, O(1) space - better solution: single pass
def kth_to_last2(head, k):
	if head is None:
		return head

	# advance second k - 1 nodes
	first, second = head, head
	for i in range(k - 1):
		if second is None or second.next is None:
			return None
		second = second.next

	# advance both nodes until second is at the end
	while second.next is not None:
		first = first.next
		second = second.next

	return first


def print_node(node):
	if node is not None:
		print(node.data)
	else:
		print(None)


# Let's test it!
foo = Node(2)
foo.append(7)
foo.append(9)
foo.append(3)
foo.append(5)
foo.append(13)
print_l(foo)

print('0th to last:', end=' ')
print_node(kth_to_last2(foo, 0))

print('1st to last:', end=' ')
print_node(kth_to_last2(foo, 1))

print('4th to last:', end=' ')
print_node(kth_to_last2(foo, 4))

print('5th to last:', end=' ')
print_node(kth_to_last2(foo, 5))

print('6th to last:', end=' ')
print_node(kth_to_last2(foo, 6))

print('7th to last:', end=' ')
print_node(kth_to_last2(foo, 7))

print('9th to last:', end=' ')
print_node(kth_to_last2(foo, 9))
