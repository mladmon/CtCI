from linked_list import *

def delete_middle(node):
	if node is not None and node.next is not None:
		node.data = node.next.data
		node.next = node.next.next

# Let's test it!
foo = Node(5)
foo.append(7)
foo.append(9)
foo.append(13)
print_list(foo)

print('Attempting to delete 13:', end=' ')
delete_middle(foo.search(13))
print_list(foo)

print('Attempting to delete 9: ', end=' ')
delete_middle(foo.search(9))
print_list(foo)

print('Attempting to delete 5: ', end=' ')
delete_middle(foo) # foo is now 7
print_list(foo)

print('Attempting to delete 7: ', end=' ')
delete_middle(foo) # foo is now 13
print_list(foo)

print('Attempting to delete 13:', end=' ')
delete_middle(foo)
print_list(foo)
