from linked_list import *

# O(n) runtime, O(n) space - use a set to check for duplicate node
def loop_detect(head):
	n = head
	nodes = set()
	while n not in nodes:
		nodes.add(n)
		n = n.next

	return n


# O(n) runtime, O(1) space - use two pointers and difficult logic
def loop_detect2(head):
	slow, fast = head.next, head.next.next
	while slow is not fast:
		slow = slow.next 
		fast = fast.next.next

	# slow, fast, and head are all k steps away from loop beginning
	slow = head
	while slow is not fast:
		slow = slow.next
		fast = fast.next

	return slow


# Let's test it!
foo = Node(1)
foo.append(2)
foo.append(3)
foo.append(4)
foo.append(5)

five = foo.search(5)
three = foo.search(3)
five.next = three

print('foo: 1 2 3 4 5 3 4 5 ...')
loop_start = loop_detect2(foo)
print('loop detected at node:', loop_start.data, f'({loop_start})')
