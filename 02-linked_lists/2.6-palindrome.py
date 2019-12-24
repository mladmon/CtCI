from linked_list import *

def palindrome(head):
	chars = []
	n = head
	while n is not None:
		chars.append(str(n.data).lower())
		n = n.next
	return ''.join(chars) == ''.join(reversed(chars))

# Let's test it!
l1 = Node('m')
l1.append('a')
l1.append('r')
l1.append('a')
l1.append('m')

l2 = Node('M')
l2.append('a')
l2.append('R')
l2.append('A')
l2.append('m')

l3 = Node('d')
l3.append('i')
l3.append('7')
l3.append('!')
l3.append('!')
l3.append('7')
l3.append('I')
l3.append('D')

l4 = Node('s')
l4.append('o')
l4.append('r')
l4.append('r')
l4.append('y')

print(palindrome(l1), end=' ')
print_list(l1)
print(palindrome(l2), end=' ')
print_list(l2)
print(palindrome(l3), end=' ')
print_list(l3)
print(palindrome(l4), end=' ')
print_list(l4)
