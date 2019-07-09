class SetOfStacks:
	def __init__(self, threshold):
		self.threshold = threshold
		self.data = []

	def push(self, val):
		if not self.data or len(self.data[-1]) == self.threshold:
			self.data.append([val])
		else:
			self.data[-1].append(val)

	def pop(self, index=-1):
		if self.data: # has at least 1 list w/ 1 element
			val = self.data[index].pop()
			if not self.data[index]:
				del self.data[index]
			return val
		else:
			raise EmptyStackError('pop from an empty stack')

	def pop_at(self, index):
		if index >= len(self.data) or index < 0:
			raise IndexError('substack does not exist')
		return self.pop(index)

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
print('pop:', s.pop())
print('pop:', s.pop())
print('push: 6\npush: 7')
s.push(6)
s.push(7)
print(s.data)
print('pop_at(1):', s.pop_at(1))
print('pop_at(0):', s.pop_at(0))
print('pop:', s.pop())
print(s.data)
print('pop_at(1):', s.pop_at(1))
print(s.data)
print('pop_at(1):', s.pop_at(1)) # raises IndexError exception
