from linked_list import *

def sum_lists(l1, l2):
	carry, n1, n2 = 0, l1, l2
	result = None
	while n1:
		if result is None:
			result = Node((n1.data + n2.data + carry) % 10)
		else:
			result.append((n1.data + n2.data + carry) % 10)
		carry = (n1.data + n2.data) // 10
		n1, n2 = n1.next, n2.next
	if carry:
		result.append(1)
	return result

def sum_lists_rec(l1, l2):
	result = sum_lists_helper(l1, l2)
	if result[0]:
		head = Node(1)
		head.next = result[1]
		return head
	else:
		return result[1]

def sum_lists_helper(l1, l2):
	if l1 is None:
		return None
	result = sum_lists_helper(l1.next, l2.next)
	if result is None:
		result = ((l1.data + l2.data) // 10, Node((l1.data + l2.data) % 10))
	else:
		carry, digit = ((l1.data + l2.data) // 10, 
		                Node((l1.data + l2.data + result[0]) % 10))
		digit.next = result[1]
		result = (carry, digit)
	return result

# Let's test it!
l1 = Node(7)
l1.append(1)
l1.append(6)

l2 = Node(5)
l2.append(9)
l2.append(2) 

l3 = Node(6)
l3.append(1)
l3.append(7)

l4 = Node(2)
l4.append(9)
l4.append(5) 

print_l(l1)
print_l(l2)
print_l(sum_lists(l1, l2))

print_l(l3)
print_l(l4)
print_l(sum_lists_rec(l3, l4))
