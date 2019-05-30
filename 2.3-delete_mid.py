from linked_list import *

def delete_middle(node):
	if node.next is not None:
		node.data = node.next.data
		node.next = node.next.next

# Let's test it!
head = Node(5)
head.append(7)
head.append(9)
head.append(13)

print_l(head)
print('Try deleting 13:', end=' ')
delete_middle(head.search(13))
print_l(head)

print('Try deleting 9:', end=' ')
delete_middle(head.search(9))
print_l(head)

new_head = head.search(7)
print('Try deleting 5:', end=' ')
delete_middle(head.search(5))
print_l(new_head)

print('Try deleting 7:', end=' ')
delete_middle(new_head.search(7))
print_l(new_head)

print('Try deleting 13:', end=' ')
delete_middle(new_head.search(13))
print_l(new_head)
