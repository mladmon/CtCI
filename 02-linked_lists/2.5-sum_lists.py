from linked_list import *
from collections import namedtuple

# Used in the recursive solution to the FOLLOW UP question below
PartialSum = namedtuple('PartialSum', 'carry sum');


# O(n) runtime, O(n) space (where n is the larger of the two lists)
def sum_lists(l1, l2):
	result, last_digit = None, None
	carry = 0
	while l1 is not None or l2 is not None:
		digit = Node(0)

		if l1 is not None:
			digit.data = l1.data
			l1 = l1.next

		if l2 is not None:
			digit.data += l2.data
			l2 = l2.next

		digit.data += carry

		# calculate the next carry and digit
		carry = digit.data // 10
		digit.data = digit.data % 10

		# append the next digit to the sum
		if result is None:
			result = digit
			last_digit = digit
		else:
			last_digit.next = digit
			last_digit = digit

	if carry == 1:
		last_digit.next = Node(carry)

	return result


# O(n) runtime, O(n) space - recursive solution to the FOLLOW UP question
# Note, this solution only works for operands of the same length
def sum_lists_rec(l1, l2):
	partial_sum = sum_lists_helper(l1, l2)
	if partial_sum.carry == 1:
		final_sum = Node(1)
		final_sum.next = partial_sum.sum
		return final_sum
	else:
		return partial_sum.sum


def sum_lists_helper(l1, l2):
	if l1 is None:
		return None

	partial_sum = sum_lists_helper(l1.next, l2.next)
	if partial_sum is None:
		return PartialSum((l1.data + l2.data) // 10, 
		                   Node((l1.data + l2.data) % 10))
	else:
		carry = (l1.data + l2.data + partial_sum.carry) // 10
		digit = Node((l1.data + l2.data + partial_sum.carry) % 10)
		digit.next = partial_sum.sum

		return PartialSum(carry, digit)


# Let's test it!
foo = Node(7)
foo.append(1)
foo.append(6)

bar = Node(5)
bar.append(9)
bar.append(2)

baz = Node(5)
baz.append(9)
baz.append(9)

biz = Node(6)
biz.append(9)

# example from book
print_list(foo)
print_list(bar)
print_list(sum_lists(foo, bar))
print()

# results in extra carry
print_list(foo)
print_list(baz)
print_list(sum_lists(foo, baz))
print()

# operands have different #s of digits
print_list(biz)
print_list(baz)
print_list(sum_lists(biz, baz))
print()

# tests for FOLLOW UP question
print_list(foo)
print_list(bar)
print_list(sum_lists_rec(foo, bar))
