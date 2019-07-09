def sort_stack(s1):
	s2 = list()
	while s1:
		print('s1:', s1)
		smallest = None
		while s1:
			if smallest is None or s1[-1] < smallest:
				smallest = s1[-1]
			s2.append(s1.pop())
		stored = False
		print('smallest:', smallest)
		count = 0
		while s2:
			if s2[-1] < smallest:
				break
			val = s2.pop()
			if val == smallest:
				count += 1
				continue
			s1.append(val)
		for i in range(count):
			s2.append(smallest)
		print('s2:', s2)
	while s2:
		s1.append(s2.pop())

# Let's test it!
s = [7, 2, 9, 3, 2, 1, 12, 0, 8, 2]
print(s)
sort_stack(s)
print(s)
