from linked_list import *

# O(n) runtime, O(n) space - create a list of nodes, compare to reversed
def is_palindrome(head):
	nodes = []
	n = head
	while n is not None:
		nodes.append(n.data)
		n = n.next

	return nodes == list(reversed(nodes))


# Let's test it!
foo = Node(1)
foo.append(2)
foo.append(7)
foo.append(2)
foo.append(1)

bar = Node(1)
bar.append(2)
bar.append(2)
bar.append(1)

baz = Node(1)
baz.append(2)
baz.append(3)
baz.append(1)

print('foo:', end=' ')
print_list(foo)
print('foo:', is_palindrome(foo))

print('bar:', end=' ')
print_list(bar)
print('bar:', is_palindrome(bar))

print('baz:', end=' ')
print_list(baz)
print('baz:', is_palindrome(baz))
