from linked_list import *

# Note, n is the larger of the two lists in both solutions
# O(n) runtime, O(n) space - use a set to compare nodes
def intersection(l1, l2):
	l1_nodes = set()
	n = l1
	while n is not None:
		l1_nodes.add(n)
		n = n.next

	n = l2
	while n is not None:
		if n in l1_nodes:
			return n
		n = n.next

	return None

# O(n) runtime, O(1) space - comp. tails, use lengths to find intersection
def intersection2(l1, l2):
	if l1 is None or l2 is None:
		return None

	n1, len_l1 = l1, 1
	while n1.next is not None:
		len_l1 += 1
		n1 = n1.next

	n2, len_l2 = l2, 1
	while n2.next is not None:
		len_l2 += 1
		n2 = n2.next

	if n1 is not n2:
		return None

	if len_l1 > len_l2:
		return find_intersection(l1, l2, len_l1-len_l2)
	else:
		return find_intersection(l2, l1, len_l2-len_l1)


def find_intersection(larger, smaller, diff):
	for i in range(diff):
		larger = larger.next
	while larger is not smaller:
		larger, smaller = larger.next, smaller.next

	return larger


# Let's test it!
foo = Node(7)
foo.append(3)
foo.append(8)
foo.append(9)

bar = Node(5)
bar.append(11)
bar.append(3)
bar.append(6)

baz = Node(12)
baz.append(16)
baz.next.next = foo.next

print('foo:', end=' ')
print_list(foo)
print('3:', foo.next)
print('bar:', end=' ')
print_list(bar)
print('3:', bar.next.next)
print('baz:', end=' ')
print_list(baz)
print('3:', baz.next.next)
print('intersection(foo, bar):', intersection2(foo, bar))
print('intersection(foo, baz):', intersection2(foo, baz))
print('intersection(bar, baz):', intersection2(bar, baz))
