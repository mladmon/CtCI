from collections import deque

class EmptyStackError(Exception):
	pass

class stack:
	def __init__(self, iterable=None):
		if iterable is None:
			self.data = []
		else:
			self.data = list(iterable)

	def push(self, item):
		self.data.append(item)

	def pop(self):
		if not self.data:
			raise EmptyStackError('pop from an empty stack')
		return self.data.pop()

	def peek(self):
		return self.data[-1]

	def is_empty(self):
		return len(self.data) == 0

class queue:
	def __init__(self, iterable=None):
		if iterable is None:
			self.data = deque()
		else:
			self.data = deque(iterable)

	def add(self, item):
		self.data.append(item)

	def remove(self):
		if not self.data:
			raise IndexError('pop from an empty queue')
		return self.data.popleft()

	def peek(self):
		return self.data[0]

	def is_empty(self):
		return len(self.data) == 0

# Let's test it!
if __name__ == '__main__':
	s = stack()
	q = queue([1, 2, 3])

	print('s', s.data)
	print('s.is_empty()', s.is_empty())
	s.push(5)
	s.push(13)
	print('s', s.data)
	print('s.pop()', s.pop())
	print('s.peek()', s.peek())
	
	print('q', q.data)
	print('q.is_empty()', q.is_empty())
	print('q.peek()', q.peek())
	print('q.remove()', q.remove())
	q.add(30)
	print('q', q.data)
	for i in range(3):
		q.remove()
	print('q', q.data)
	print('q.is_empty()', q.is_empty())
