# Custom exception class raised in MyQueue instance methods
class EmptyQueueError(Exception):
	pass


# MyQueue class definition
class MyQueue:
	def __init__(self, iterable=None):
		if iterable is None:
			self.enqueue_stack = []
		else:
			self.enqueue_stack = list(iterable)
		self.dequeue_stack = []

	def enqueue(self, elem):
		self.enqueue_stack.append(elem)

	def dequeue(self):
		if self.empty():
			raise EmptyQueueError('dequeue() called on an empty queue')

		if not self.dequeue_stack:
			self.move()

		return self.dequeue_stack.pop()

	def peek(self):
		if self.empty():
			raise EmptyQueueError('peek() called on an empty queue')

		if not self.dequeue_stack:
			self.move()

		return self.dequeue_stack[-1]

	def empty(self):
		return not self.dequeue_stack and not self.enqueue_stack

	def move(self):
		for i in range(len(self.enqueue_stack)):
			self.dequeue_stack.append(self.enqueue_stack.pop())


# Let's test it!
foo = MyQueue([1, 2, 3, 4])
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.enqueue(5)')
foo.enqueue(5)
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.dequeue():', foo.dequeue())
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.peek():', foo.peek())
print('foo.dequeue():', foo.dequeue())
print('foo.dequeue():', foo.dequeue())
print('foo.enqueue(6)')
print('foo.enqueue(7)')
foo.enqueue(6)
foo.enqueue(7)
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.dequeue():', foo.dequeue())
print('foo.dequeue():', foo.dequeue())
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.peek():', foo.peek())
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.dequeue():', foo.dequeue())
print('foo:', foo.enqueue_stack, foo.dequeue_stack)
print('foo.dequeue():', foo.dequeue())
try:
	print('foo.dequeue():', end=' ')
	foo.dequeue()
except EmptyQueueError as err:
	print(err)
