from linked_list import *

def delete_middle(node):
	if node.next is not None:
		node.data = node.next.data
		node.next = node.next.next

# Let's test it!
foo = Node(5)
foo.append(7)
foo.append(9)
foo.append(13)

print_list(foo)
print('Try deleting 13:', end=' ')
delete_middle(foo.search(13))
print_list(foo)

print('Try deleting 9:', end=' ')
delete_middle(foo.search(9))
print_list(foo)

new_head = foo.search(7)
print('Try deleting 5:', end=' ')
delete_middle(foo.search(5))
print_list(new_head)

print('Try deleting 7:', end=' ')
delete_middle(new_head.search(7))
print_list(new_head)

print('Try deleting 13:', end=' ')
delete_middle(new_head.search(13))
print_list(new_head)
