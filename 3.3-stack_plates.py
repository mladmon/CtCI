class SetOfStacks:
	def __init__(self, threshold):
		self.threshold = threshold
		self.data = []

	def push(self, val):
		if not self.data or len(self.data[-1]) == self.threshold:
			self.data.append([val])
		else:
			self.data[-1].append(val)

	def pop(self):
		if self.data: # has at least 1 list w/ 1 element
			val = self.data[-1].pop()
			if not self.data[-1]:
				del self.data[-1]
			return val
		else:
			raise EmptyStackError('pop from an empty stack')

class EmptyStackError(Exception):
	pass

# Let's test it!
s = SetOfStacks(2)
print(s.data)
try:
	s.pop()
except EmptyStackError as err:
	print(err)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.data)
print('pop():', s.pop())
print('pop():', s.pop())
print('push: 6\npush: 7')
s.push(6)
s.push(7)
print(s.data)
