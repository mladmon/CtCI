class EmptyQueueError(Exception):
	pass

class MyQueue:
	def __init__(self, iterable=None):
		if iterable is None:
			self.enqueue_stack = []
		else:
			self.enqueue_stack = list(iterable)
		self.dequeue_stack = []

	def enqueue(self, val):
		self.enqueue_stack.append(val)

	def dequeue(self):
		if not self.dequeue_stack:
			if not self.enqueue_stack:
				raise EmptyQueueError('dequeue from an empty queue')
			else:
				for i in range(len(self.enqueue_stack)):
					self.dequeue_stack.append(self.enqueue_stack.pop())
		return self.dequeue_stack.pop()

# Let's test it!
q = MyQueue([1, 2, 3, 4])
print(q.enqueue_stack, q.dequeue_stack)
print('enqueue: 5')
q.enqueue(5)
print('dequeue:', q.dequeue())
print(q.enqueue_stack, q.dequeue_stack)
print('dequeue:', q.dequeue())
print('dequeue:', q.dequeue())
print('enqueue: 6, 7')
q.enqueue(6)
q.enqueue(7)
print(q.enqueue_stack, q.dequeue_stack)
print('dequeue:', q.dequeue())
print('dequeue:', q.dequeue())
print('dequeue:', q.dequeue())
print(q.enqueue_stack, q.dequeue_stack)
print('dequeue:', q.dequeue())
print('dequeue:', q.dequeue())
