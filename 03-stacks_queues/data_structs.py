from collections import deque

class EmptyStackError(Exception):
	pass


class EmptyQueueError(Exception):
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
			raise EmptyStackError('tried popping from an empty stack')
		return self.data.pop()

	def peek(self):
		if not self.data:
			raise EmptyStackError('tried peeking from an empty stack')
		return self.data[-1]

	def is_empty(self):
		return not self.data


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
			raise EmptyQueueError('tried removing from an empty queue')
		return self.data.popleft()

	def peek(self):
		if not self.data:
			raise EmptyQueueError('tried peeking from an empty queue')
		return self.data[0]

	def is_empty(self):
		return not self.data


# Let's test it!
if __name__ == '__main__':
	s = stack()
	q = queue([1, 2, 3])

	print('s:', s.data)
	print('s.is_empty():', s.is_empty())
	#print('s.peek():', s.peek()) # raises an EmptyStackError
	print('pushing 5 and 13 onto the stack')
	s.push(5)
	s.push(13)
	print('s:', s.data)
	print('s.pop():', s.pop())
	print('s.peek():', s.peek())
	print()
	
	print('adding 1, 2, and 3 to the queue')
	print('q:', q.data)
	print('q.is_empty():', q.is_empty())
	print('q.peek():', q.peek())
	print('q.remove():', q.remove())
	print('adding 5 to the queue')
	q.add(5)
	print('q:', q.data)
	print('p.peek():', q.peek())

