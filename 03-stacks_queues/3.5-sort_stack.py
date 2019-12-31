# O(n^2) runtime, O(1) space - we inspect n, n-1, n-2, ..., 1 elements
# and MOVE (not copy) elements between input and temporary stacks
def sort_stack(stack):
	temp = []
	while stack:
		#print('stack:', stack)
		smallest = None
		while stack:
			if smallest is None or stack[-1] < smallest:
				smallest = stack[-1]
			temp.append(stack.pop())
		#print('smallest:', smallest)

		count = 0
		while temp:
			if temp[-1] < smallest:
				break
			elem = temp.pop()
			if elem == smallest:
				count += 1
				continue
			stack.append(elem)

		for i in range(count):
			temp.append(smallest)
		#print('temp:', temp)

	while temp:
		stack.append(temp.pop())


# Let's test it!
foo = [7, 2, 9, 3, 2, 1, 12, 0, 8, 2]
print(foo)
sort_stack(foo)
print(foo)
