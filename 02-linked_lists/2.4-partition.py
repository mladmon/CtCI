from linked_list import *

# O(n) runtime, O(1) space - grows new list middle-out
def partition(node, partition):
	head, tail = node, node
	while node is not None:
		next_node = node.next
		if node.data < partition:
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node

		node = next_node

	if tail is not None:
		tail.next = None

	return head


# Let's test it!
foo = Node(3)
foo.append(5)
foo.append(8)
foo.append(5)
foo.append(10)
foo.append(2)
foo.append(1)

print_list(foo)
print('partition: 5')
foo = partition(foo, 5)
print_list(foo)
print()

bar = Node(7)
bar.append(4)

print_list(bar)
print('partition: 10')
bar = partition(bar, 10)
print_list(bar)
print('partition: 5')
bar = partition(bar, 5)
print_list(bar)
print('partition: 3')
bar = partition(bar, 3)
print_list(bar)

baz = None
baz = partition(baz, 5)
print_list(baz)
