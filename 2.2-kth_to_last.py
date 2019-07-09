from linked_list import *

def kth_to_last(head, k):
	size = 0
	n = head
	while n is not None:
		size += 1
		n = n.next
	if size <= k:
		return None
	else:
		n = head
		for i in range(size-k-1):
			n = n.next
		return n

def kth_to_last2(head, k):
	num_moves = 0
	kth, runner = head, head
	while runner is not None:
		if num_moves > k:
			kth = kth.next
		runner = runner.next
		num_moves += 1
	if k >= num_moves:
		return None
	else:
		return kth

# Let's test it!
l1 = Node(2)
l1.append(7)
l1.append(9)
l1.append(3)
l1.append(5)
l1.append(2)

def print_kth(kth):
	if kth:
		print(kth.data)
	else:
		print(repr(None))

print_l(l1)
print('0th to last:', end=' ')
#print_kth(kth_to_last(l1, 0))
print_kth(kth_to_last2(l1, 0))
print('1st to last:', end=' ')
#print_kth(kth_to_last(l1, 1))
print_kth(kth_to_last2(l1, 1))
print('4th to last:', end=' ')
#print_kth(kth_to_last(l1, 4))
print_kth(kth_to_last2(l1, 4))
print('5th to last:', end=' ')
#print_kth(kth_to_last(l1, 5))
print_kth(kth_to_last2(l1, 5))
print('6th to last:', end=' ')
#print_kth(kth_to_last(l1, 6))
print_kth(kth_to_last2(l1, 6))
